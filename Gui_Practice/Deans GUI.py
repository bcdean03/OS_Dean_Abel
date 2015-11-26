__author__ = 'Dean'
# from tkinter import *
# from PIL import Image, ImageTk
# import ttk
from tkinter import *

import tkinter as tk
from tkinter import *
# import tkinter
from PIL import Image, ImageTk



class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()


    def init_window(self):
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)
        #
        # menu = Menu(self.master)
        # self.master.config(menu=menu)
        #
        # file = Menu(menu)
        # file.add_command(label='Save')
        # file.add_command(label='Exit', command=self.client_exit)
        # menu.add_cascade(label="Edit", menu=file)
        #
        # edit = Menu(menu)
        # edit.add_command(label='Show Image', command=self.showImg)
        # edit.add_command(label='Show Text', command=self.showTxt)
        # menu.add_cascade(label='Edit', menu=edit)
        self.showImg()
        self.showTxt()


    def showImg(self):
        load = Image.open('onlinePicture.jpg')
        render = ImageTk.PhotoImage(load)

        img = Label(self, image=render, bg="red")
        img.image = render
        img.place(x=0, y=0)


    def showTxt(self):
        text = Label(self, text="Client_1", fg="red")
        text.place(x=600,  y=200)
        text.pack()


    def client_exit(self):
        exit()

root = Tk()
root.geometry("400x300")
# scrollbar.config(command=root.yview)
app = Window(root)
canvas = tkinter.Canvas(app)
canvas.pack()
canvas.mainloop()
#
# for i in range(10):
#     canvas.create_line(50 * i, 0, 50 * i, 400)
#     canvas.create_line(0, 50 * i, 400, 50 * i)
# canvas.create_rectangle(100, 100, 200, 200, fill="blue")
# canvas.create_line(50, 100, 250, 200, fill="red", width=10)

root.mainloop()
# from Tkinter import *
# import Image, ImageTk
#
# root = Tk()
#
# frame = Frame(root, bd=2, relief=SUNKEN)
#
# frame.grid_rowconfigure(0, weight=1)
# frame.grid_columnconfigure(0, weight=1)
#
# xscrollbar = Scrollbar(frame, orient=HORIZONTAL)
# xscrollbar.grid(row=1, column=0, sticky=E+W)
#
# yscrollbar = Scrollbar(frame)
# yscrollbar.grid(row=0, column=1, sticky=N+S)
#
# canvas = Canvas(frame, bd=0, xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set)
# canvas.grid(row=0, column=0, sticky=N+S+E+W)
#
# File = "onlinePicture.jpg"
# img = ImageTk.PhotoImage(Image.open(File))
# canvas.create_image(0,0,image=img, anchor="nw")
# canvas.config(scrollregion=canvas.bbox(ALL))
# xscrollbar.config(command=canvas.xview)
# yscrollbar.config(command=canvas.yview)
#
# frame.pack()
# root.mainloop()
# root = Tk()
# load = Image.open('onlinePicture.jpg')
# render = ImageTk.PhotoImage(load)
#
# img = Label(image=render, bg="red")
# img.image = render
# img.grid(row=0, column=0)
#
# img = Label(image=render, bg="red")
# img.image = render
# img.grid(row=0, column=1)
#
# img = Label(image=render, bg="red")
# img.image = render
# img.grid(row=1, column=0)
# root.mainloop()
# master =TK()
# Label(master, text="First").grid(row=0)
# Label(master, text="Second").grid(row=1)
#
# e1 = Entry(master)
# e2 = Entry(master)
#
# e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)
# class VerticalScrolledFrame(Frame):
#     """A pure Tkinter scrollable frame that actually works!
#     * Use the 'interior' attribute to place widgets inside the scrollable frame
#     * Construct and pack/place/grid normally
#     * This frame only allows vertical scrolling
#
#     """
#     def __init__(self, parent, *args, **kw):
#         Frame.__init__(self, parent, *args, **kw)
#
#         # create a canvas object and a vertical scrollbar for scrolling it
#         vscrollbar = Scrollbar(self, orient=VERTICAL)
#         vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
#         canvas = Canvas(self, bd=0, highlightthickness=0,
#                         yscrollcommand=vscrollbar.set)
#         canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
#         vscrollbar.config(command=canvas.yview)
#
#         # reset the view
#         canvas.xview_moveto(0)
#         canvas.yview_moveto(0)
#
#         # create a frame inside the canvas which will be scrolled with it
#         self.interior = interior = Frame(canvas)
#         interior_id = canvas.create_window(0, 0, window=interior,
#                                            anchor=NW)
#
#         # track changes to the canvas and frame width and sync them,
#         # also updating the scrollbar
#         def _configure_interior(event):
#             # update the scrollbars to match the size of the inner frame
#             size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
#             canvas.config(scrollregion="0 0 %s %s" % size)
#             if interior.winfo_reqwidth() != canvas.winfo_width():
#                 # update the canvas's width to fit the inner frame
#                 canvas.config(width=interior.winfo_reqwidth())
#         interior.bind('<Configure>', _configure_interior)
#
#         def _configure_canvas(event):
#             if interior.winfo_reqwidth() != canvas.winfo_width():
#                 # update the inner frame's width to fill the canvas
#                 canvas.itemconfigure(interior_id, width=canvas.winfo_width())
#         canvas.bind('<Configure>', _configure_canvas)
#
#
# if __name__ == "__main__":
#
#     class SampleApp(Tk):
#         def __init__(self, *args, **kwargs):
#             root = Tk.__init__(self, *args, **kwargs)
#
#
#             self.frame = VerticalScrolledFrame(root)
#             self.frame.pack()
#             self.label = Label(text="Shrink the window to activate the scrollbar.")
#             self.label.pack()
#             buttons = []
#             for i in range(10):
#                 buttons.append(Button(self.frame.interior, text="Button " + str(i)))
#                 buttons[-1].pack()
#
#     app = SampleApp()
#     app.mainloop()


