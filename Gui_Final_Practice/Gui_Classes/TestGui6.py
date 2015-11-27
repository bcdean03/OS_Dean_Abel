__author__ = 'abelamadou'
__author__ = 'abelamadou'
__author__ = 'Dean'
from threading import Thread
from Tkinter import *
import tkinter.messagebox
import re
import tkFont
from PIL import Image, ImageTk
from change_label_color import DisplayClient


class AbeanGui(Thread):
    def __init__(self,master):
        Thread.__init__(self)
        self.root = master
        self.root.title("Abean Groceries")
        self.root.geometry('450x300+200+200')

    def run(self):
        # self.welcome_screen()
        self.cooking_screen()
        while True:
            # c=raw_input("Enter Color of label:")
            # self.label.config(bg=c)
            # c2=raw_input("Enter Color of oval:")
            # self.w1.itemconfig(self.oval,fill=c2)
            c=raw_input("Enter 3 Color(oval,clientName,food)")
            a=c.split(" ")
            self.client_obj.change_oval(a[0])
            self.client_obj.change_label_color( self.client_obj.clientName,a[1])
            self.client_obj.change_label_color( self.client_obj.food,a[2])
            # c2=raw_input("Enter name and color").split(" ")
            a=""
            while a!="1":
                c2=raw_input("Enter name and color")
                a=c2.split(" ")
                self.client_obj.change_label_color(self.client_obj.ingredient[a[0]],a[1])

            # self.client_obj
            # pass


        # cooking_screen()
        # self.root.protocol("WM_DELETE_WINDOW", self.callback)
        # self.root.mainloop()

    def change_label(self):
        if(self.entry_comsumer.get() is not "" and
                       self.entry_producer.get() is not ""and
                       self.entry_buffer_size.get()is not ""):
            if(re.search('[a-zA-Z]', self.entry_comsumer.get()) is None and
                       re.search('[a-zA-Z]', self.entry_producer.get()) is None and
                       re.search('[a-zA-Z]', self.entry_buffer_size.get()) is None):

                if int(self.entry_comsumer.get()) < 2053 and \
                                int(self.entry_producer.get()) < 500 and\
                                int(self.entry_buffer_size.get())>0:
                    # print self.entry_comsumer.get()
                    # print self.entry_producer.get()
                    # print self.entry_buffer_size.get()
                    self.comsumer_amount= self.entry_comsumer.get()
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
                    tkinter.messagebox.showinfo("!!Error!!",detail="Producer(s) < 2053 : Consumer(s) < 500 : Buffer Size > 0")

            else:
                tkinter.messagebox.showinfo("!!Error!!",detail="One of your entries contains a letter or wrong symbol, only integers!")
        else:
            tkinter.messagebox.showinfo("!!Error!!",detail="One of the entries is empty")


        # name ="Thanks for the click"+ yourName.get()
        # labelText.set(name)
        # yourName.delete(0,END)
        # yourName.insert(0,"My name is Abel")
        return

    def welcome_screen(self):
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

        self.button1 = Button(self.root, text="Done",command=self.change_label)
        self.button1.grid(row=4,column=1,sticky=S)

    def onFrameConfigure(self,canvas):
        '''Reset the scroll region to encompass the inner frame'''
        canvas.configure(scrollregion=canvas.bbox("all"))

    def cooking_screen(self):
        # print self.comsumer_amount
        # print self.producer_amount
        # print self.buffer_amount
        self.color="green"
        canvas = Canvas(self.root, borderwidth=0, background="blue",width=700,height=700)
        frame = Frame(canvas, background="blue")
        vsb = Scrollbar(self.root, orient="vertical", command=canvas.yview)
        vsb2 = Scrollbar(self.root, orient="horizontal", command=canvas.xview)
        canvas.configure(xscrollcommand=vsb2.set ,yscrollcommand=vsb.set)
        # canvas.configure()

        vsb2.pack(side='bottom', fill='x')
        vsb.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.create_window((4,4), window=frame, anchor="nw")

        frame.bind("<Configure>", lambda event, canvas=canvas: self.onFrameConfigure(canvas))
        self.populate_frame(frame,100)


    def populate_frame(self,frame2,n):
            # self.label= Label(frame2, text="BONE", bg="green", font=tkFont.Font(family="comic sans ms", size =40),bd=10,relief="ridge", anchor=N)
            # self.label.grid(row=2, column=4)
            # self.w1 = Canvas(frame2, width=20, height=20,background="red")
            # self.oval = self.w1.create_oval(6,6,16,16, fill='green')
            # self.w1.grid(row=2,column=0)

            ingredient=['a','b','c']
            client_label= Label(frame2, text="Client_1->", bg="red", font=tkFont.Font(family="comic sans ms", size =40),bd=10,relief="ridge", anchor=N)
            client_label.grid(row=0, column=4)
            food_label= Label(frame2, text="Burger:", bg="red", font=tkFont.Font(family="comic sans ms", size =40),bd=10,relief="ridge", anchor=N)
            food_label.grid(row=0, column=5)
            ingredient_labels_list={}
            ig=5
            for i in xrange(len(ingredient)):
                ig+=1
                ig_label= Label(frame2, text=ingredient[i], bg="red", font=tkFont.Font(family="comic sans ms", size =40),bd=10,relief="ridge", anchor=N)
                ig_label.grid(row=0, column=ig)
                ingredient_labels_list[ingredient[i]]=ig_label

            w1 = Canvas(frame2, width=20, height=20,background="red")
            oval = w1.create_oval(6,6,16,16, fill='green')
            w1.grid(row=0,column=0)

            self.client_obj=DisplayClient(w1,oval,client_label,food_label,ingredient_labels_list)#canvas,oval,clientName,food,ingredient


     # for row in range(n):
     #        # label1 = Label(frame2, text="Hello",bd=10,relief="ridge", anchor=N)
     #        # label1.grid(row=row, column=1)
     #
     #
     #        w1 = Canvas(frame2, width=20, height=20,background="red")
     #        w1.create_oval(6,6,16,16, fill='green')
     #        w1.grid(row=row,column=0)

            # if row % 2 == 0:
            #     label1= Label(frame2, text="Bread", bg="green", font=tkFont.Font(family="comic sans ms", size =40),bd=10,relief="ridge", anchor=N)
            #     label1.grid(row=row, column=1)
            #     label1= Label(frame2, text="Bread", bg="red", font=tkFont.Font(family="comic sans ms", size =40),bd=10,relief="ridge", anchor=N)
            #     label1.grid(row=row, column=2)
            #     label1= Label(frame2, text="Bread", bg="green", font=tkFont.Font(family="comic sans ms", size =40),bd=10,relief="ridge", anchor=N)
            #     label1.grid(row=row, column=3)
            #     label1= Label(frame2, text="Bread", bg="red", font=tkFont.Font(family="comic sans ms", size =40),bd=10,relief="ridge", anchor=N)
            #     label1.grid(row=row, column=4)
            # else:
            #     label1= Label(frame2, text="Bread", bg="red", font=tkFont.Font(family="comic sans ms", size =40),bd=10,relief="ridge", anchor=N)
            #     label1.grid(row=row, column=1)
            #     label1= Label(frame2, text="Bread", bg="green", font=tkFont.Font(family="comic sans ms", size =40),bd=10,relief="ridge", anchor=N)
            #     label1.grid(row=row, column=2)
            #     label1= Label(frame2, text="Bread", bg="red", font=tkFont.Font(family="comic sans ms", size =40),bd=10,relief="ridge", anchor=N)
            #     label1.grid(row=row, column=3)
            #     label1= Label(frame2, text="Bread", bg="green", font=tkFont.Font(family="comic sans ms", size =40),bd=10,relief="ridge", anchor=N)
            #     label1.grid(row=row, column=4)

if __name__ == '__main__':

    root = Tk()
    AbeanGui(root).start()
    root.mainloop()

