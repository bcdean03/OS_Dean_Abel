__author__ = 'Dean'
from Tkinter import *
from PIL import Image, ImageTk


master = Tk()
base_width = 50
height_size = 50
w = Canvas(master, width=1000, height=1000)
load = Image.open('hiking.png')
# width_percent = (base_width*.5 / float(load.size[0]))
# height_size = int((float(load.size[1]) * float(width_percent)))
img = load.resize((base_width, height_size), Image.ANTIALIAS)
img.save("hiking_resized_image.png")
render = ImageTk.PhotoImage(img)
img = Label(image=render, bg="red")
img.image = render
x = 0
# for i in range(0,50):
#     x+=100
#     w.create_image(50,50+x,image=img.image)
# vbar.pack(side=RIGHT,fill=Y)
# vbar.config(command=w.yview)
# w.config(yscrollcommand=vbar.set)
w.pack()
mainloop()