# style = ttk.Style()
# style.configure("Red.TCheckbutton", foreground="red")
# root = Tk()
# S = Scrollbar(root)
# T = Text(root, height=4, width=50)
# S.pack(side=RIGHT, fill=Y)
# T.pack(side=LEFT, fill=Y)
# S.config(command=T.yview)
# T.config(yscrollcommand=S.set,style="Red.TCheckButton")
# quote = """HAMLET: To be, or not to be--that is the question:
# Whether 'tis nobler in the mind to suffer
# The slings and arrows of outrageous fortune
# Or to take arms against a sea of troubles
# And by opposing end them. To die, to sleep--
# No more--and by a sleep to say we end
# The heartache, and the thousand natural shocks
# That flesh is heir to. 'Tis a consummation
# Devoutly to be wished."""
# T.insert(END, quote)
# mainloop()
# master = Tk()
#
# scrollbar = Scrollbar(master)
# scrollbar.pack(side=RIGHT, fill=Y)
#
# listbox = Listbox(master, yscrollcommand=scrollbar.set)
# for i in range(1000):
#     listbox.insert(END, str(i))
# listbox.pack(side=LEFT, fill=BOTH)
#
# scrollbar.config(command=listbox.yview)
#
# mainloop()



# class Window(Frame):
#     def __init__(self, master = None):
#         Frame.__init__(self, master)
#         self.master = master
#         self.init_window()
#
#
#     def init_window(self):
#         self.master.title("GUI")
#         self.pack(fill=BOTH, expand=1)
#         #
#         # menu = Menu(self.master)
#         # self.master.config(menu=menu)
#         #
#         # file = Menu(menu)
#         # file.add_command(label='Save')
#         # file.add_command(label='Exit', command=self.client_exit)
#         # menu.add_cascade(label="Edit", menu=file)
#         #
#         # edit = Menu(menu)
#         # edit.add_command(label='Show Image', command=self.showImg)
#         # edit.add_command(label='Show Text', command=self.showTxt)
#         # menu.add_cascade(label='Edit', menu=edit)
#         self.showImg()
#         self.showTxt()
#
#
#     def showImg(self):
#         load = Image.open('onlinePicture.jpg')
#         render = ImageTk.PhotoImage(load)
#
#         img = Label(self, image=render, bg="red")
#         img.image = render
#         img.place(x=0, y=0)
#
#
#     def showTxt(self):
#         text = Label(self, text="Client_1", fg="red")
#         text.place(x=600,  y=200)
#         text.pack()
#
#
#     def client_exit(self):
#         exit()
#
# root = Tk()
# root.geometry("400x300")
# # scrollbar.config(command=root.yview)
# app = Window(root)
# root.mainloop()


#
# master = Tk()
#
# listbox = Listbox(master)
# listbox.pack()
#
# listbox.insert(END, "a list entry")
#
# for item in ["one", "two", "three", "four"]:
#     listbox.insert(END, item)
#
# mainloop()