__author__ = 'abelamadou'

from Tkinter  import *
root = Tk()
colour = StringVar()
colour.set('blue')
def colourUpdate():
    l.config(bg='red')
    # root.update()

btn = Button(root, text = "Click Me", command = colourUpdate)
l = Label(root, textvariable=colour, bg = "blue")
l.pack()
btn.pack()
root.mainloop()