__author__ = 'abelamadou'
from tkinter import *

root = Tk()

frame2 = Frame(root)
frame2.pack(side=RIGHT)

w1 = Canvas(frame2, width=600, height=300,background="green", scrollregion=(0,0,3000,3000))


scr_h1 = Scrollbar(frame2,orient=HORIZONTAL)
scr_h1.pack(side=BOTTOM,fill=X)
scr_h1.config(command=w1.xview)

scr_v1 = Scrollbar(frame2,orient=VERTICAL)
scr_v1.pack(side=RIGHT,fill=Y)
scr_v1.config(command=w1.yview)

w1.config(xscrollcommand=scr_h1.set,yscrollcommand=scr_v1.set)
w1.pack(fill=BOTH,expand=True)

# inserted to see if it's actually scrolling
w1.create_oval(0,0,50,50,fill='red')


root.mainloop()