__author__ = 'abelamadou'
#Canvas->http://www.java2s.com/Tutorial/Python/0360__Tkinker/AddLabeltocanvas.htm
from tkinter import *

root = Tk()

frame2 = Frame(root,background="blue")
frame2.pack()
# frame2.pack(side=RIGHT)

w1 = Canvas(frame2, width=450, height=300,background="green", scrollregion=(0,0,3000,3000))


scr_h1 = Scrollbar(frame2,orient=HORIZONTAL)
scr_h1.pack(side=BOTTOM,fill=X)
scr_h1.config(command=w1.xview)

scr_v1 = Scrollbar(frame2,orient=VERTICAL)
scr_v1.pack(side=RIGHT,fill=Y)
scr_v1.config(command=w1.yview)

w1.config(xscrollcommand=scr_h1.set,yscrollcommand=scr_v1.set)
w1.pack(fill=BOTH,expand=YES)

# inserted to see if it's actually scrolling
w1.create_oval(5,5,50,50,fill='red')

labelText = StringVar() # StringVar() Allows you to enter Strings
labelText.set(" ".join(["a","c","d","a","c","d"]))
# label1= Label(w1, text="hhhoooooooooooooo",height=4)#Attribute want label to have
label1= Label(w1, textvariable=labelText, bg="red",fg="yellow",height=4)
label1.pack()
w1.create_window(100, 100, window=label1)
w1.create_text(100, 280, tex='Ham')
w1.create_text(100, 280, tex='YYYYYYYYY')

root.mainloop()


# canvas = Canvas(width=300, height=300, bg='white')
# canvas.pack(expand=YES, fill=BOTH)
#
# widget = Label(canvas, text='Spam', fg='white', bg='black')
# widget.pack()
# canvas.create_window(100, 100, window=widget)
# mainloop()