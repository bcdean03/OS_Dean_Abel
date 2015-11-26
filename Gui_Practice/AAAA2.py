__author__ = 'abelamadou'
__author__ = 'Dean'
# __author__ = 'abelamadou'
from threading import Thread
from Tkinter import *
import tkinter.messagebox
from time import sleep
import re
import tkFont


class AbeanGui(Thread):
    def __init__(self,master):
        Thread.__init__(self)
        self.root = master
        self.root.title("Abean Groceries")
        self.root.geometry('450x300+200+200')


    def run(self):
        # self.welcome_screen()
        self.cooking_screen()
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

                    #
                    # self.button1.grid_forget()
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



    def cooking_screen(self):
        # print self.comsumer_amount
        # print self.producer_amount
        # print self.buffer_amount

        # frame = Frame(self.root)
        # frame2 = Frame(self.root, bg='blue')
        # frame2.grid()


        frame2 = Canvas(self.root, width=500, height=300,background="blue",scrollregion=(0,0,3000,3000))
        frame2.grid()

        # frame3 = Frame(frame2)
        # frame3.pack(side=RIGHT)

        scr_h1 = Scrollbar(frame2,orient=HORIZONTAL)
        scr_h1.pack(side=BOTTOM,fill=X)
        scr_h1.config(command=frame2.xview)

        scr_v1 = Scrollbar(frame2,orient=VERTICAL)
        scr_v1.pack(side=RIGHT,fill=Y)
        scr_v1.config(command=frame2.yview)

        frame2.config(xscrollcommand=scr_h1.set,yscrollcommand=scr_v1.set)
        # frame2.pack(fill=BOTH,expand=True)

        # inserted to see if it's actually scrolling
        frame2.create_oval(0,0,50,50,fill='red')


        label1 = Label(frame2, text="Hello",bd=10,relief="ridge")
        label1.grid(row=0, column=1)
        label1 = Label(frame2, text="Hello",bd=10,relief="ridge", anchor=N)
        label1.grid(row=1, column=1)
        label1= Label(frame2, text="Bread", font=tkFont.Font(family="Helvetica", size =40),bd=10,relief="ridge", anchor=N)
        label1.grid(row=1, column=1)
        label1= Label(frame2, text="Bread", bg="red", font=tkFont.Font(family="Helvetica", size =40),bd=10,relief="ridge", anchor=N)
        label1.grid(row=0, column=1)
        label1= Label(frame2, text="Cinammon",bg="green", font=tkFont.Font(family="Helvetica", size =40),bd=10,relief="ridge", anchor=N)
        label1.grid(row=2,column=1)
        label1= Label(frame2, text="Cinammon",bg="green", font=tkFont.Font(family="Helvetica", size =40),bd=10,relief="ridge", anchor=N)
        label1.grid(row=3,column=1)
        label1= Label(frame2, text="Cinammon",bg="green", font=tkFont.Font(family="Helvetica", size =40),bd=10,relief="ridge", anchor=N)
        label1.grid(row=4,column=1)

        w2 = Canvas(frame2, width=20, height=20,background="red")
        w2.create_oval(6,6,16,16, fill='green', )
        w2.grid(row=0,column=0)
        w2 = Canvas(frame2, width=20, height=20,background="red")
        w2.create_oval(6,6,16,16, fill='green', )
        w2.grid(row=1,column=0)
        w2 = Canvas(frame2, width=20, height=20,background="red")
        w2.create_oval(6,6,16,16, fill='green', )
        w2.grid(row=2,column=0)
        w2 = Canvas(frame2, width=20, height=20,background="red")
        w2.create_oval(6,6,16,16, fill='green', )
        w2.grid(row=3,column=0)






        # # frame = Frame(self.root)
        # frame2 = Frame(self.root)
        # frame2.pack(side=RIGHT)
        #
        # w1 = Canvas(frame2, width=600, height=300,background="white", scrollregion=(0,0,3000,3000))
        #
        #
        # scr_h1 = Scrollbar(frame2,orient=HORIZONTAL)
        # scr_h1.pack(side=BOTTOM,fill=X)
        # scr_h1.config(command=w1.xview)
        #
        # scr_v1 = Scrollbar(frame2,orient=VERTICAL)
        # scr_v1.pack(side=RIGHT,fill=Y)
        # scr_v1.config(command=w1.yview)
        #
        # w1.config(xscrollcommand=scr_h1.set,yscrollcommand=scr_v1.set)
        # w1.pack(fill=BOTH,expand=True)
        #
        # # inserted to see if it's actually scrolling
        # w1.create_oval(0,0,50,50,fill='red')
        # pass
if __name__ == '__main__':

    root = Tk()
    AbeanGui(root).start()
    root.mainloop()

