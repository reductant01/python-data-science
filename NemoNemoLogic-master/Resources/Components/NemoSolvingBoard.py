############
#Start here#
############
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import numpy as np

from Resources.Components.NemoToggleButton import NemoToggleButton
    
    

class SolvingBoard(QLabel):
    def __init__(self, problem_size):
        super().__init__()
        self.problem_size = problem_size
      
        if self.problem_size == 8:
            self.button_size =100
        elif self.problem_size == 16:
            self.button_size = 50
        else:
            self.button_size = 25
        
        self.button_dict = {}
        self.button_distance = 3

        

        for i in range(self.problem_size):
            for j in range(self.problem_size):
                self.button_dict[f"{i}_{j}"] = NemoToggleButton()

        self.apply_childs()
        self.set_individual_components()
        self.set_style_sheet()
    
    def apply_childs(self):
        for comp in self.button_dict.values():
            comp.setParent(self)

    def set_individual_components(self):
        x_start = 20
        y_start = 20
        for i in range(self.problem_size):
            for j in range(self.problem_size):
                x_pos = x_start + i* (self.button_size+self.button_distance)
                y_pos = y_start + j* (self.button_size+self.button_distance)
                self.button_dict[f"{j}_{i}"].setGeometry(x_pos, y_pos, self.button_size,self.button_size)
        label_start = 30
        label_size = self.button_size*self.problem_size + self.button_distance*(self.problem_size-1) +40
        self.setGeometry(label_start, label_start, label_size, label_size)
   
        

    def set_style_sheet(self):
        self.setStyleSheet("background-color: white; border: 2px solid black")

    def get_user_answer(self):
        user_answer = np.zeros((self.problem_size, self.problem_size))
        for i in range(self.problem_size):
            for j in range(self.problem_size):
                user_answer[i][j] = self.button_dict[f"{i}_{j}"].state

        return user_answer
    
##########
#End here#
##########