__author__ = 'Dean'
from Tkinter import *
from PIL import Image, ImageTk


master = Tk()

w = Canvas(master, width=600, height=700)
w.pack()
load = Image.open('hiking.png')
render = ImageTk.PhotoImage(load)

img = Label(image=render, bg="red")
img.image = render
w.create_image(256,256,image=img.image)
mainloop()