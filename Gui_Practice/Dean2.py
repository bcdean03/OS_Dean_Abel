from Tkinter import *
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
root.mainloop()
