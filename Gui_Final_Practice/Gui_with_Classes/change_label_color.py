__author__ = 'abelamadou'
from Tkinter import *
class DisplayClient:
    def __init__(self,dot,clientName,food,ingredient):
        self.dot=dot
        self.clientName=clientName
        self.food=food
        self.ingredient=ingredient
        pass
    def change_label_color(self,l_obj,color):
        l_obj.config(bg=color)
