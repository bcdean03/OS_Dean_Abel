__author__ = 'abelamadou'
from threading import Thread
from Tkinter import *
import tkinter.messagebox
import tkFont

root = Tk()
frame = Frame(root, bd=2, relief=SUNKEN)

frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

xscrollbar = Scrollbar(frame, orient=HORIZONTAL)
xscrollbar.grid(row=1, column=0, sticky=E+W)

yscrollbar = Scrollbar(frame)
yscrollbar.grid(row=0, column=1, sticky=N+S)


# canvas = Canvas(frame, bd=0,
#                 xscrollcommand=xscrollbar.set,
#                 yscrollcommand=yscrollbar.set)

canvas = Canvas(frame, bd=0,background="yellow", scrollregion=(0, 0, 30000, 30000),
                xscrollcommand=xscrollbar.set,
                yscrollcommand=yscrollbar.set)
canvas.grid(row=0, column=0, sticky=N+S+E+W)


xscrollbar.config(command=canvas.xview)
yscrollbar.config(command=canvas.yview)


label1 = Label(canvas, text="Hello", bd=10,relief="ridge", anchor=N)
label1.grid(row=0, column=1)
# label1 = Label(canvas, text="Hello", bd=10,relief="ridge", anchor=N)
# label1.grid(row=1, column=1)
# label1= Label(canvas, text="Bread", font=tkFont.Font(family="Helvetica", size =40),bd=10,relief="ridge", anchor=N)
# label1.grid(row=1, column=1)
# label1= Label(canvas, text="Bread", bg="red", font=tkFont.Font(family="Helvetica", size =40),bd=10,relief="ridge", anchor=N)
# label1.grid(row=0, column=1)
# label1= Label(canvas, text="Cinammon", bg="green", font=tkFont.Font(family="Helvetica", size =40),bd=10,relief="ridge", anchor=N)
# label1.grid(row=2,column=1)
# label1= Label(canvas, text="Cinammon", bg="green", font=tkFont.Font(family="Helvetica", size =40),bd=10,relief="ridge", anchor=N)
# label1.grid(row=3,column=1)
canvas.create_window(100,100,window=label1)

canvas.create_window()
canvas.create_oval(0,0,50,50,fill='red')

frame.pack()

root.mainloop()