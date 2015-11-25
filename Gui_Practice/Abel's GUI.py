__author__ = 'Abel'
# from tkinter import *
# import tkinter.messagebox  #Allow to pop message box
#
# app = Tk()#basic interface
# app.title("GUIII")
# app.geometry('450x300+200+200')#How big you want the application to be displayed on the screen
#
# #Make a label
# labelText = StringVar() # StringVar() Allows you to enter Strings
# # labelText.set(" ".join(["a","c","d"]))
# labelText.set("Click here noob")
# # label1= Label(app, textvariable=labelText,height=4)#Attribute want label to have
# label1= Label(app, textvariable=labelText, bg="red",fg="yellow",height=4)#Attribute want label to have
# label1.pack(fill=X)#important to pack
# # label1.pack()#important to pack
#
# #Making a checkbox
# checkBoxVal = IntVar()# IntVar() Allows you to enter Integers
# checkBox1 = Checkbutton(app,variable=checkBoxVal,text="Happy?")
# checkBox1.pack()
#
# custName = StringVar(None)#Accept information from customer
# # custName.set("Howdy")
# yourName= Entry(app, textvariable=custName)
# yourName.pack()
#
# def beenClicked():
#     radioValue =relStatus.get()
#     tkinter.messagebox.showinfo("You cliked",radioValue)
#     return
# #Radio button
# relStatus = StringVar()
# relStatus.set(None)#Set them by default to None
# radio1=Radiobutton(app,text="Single", value="Single",variable=relStatus,command=beenClicked).pack()#make it so only can select one of them at a time, thus why going to have same name
# radio1=Radiobutton(app,text="Married", value="Married",variable=relStatus,command=beenClicked).pack()#make it so only can select one of them at a time, thus why going to have same name
#
# #Make buttons
# def changeLabel():
#     name ="Thanks for the click"+ yourName.get()
#     labelText.set(name)
#     yourName.delete(0,END)
#     yourName.insert(0,"My name is Abel")
#     return
# button1 = Button(app, text="Click Here",width=20,command=changeLabel)
# button1.pack(side='bottom',padx=15,pady=15)#Can do bottom,top etc...
#
#
# app.mainloop()
#



# http://www.tutorialspoint.com/python/tk_scrollbar.htm
# from Tkinter import *
#
# root = Tk()
# scrollbar = Scrollbar(root)
# scrollbar.pack( side = RIGHT, fill=Y )
#
# mylist = Listbox(root, yscrollcommand = scrollbar.set )
# for line in range(100):
#    mylist.insert(END, "This is line number " + str(line))
#
# mylist.pack( side = LEFT, fill = BOTH )
# scrollbar.config( command = mylist.yview )
#
# mainloop()

#Frame-> http://www.tutorialspoint.com/python/tk_frame.htm
#Canvas-> http://www.tutorialspoint.com/python/tk_canvas.htm

# from tkinter import *
#
# root = Tk()
#
# frame2 = Frame(root)
# frame2.pack(side=RIGHT)
#
# w1 = Canvas(frame2, width=600, height=300,background="green", scrollregion=(0,0,3000,3000))
#
#
# scr_h1 = Scrollbar(frame2,orient=HORIZONTAL)
# scr_h1.pack(side=BOTTOM,fill=X)
# scr_h1.config(command=w1.xview)
#
# scr_v1 = Scrollbar(frame2,orient=VERTICAL)
# scr_v1.pack(side=RIGHT,fill=Y)
# scr_v1.config(command=w1.yview)
#
# w1.config(xscrollcommand=scr_h1.set,yscrollcommand=scr_v1.set)
# w1.pack(fill=BOTH,expand=True)
#
# # inserted to see if it's actually scrolling
# w1.create_oval(0,0,50,50,fill='red')
#
#
# root.mainloop()


#Canvas
# from Tkinter import*
# import tkMessageBox
# # import Image
#
# top = Tk()
#
# C = Canvas(top, bg="blue", height=250, width=300)
# # filename = PhotoImage(file = "cat.jpg")
# # image = C.create_image(50, 50, anchor=NE, image=filename)
# coord = 10, 50, 240, 210
# arc = C.create_arc(coord, start=0, extent=150, fill="red")
#
# C.pack()
# top.mainloop()
#

#Frame
# from Tkinter import *
#
# root = Tk()
# frame = Frame(root)
# frame.pack()
#
# bottomframe = Frame(root)
# bottomframe.pack( side = BOTTOM )
#
# redbutton = Button(frame, text="Red", fg="red")
# redbutton.pack( side = LEFT)
#
# greenbutton = Button(frame, text="Brown", fg="brown")
# greenbutton.pack( side = LEFT )
#
# bluebutton = Button(frame, text="Blue", fg="blue")
# bluebutton.pack( side = LEFT )
#
# blackbutton = Button(bottomframe, text="Black", fg="black")
# blackbutton.pack( side = BOTTOM)
#
# root.mainloop()