from threading import Thread
from Tkinter import *
import tkinter.messagebox
from time import sleep
import re
import tkFont
from PIL import Image, ImageTk

class AbeanGui(Thread):
    def __init__(self,master):
        Thread.__init__(self)
        self.root = master
        self.root.title("Abean Groceries")
        self.root.geometry('450x300+200+200')
    def run(self):
        self.cooking_screen()
    def cooking_screen(self):
        frame2 = Canvas(self.root, borderwidth=5, width=200, height=100, bg='blue')
        scrollbar = Scrollbar(frame2)
        scrollbar.config(command=frame2.yview)
        frame2.grid(column=0,row=0,columnspan=3,rowspan=2)
        self.populate_frame(frame2)

    def populate_frame(self,frame2):
        label1 = Label(frame2, text="Hello",bd=10,relief="ridge", anchor=N)
        label1.grid(row=0, column=1)
        label1 = Label(frame2, text="Hello",bd=10,relief="ridge", anchor=N)
        label1.grid(row=1, column=1)
        label1= Label(frame2, text="Bread", font=tkFont.Font(family="Helvetica", size =40),bd=10,relief="ridge", anchor=N)
        label1.grid(row=1, column=1)
        label1= Label(frame2, text="Bread", bg="red", font=tkFont.Font(family="comic sans ms", size =40),bd=10,relief="ridge", anchor=N)
        label1.grid(row=0, column=1)
        label1= Label(frame2, text="Cinammon",bg="green", font=tkFont.Font(family="comic sans ms", size =40),bd=10,relief="ridge", anchor=N)
        label1.grid(row=2,column=1)
        label1= Label(frame2, text="Cinammon",bg="green", font=tkFont.Font(family="comic sans ms", size =40),bd=10,relief="ridge", anchor=N)
        label1.grid(row=3,column=1)
        w1 = Canvas(frame2, width=20, height=20,background="red")
        w1.create_oval(6,6,16,16, fill='green', )
        w1.grid(row=0,column=0)
        w1 = Canvas(frame2, width=20, height=20,background="red")
        w1.create_oval(6,6,16,16, fill='green', )
        w1.grid(row=1,column=0)
        w1 = Canvas(frame2, width=20, height=20,background="red")
        w1.create_oval(6,6,16,16, fill='green', )
        w1.grid(row=2,column=0)
        w1 = Canvas(frame2, width=20, height=20,background="red")
        w1.create_oval(6,6,16,16, fill='green', )
        w1.grid(row=3,column=0)
if __name__ == '__main__':
    root = Tk()
    AbeanGui(root).start()
    root.mainloop()
