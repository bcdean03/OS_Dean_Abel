__author__ = 'Dean'
__author__ = 'Dean'
import tkinter as tk
from tkinter import *
import tkFont
from PIL import Image, ImageTk
def populate(frame2):
    '''Put in some fake data'''
    # for row in range(100):
    # Label(frame, text="%s" % 1, width=3, borderwidth="1",
    #          relief="solid").grid(row=1, column=0)
    # t="this is the second column for row %s" %1
    # Label(frame, text=t).grid(row=1, column=1)

    # for row in range(100):
    #     label1 = Label(frame, text="Hello",bd=10,relief="ridge", anchor=N)
    #     label1.grid(row=row, column=0)
    # label1 = Label(frame2, text="Hello",bd=10,relief="ridge", anchor=N)
    # label1.grid(row=0, column=1)
    # label1 = Label(frame2, text="Hello",bd=10,relief="ridge", anchor=N)
    # label1.grid(row=1, column=1)
    # label1= Label(frame2, text="Bread", font=tkFont.Font(family="Helvetica", size =40),bd=10,relief="ridge", anchor=N)
    # label1.grid(row=1, column=1)
    # label1= Label(frame2, text="Bread", bg="red", font=tkFont.Font(family="comic sans ms", size =40),bd=10,relief="ridge", anchor=N)
    # label1.grid(row=0, column=1)
    # label1= Label(frame2, text="Cinammon",bg="green", font=tkFont.Font(family="comic sans ms", size =40),bd=10,relief="ridge", anchor=N)
    # label1.grid(row=2,column=1)
    # load = Image.open('space_resized_image.png')
    # render = ImageTk.PhotoImage(load)
    # img = Label(frame2,image=render, bg="green",text="SPACE",fg="black",font=tkFont.Font(family="comic sans ms", size =20),compound="bottom",borderwidth=15,relief="ridge")
    # img.image = render
    # img.grid(row=3,column=1)
    # w1 = Canvas(frame2, width=20, height=20,background="red")
    # w1.create_oval(6,6,16,16, fill='green', )
    # w1.grid(row=0,column=0)
    # w1 = Canvas(frame2, width=20, height=20,background="red")
    # w1.create_oval(6,6,16,16, fill='green', )
    # w1.grid(row=1,column=0)
    # w1 = Canvas(frame2, width=20, height=20,background="red")
    # w1.create_oval(6,6,16,16, fill='green', )
    # w1.grid(row=2,column=0)
    # w1 = Canvas(frame2, width=20, height=20,background="red")
    # w1.create_oval(6,6,16,16, fill='green', )
    # w1.grid(row=3,column=0)

    for row in range(100):
        # label1 = Label(frame2, text="Hello",bd=10,relief="ridge", anchor=N)
        # label1.grid(row=row, column=1)
        label1= Label(frame2, text="Bread", bg="green", font=tkFont.Font(family="comic sans ms", size =40),bd=10,relief="ridge", anchor=N)
        label1.grid(row=row, column=1)
        w1 = Canvas(frame2, width=20, height=20,background="red")
        w1.create_oval(6,6,16,16, fill='green')
        w1.grid(row=row,column=0)



        label1= Label(frame2, text="Bread", bg="green", font=tkFont.Font(family="comic sans ms", size =40),bd=10,relief="ridge", anchor=N)
        label1.grid(row=row, column=2)
        label1= Label(frame2, text="Bread", bg="green", font=tkFont.Font(family="comic sans ms", size =40),bd=10,relief="ridge", anchor=N)
        label1.grid(row=row, column=3)
        label1= Label(frame2, text="Bread", bg="green", font=tkFont.Font(family="comic sans ms", size =40),bd=10,relief="ridge", anchor=N)
        label1.grid(row=row, column=4)


    # for row in range(100):
    #     Label(frame, text="%s" % row, width=3, borderwidth="1",
    #              relief="solid").grid(row=row, column=0)
    #
    #
    #     t="this is the second column for row %s" %row
    #     Label(frame, text=t).grid(row=row, column=1)


def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))

root = Tk()
canvas = Canvas(root, borderwidth=0, background="red",width=700,height=700)
frame = Frame(canvas, background="red")
vsb = Scrollbar(root, orient="vertical", command=canvas.yview)
vsb2 = Scrollbar(root, orient="horizontal", command=canvas.xview)
canvas.configure(xscrollcommand=vsb2.set ,yscrollcommand=vsb.set)
# canvas.configure()

vsb2.pack(side='bottom', fill='x')
vsb.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((4,4), window=frame, anchor="nw")

frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

populate(frame)

root.mainloop()
