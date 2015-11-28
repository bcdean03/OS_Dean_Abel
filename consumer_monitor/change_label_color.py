__author__ = 'abelamadou'
from Tkinter import *

class DisplayClient:
    '''
    This class configures objects to update the Abean GUI
    '''
    def __init__(self,canvas,oval,clientName,food,ingredient):
        self.canvas=canvas
        self.oval=oval
        self.clientName=clientName
        self.food=food
        self.ingredient=ingredient

    # Change the label color in the object to update the GUI
    def change_label_color(self,l_obj,color):
        l_obj.config(bg=color)

    # Change the label color in the object to update the GUI
    def change_label_name(self,l_obj,name):
        l_obj.config(text=name)

    # Change the label color in the object to update the GUI
    def change_oval(self,color):
        self.canvas.itemconfig(self.oval,fill=color)
