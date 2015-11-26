# __author__ = 'abelamadou'
from threading import Thread
from Tkinter import *
from time import sleep





def cooking_screen():
   # frame2 = Frame(root)
   #      frame2.pack(side=RIGHT)
   #
   #      w1 = Canvas(frame2, width=600, height=300,background="white", scrollregion=(0,0,3000,3000))
   #
   #
   #      scr_h1 = Scrollbar(frame2,orient=HORIZONTAL)
   #      scr_h1.pack(side=BOTTOM,fill=X)
   #      scr_h1.config(command=w1.xview)
   #
   #      scr_v1 = Scrollbar(frame2,orient=VERTICAL)
   #      scr_v1.pack(side=RIGHT,fill=Y)
   #      scr_v1.config(command=w1.yview)
   #
   #      w1.config(xscrollcommand=scr_h1.set,yscrollcommand=scr_v1.set)
   #      w1.pack(fill=BOTH,expand=True)
   #
   #  # inserted to see if it's actually scrolling
   #  w1.create_oval(0,0,50,50,fill='red')
   pass


class AbeanGui(Thread):
    def __init__(self,master):
        Thread.__init__(self)
        self.root = master
        self.root.title("Abean Groceries")
        # self.root.geometry('450x300+200+200')


    def run(self):
        self.welcome_screen()
        # cooking_screen()
        # self.root.protocol("WM_DELETE_WINDOW", self.callback)
        # self.root.mainloop()

    def changeLabel(self):
        # print self.producer_number.get()
        if(int())
        print self.entry_comsumer.get()
        print self.entry_producer.get()
        print self.entry_buffersize.get()
        # name ="Thanks for the click"+ yourName.get()
        # labelText.set(name)
        # yourName.delete(0,END)
        # yourName.insert(0,"My name is Abel")
        return
    def welcome_screen(self):
        label_comsumer = Label(self.root,text="Number of Comsumer")
        label_producer =Label(self.root,text="Number of Producer")
        label_buffersize =Label(self.root,text="Buffer Size")

        self.entry_comsumer = Entry(self.root)
        self.entry_producer = Entry(self.root)
        self.entry_buffersize = Entry(self.root)

        label_comsumer.grid(row=0,column=0,sticky=E)
        label_producer.grid(row=1,sticky=E)
        label_buffersize.grid(row=2,column=0,sticky=E)

        self.entry_comsumer.grid(row=0,column=1,sticky=E)
        self.entry_producer.grid(row=1,column=1,sticky=E)
        self.entry_buffersize.grid(row=2,column=1,sticky=E)

        button1 = Button(self.root, text="Done",command=self.changeLabel)
        button1.grid(row=4,column=1,sticky=S)

if __name__ == '__main__':

    root = Tk()
    AbeanGui(root).start()
    root.mainloop()

