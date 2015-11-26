__author__ = 'Dean'
from Tkinter import *

canvas = Canvas(width=300, height=300, bg='white')
canvas.pack(expand=YES, fill=BOTH)

photo=PhotoImage(file='/Users/Dean/PycharmProjects/OS_Dean_Abel/Gui_Practice/picture.gif')
canvas.create_image(250, 0, image=photo, anchor=NW)

widget = Label(canvas, text='AAA', fg='white', bg='black')
widget.pack()
canvas.create_window(100, 100, window=widget)


mainloop()