############
#Start here#
############
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class NemoWelcom(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 500, 500)
        self.label = QLabel()
        self.label.setParent(self)
        self.label.setGeometry(0,0,500,500)
        self.label.setPixmap(QPixmap("./Resources/Images/thumb_dochi.png").scaled(QSize(500,500)))

        self.ok_button = QPushButton("ok")
        self.ok_button.setParent(self)
        self.ok_button.setGeometry(150, 400, 200, 50)
        self.ok_button.clicked.connect(self.hide)

        self.setFixedSize(self.size())
    
    def show_welcome_widget(self):        
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

##########
#End here#
##########


