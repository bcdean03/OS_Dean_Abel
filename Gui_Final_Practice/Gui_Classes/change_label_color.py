__author__ = 'abelamadou'
from Tkinter import *

class DisplayClient:
    def __init__(self,canvas,oval,clientName,food,ingredient):
        self.canvas=canvas
        self.oval=oval
        self.clientName=clientName
        self.food=food
        self.ingredient=ingredient
    def change_label_color(self,l_obj,color):
        l_obj.config(bg=color)

    def change_oval(self,color):
        self.canvas.itemconfig(self.oval,fill=color)
