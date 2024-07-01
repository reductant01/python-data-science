############
#Start here#
############
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class NemoToggleButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.state = 1
        self.change_style_sheet()

    def toggle_state(self):
        if self.state == 0 or self.state == 1:
            self.state = (self.state+1)%2
        else:
            self.state = 1
        self.change_style_sheet()

    def mousePressEvent(self, event):
        if event.button() == 1:
            self.toggle_state()
            
        elif event.button() == 2:  # 우클릭 확인
            self.state =0.5
            self.change_style_sheet()
           
        else:
            super().mousePressEvent(event)

    def change_style_sheet(self):
        if self.state == 1:
            self.setStyleSheet("""  background-color: white; border: 2px solid black;""")

        elif self.state == 0:
            self.setStyleSheet("""  background-color: black; border: 2px solid  black;""")
        
        else:
            self.setStyleSheet("background-color: gray; border: 2px solid black;")

##########
#End here#
##########