__author__ = 'Dean Bailey abelamadou'
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

    def change_label_color(self,l_obj,color):
        '''
        Change the label color in the object to update the GUI
        :param l_obj:
        :param color:
        :return:
        '''
        l_obj.config(bg=color)

    def change_label_name(self,l_obj,name):
        '''
        Change the label color in the object to update the GUI
        :param l_obj:
        :param name:
        :return:
        '''
        l_obj.config(text=name)


    def change_oval(self,color):
        '''
        Change the label color in the object to update the GUI
        :param color:
        :return:
        '''
        self.canvas.itemconfig(self.oval,fill=color)
