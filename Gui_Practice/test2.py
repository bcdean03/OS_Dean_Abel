__author__ = 'Dean'
import tkinter as tk
from tkinter import *
def populate(frame):
    '''Put in some fake data'''
    # for row in range(100):
    # Label(frame, text="%s" % 1, width=3, borderwidth="1",
    #          relief="solid").grid(row=1, column=0)
    # t="this is the second column for row %s" %1
    # Label(frame, text=t).grid(row=1, column=1)

    for row in range(100):
        label1 = Label(frame, text="Hello",bd=10,relief="ridge", anchor=N)
        label1.grid(row=row, column=0)

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
canvas = Canvas(root, borderwidth=0, background="#ffffff")
frame = Frame(canvas, background="#ffffff")
vsb = Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=vsb.set)

vsb.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((4,4), window=frame, anchor="nw")

frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

populate(frame)

root.mainloop()
