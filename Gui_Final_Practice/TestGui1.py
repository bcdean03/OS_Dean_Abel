# __author__ = 'abelamadou'
from threading import Thread
from Tkinter import *
from time import sleep


def welcome_screen():
    pass


def cooking_screen():
   # frame2 = Frame(root)
   #      frame2.pack(side=RIGHT)
   #
   #      w1 = Canvas(frame2, width=600, height=300,background="white", scrollregion=(0,0,3000,3000))
   #
   #
   #      scr_h1 = Scrollbar(frame2,orient=HORIZONTAL)
   #      scr_h1.pack(side=BOTTOM,fill=X)
   #      scr_h1.config(command=w1.xview)
   #
   #      scr_v1 = Scrollbar(frame2,orient=VERTICAL)
   #      scr_v1.pack(side=RIGHT,fill=Y)
   #      scr_v1.config(command=w1.yview)
   #
   #      w1.config(xscrollcommand=scr_h1.set,yscrollcommand=scr_v1.set)
   #      w1.pack(fill=BOTH,expand=True)
   #
   #  # inserted to see if it's actually scrolling
   #  w1.create_oval(0,0,50,50,fill='red')
   pass

class AbeanGui(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.root = Tk()
        self.root.title("Abean Groceries")
        self.root.geometry('450x300+200+200')
    def callback(self):
        sleep(3)
        self.root.quit()
    def run(self):
        # welcome_screen()
        # cooking_screen()
        self.root.protocol("WM_DELETE_WINDOW", self.callback)
        self.root.mainloop()


if __name__ == '__main__':
    AbeanGui().start()

# import tkinter as tk
# import threading
#
# class App(threading.Thread):
#
#     def __init__(self):
#         threading.Thread.__init__(self)
#         self.start()
#
#     def callback(self):
#         self.root.quit()
#
#     def run(self):
#         self.root = tk.Tk()
#         self.root.protocol("WM_DELETE_WINDOW", self.callback)
#
#         label = tk.Label(self.root, text="Hello World")
#         label.pack()
#
#         self.root.mainloop()
#
#
# app = App()
# print('Now we can continue running code while mainloop runs!')
#
# for i in range(100000):
#     print(i)