__author__ = 'abelamadou'
from threading import Thread
from Tkinter import *
import tkinter.messagebox
import tkFont

root = Tk()
frame = Frame(root, bd=2,bg='blue', relief=SUNKEN)

frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

xscrollbar = Scrollbar(frame, orient=HORIZONTAL)
xscrollbar.grid(row=1, column=0, sticky=E+W)

yscrollbar = Scrollbar(frame)
yscrollbar.grid(row=0, column=1, sticky=N+S)


# canvas = Canvas(frame, bd=0,
#                 xscrollcommand=xscrollbar.set,
#                 yscrollcommand=yscrollbar.set)

canvas = Canvas(frame, bd=0,background="yellow", scrollregion=(0, 0, 30000, 30000),width=1000, height=1000,
                xscrollcommand=xscrollbar.set,
                yscrollcommand=yscrollbar.set)
canvas.grid(row=0, column=0, sticky=N+S+E+W)
# canvas.pack(fill=BOTH,expand=True)


xscrollbar.config(command=canvas.xview)
yscrollbar.config(command=canvas.yview)


# label1 = Label(canvas, text="Hello", bd=10,relief="ridge", anchor=N)
# label1.grid(row=0, column=1)
# label2 = Label(canvas, text="Hello", bd=10,relief="ridge", anchor=N)
# label2.grid(row=1, column=1)
# label3= Label(canvas, text="Bread", font=tkFont.Font(family="Helvetica", size =40),bd=10,relief="ridge", anchor=N)
# label3.grid(row=1, column=1)
# label4= Label(canvas, text="Bread", bg="red", font=tkFont.Font(family="Helvetica", size =40),bd=10,relief="ridge", anchor=N)
# label4.grid(row=0, column=1)
# label5= Label(canvas, text="Cinammon", bg="green", font=tkFont.Font(family="Helvetica", size =40),bd=10,relief="ridge", anchor=N)
# label5.grid(row=2,column=1)
# label6= Label(canvas, text="Cinammon", bg="green", font=tkFont.Font(family="Helvetica", size =40),bd=10,relief="ridge", anchor=N)
# label6.grid(row=3,column=1)
# canvas.config(scrollregion=canvas.bbox("all"))
frame2 = Frame(canvas, borderwidth=5, bg='blue')
frame2.grid_rowconfigure(0, weight=1)
frame2.grid_columnconfigure(0, weight=1)
frame2.grid(row=0, column=1)

label1 = Label(frame2, text="Hello", bd=10,relief="ridge", anchor=N)
label1.grid(row=0, column=1)
label1 = Label(frame2, text="Hello", bd=10,relief="ridge", anchor=N)
label1.grid(row=1, column=1)
label1= Label(frame2, text="Bread", font=tkFont.Font(family="Helvetica", size =40),bd=10,relief="ridge", anchor=N)
label1.grid(row=1, column=1)
label1= Label(frame2, text="Bread", bg="red", font=tkFont.Font(family="Helvetica", size =40),bd=10,relief="ridge", anchor=N)
label1.grid(row=0, column=1)
label1= Label(frame2, text="Cinammon", bg="green", font=tkFont.Font(family="Helvetica", size =40),bd=10,relief="ridge", anchor=N)
label1.grid(row=2,column=1)
label1= Label(frame2, text="Cinammon", bg="green", font=tkFont.Font(family="Helvetica", size =40),bd=10,relief="ridge", anchor=N)
label1.grid(row=3,column=1)
label1= Label(frame2, text="Cinammon", bg="green", font=tkFont.Font(family="Helvetica", size =40),bd=10,relief="ridge", anchor=N)
label1.grid(row=4,column=1)

# canvas.create_window(400, 400, window=frame2)

canvas.create_oval(0,1,50,50,fill='red')

frame.pack()

root.mainloop()