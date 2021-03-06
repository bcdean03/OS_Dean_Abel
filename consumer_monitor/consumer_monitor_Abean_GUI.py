__author__ = 'Dean Bailey abelamadou'
from threading import Thread
from Tkinter import *
import tkMessageBox
import re
import socket
import tkFont
from update_grid import DisplayClient
from recipe_module import get_food_and_recipe,create_recipe_dictionary


class ConsumerMonitorAbeanGui(Thread):
    '''
    This class manages the user client socket, the simulated client sockets, and the GUI. As each
    client thread is run, it updates the GUI via update_grid objects which are linked to specific rows and
    clients. The GUI is updated every time the client receives their requested item from the server.
    '''
    # consumer_amount = -1

    def __init__(self,master):
        '''
        intitlize GUI with a title
        :param master: This is the tkinter window
        :return:
        '''
        Thread.__init__(self)
        self.root = master
        self.root.title("Abean Groceries")
        # self.done_lock = RLock()
        # self.done_counter=0

    def run(self):
        self.welcome_screen()

    def change_screen(self):
        '''
        This method is the method that is called when the user presses the "Done" button. It has a few checks
        based on whether the first user inputs too big of numbers that out did the limitations of our computers
        for the number of producers and consumers, or if they didnt input a correct string, including empty entries.
        This method also removes all the widgets created in the root and switches it too the next part of the GUI. Which
        is to update the clients requests and information received back from the server.
        :return:
        '''
        if(self.entry_comsumer.get() is not "" and
                       self.entry_producer.get() is not ""and
                       self.entry_buffer_size.get()is not ""):
            if(re.search('[a-zA-Z]', self.entry_comsumer.get()) is None and
                       re.search('[a-zA-Z]', self.entry_producer.get()) is None and
                       re.search('[a-zA-Z]', self.entry_buffer_size.get()) is None):

                if int(self.entry_comsumer.get()) < 2053 and \
                                int(self.entry_producer.get()) < 500 and\
                                int(self.entry_buffer_size.get())>0:

                    self.consumer_amount= self.entry_comsumer.get()
                    self.producer_amount= self.entry_producer.get()
                    self.buffer_amount=  self.entry_buffer_size.get()
                    self.label_comsumer.destroy()
                    self.label_producer.destroy()
                    self.label_buffersize.destroy()
                    self.entry_comsumer.destroy()
                    self.entry_producer.destroy()
                    self.entry_buffer_size.destroy()
                    self.button1.destroy()
                    self.cooking_screen()
                else:
                    tkMessageBox.showinfo("!!Error!!",detail="Producer(s) < 2053 : Consumer(s) < 500 : Buffer Size > 0")

            else:
                tkMessageBox.showinfo("!!Error!!",detail="One of your entries contains a letter or wrong symbol, only integers!")
        else:
            tkMessageBox.showinfo("!!Error!!",detail="One of the entries is empty")

        return

    def welcome_screen(self):
        '''
        This screen is the first GUI that gets popped up to the main user to specify the number of producers, consumers
        and the buffer size.
        :return:
        '''
        self.label_comsumer = Label(self.root,text="Number of Consumer(s)")
        self.label_producer =Label(self.root,text="Number of Producer(s)")
        self.label_buffersize =Label(self.root,text="Buffer Size")

        self.entry_comsumer = Entry(self.root)
        self.entry_producer = Entry(self.root)
        self.entry_buffer_size = Entry(self.root)

        self.label_comsumer.grid(row=0,column=0,sticky=E)
        self.label_producer.grid(row=1,sticky=E)
        self.label_buffersize.grid(row=2,column=0,sticky=E)

        self.entry_comsumer.grid(row=0,column=1,sticky=E)
        self.entry_producer.grid(row=1,column=1,sticky=E)
        self.entry_buffer_size.grid(row=2,column=1,sticky=E)

        self.button1 = Button(self.root, text="Done",command=self.change_screen)
        self.button1.grid(row=4,column=1,sticky=W+E+N+S)


    def configure_canvas(self,canvas):
        '''
        Configure the scroll region to all of the canvas
        '''
        canvas.configure(scrollregion=canvas.bbox("all"))

    def cooking_screen(self):
        '''
        This is the method that sets up the second gui screen using a frame inside of a canvas. On that canvas
        a horizontal and vertical scrollbar was implemented. In that frame we placed a grid which held the information
        of each client.
        :return:
        '''
        self.main()

        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        canvas = Canvas(self.root, borderwidth=0, background="blue")
        frame = Frame(canvas, background="blue")
        vsb = Scrollbar(self.root, orient="vertical", command=canvas.yview)
        vsb2 = Scrollbar(self.root, orient="horizontal", command=canvas.xview)
        canvas.configure(xscrollcommand=vsb2.set ,yscrollcommand=vsb.set)
        # canvas.configure()

        vsb2.pack(side='bottom', fill='x')
        vsb.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.create_window((4,4), window=frame, anchor="nw")

        frame.bind("<Configure>", lambda event, canvas=canvas: self.configure_canvas(canvas))
        self.consumers(frame)

    def main(self):
        '''
        This method sets up the first socket to excahgne the infromation about how many producers
        the server should have and the buffer size of each queue
        :return:
        '''
        try:
            s = socket.socket()
            s.connect(("192.168.1.194",5002))
            # s.connect(("10.136.139.204",5002))
            # s.connect(("10.0.0.9",5002))#request a connection with the listening server
            # s.connect(("192.168.1.193",5002))#request a connection with the listening server
            str_of_list= "%s %s"%(self.producer_amount,self.buffer_amount)
            s.send(str_of_list)
            data = s.recv(1024)
            if data != "Ready...":
                print "Error happened"
                s.close()
                exit(0)
        except socket.error as error:
            print "{"+str(error)+"}","Wasn't able to send 'Done' because lost connection"
            s.close()
            root.destroy()
            exit(0)
        print "!!CLOSING!!"
        s.close()

    def consumers(self,frame2):
        '''
        This method creates the DisplayClient object that is contantly getting updated in the gui. These objects are connected
        to the clients and well as to each row for client information within the gui.
        Colors:
        red-> Haven't set nor received the item.
        green->Sent and received
        yellow->Sent, but waiting on sever to produce the item
        orange->sockets closed and client finished
        purple->got all items for the list
        green oval-> finished
        red oval->still in process of getting items
        :param frame2: This is the frame that contains the grid of client information
        :return:
        '''
        print "+++++++Going to make",self.consumer_amount,"Consumers+++++++"
        id = 0
        for i in xrange(int(self.consumer_amount)):
            try:

                food, ingredient = get_food_and_recipe(create_recipe_dictionary())

                client_label= Label(frame2, text="Client_{} ->".format(id+1),fg="black", bg="#99ffff", font=tkFont.Font(family="comic sans ms", size =20),bd=10,relief="ridge", anchor=N)
                client_label.grid(row=i, column=4,sticky=W+E+N+S)
                food_label= Label(frame2, text=food+":",fg="white", bg="red", font=tkFont.Font(name="underlined_font", underline=True,family="comic sans ms", size =20),bd=10,relief="ridge", anchor=N)
                food_label.grid(row=i, column=5,sticky=W+E+N+S)
                ingredient_labels_list = {}
                ig=5
                for b in xrange(len(ingredient)):
                    ig+=1
                    ig_label= Label(frame2, text=ingredient[b], bg="red", font=tkFont.Font(family="comic sans ms", size =20),bd=10,relief="ridge", anchor=N)
                    ig_label.grid(row=i, column=ig, sticky=W+E+N+S)
                    ingredient_labels_list[ingredient[b]]=ig_label

                w1 = Canvas(frame2, width=20, height=20,background="blue")
                oval = w1.create_oval(6,6,16,16, fill='red')
                w1.grid(row=i,column=0)

                client_obj=DisplayClient(w1,oval,client_label, food_label, ingredient_labels_list)
                Thread(target=self.client_socket_thr, args=(food, ingredient, "Client_{}".format(id), client_obj)).start()
            except Exception as e:
                print "Exception:",e
                print "Too many clients and producers combined to handle."
                print "Stopping at client:",id
                break
            id += 1
        print "{{{{{Finishing making", self.consumer_amount, "Consumers}}}}}"

    def client_socket_thr(self,food,recipe_list,c_n,client_obj):
        '''
        This is the client threads that does the communication between the server and the client. This sends and receives
        items back and forth. This method also updates the DisplayClient objects which in turn updates the gui
        to the colors specified here and the method above. It shows the producers who produced the item that
        each client received from the server as well.
        :param x: client name changing
        :param c_n: client name
        :return:
        '''
        buffer_server = ("192.168.1.194",5007)
        # buffer_server = ("10.136.139.204",5007)
        # buffer_server = ("10.0.0.9",5007)
        # buffer_server = ("192.168.1.193",5007)

        s = socket.socket()
        while True:
            try:
                s.connect(buffer_server)#request a connection with the listening server
                break
            except socket.error:
                print "Attempting to reconnect"
                s.close()
                s=socket.socket()
        # print c_n,"Connected to:->",buffer_server
        # print c_n,"Sending:->",str_list

        #lock.acquire()
        #print c_n,"Food:->",food,": Recipe_list:->",recipe_list
        #lock.release()
        for i in recipe_list:
            #lock.acquire()
            #print ">>>>",c_n,"Sending:->",i
            #lock.release()
            client_obj.change_label_color(client_obj.ingredient[i],"yellow")
            s.send(i)

            ingr = s.recv(1024)
            if not ingr:
                continue
            else:
                l = ingr.split("*")
                client_obj.change_label_color(client_obj.ingredient[l[1]],"green")
                client_obj.change_label_name(client_obj.ingredient[l[1]],l[0]+"\n"+l[1])
                #lock.acquire()
                #print "<<<<",c_n, "Received:->",ingr
                #lock.release()
        try:
            #print ">>>>",c_n,"Sending:->'Done'"
            s.send("Done")        # print c_n,"Received:->",received
            client_obj.change_oval("green")
            client_obj.change_label_color(client_obj.clientName,"orange")
            client_obj.change_label_color(client_obj.food,"purple")
            # self.done_lock.acquire()
            # self.done_counter+=1
            # self.done_lock.release()
            # if(self.done_counter== int(self.consumer_amount)):
            #     tkinter.messagebox.showinfo("Done Abean",detail="All The clients have gotten their Ingredient")
            s.close()
        except socket.error as error:
            print "{"+error+"}","Wasn't able to send 'Done' because lost connection"




if __name__ == '__main__':

    root = Tk()
    ConsumerMonitorAbeanGui(root).start()
    root.mainloop()

