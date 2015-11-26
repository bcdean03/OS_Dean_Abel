__author__ = 'Dean'
__author__ = 'abelamadou'
#Canvas->http://www.java2s.com/Tutorial/Python/0360__Tkinker/AddLabeltocanvas.htm
from tkinter import *
from threading import Thread
from time import sleep
from PIL import Image, ImageTk
root = Tk()

frame2 = Frame(root,background="blue")
frame2.pack()

w1 = Canvas(frame2, width=1000, height=1000,background="green", scrollregion=(0,0,3000,3000))


scr_h1 = Scrollbar(frame2,orient=HORIZONTAL)
scr_h1.pack(side=BOTTOM,fill=X)
scr_h1.config(command=w1.xview)

scr_v1 = Scrollbar(frame2,orient=VERTICAL)
scr_v1.pack(side=RIGHT,fill=Y)
scr_v1.config(command=w1.yview)

w1.config(xscrollcommand=scr_h1.set,yscrollcommand=scr_v1.set)
w1.pack(fill=BOTH,expand=YES)

w1.create_oval(5,5,50,50,fill='red')

# labelText = StringVar() # StringVar() Allows you to enter Strings
# labelText.set(" ".join(["a","c","d","a","c","d"]))
# # label1= Label(w1, text="hhhoooooooooooooo",height=4)#Attribute want label to have
# label1 = Label(w1,bg="red",fg="yellow",height=4, width=6)
# photo=PhotoImage(file='/Users/Dean/PycharmProjects/OS_Dean_Abel/Gui_Practice/resized_image.gif')
load = Image.open('hiking_resized_image.png')
render = ImageTk.PhotoImage(load)

img = Label(image=render, bg="red")
img.image = render
# w1.create_image(256,256,image=img.image)

def create_image():
    sleep(5)
    w1.create_image(60, 0, image=img.image, anchor=NW)
    w1.create_oval(5,5,50,50,fill='green')

# w1.create_window(70, 10, window=label1)
# create_image()
Thread(target=create_image).start()
photo1=PhotoImage(file='/Users/Dean/PycharmProjects/OS_Dean_Abel/Gui_Practice/red_resized_image.gif')
w1.create_image(60,0, image=photo1, anchor=NW)
root.mainloop()
