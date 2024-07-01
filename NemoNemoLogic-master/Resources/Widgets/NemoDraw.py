############
#Start here#
############
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from functools import partial

from Resources.Components.NemoCanvas import NemoCanvas


#widget #1
class NemoDraw(QWidget):
    ChildComponents = []

    def __init__(self, app):
        super().__init__()
        self.app = app
        self.statusBar = QStatusBar()
        self.canvas_window = NemoCanvas(self.statusBar)

        self.upload_button = QPushButton("이미지 업로드하기")
        self.save_button = QPushButton("문제 저장하기")
        self.apply_button = QPushButton("도트로 변환")
        self.back_button = QPushButton("뒤로가기")

        self.size_8_button = QPushButton("8 * 8")
        self.size_16_button = QPushButton("16 * 16")
        self.size_32_button = QPushButton("32 * 32")

        NemoDraw.ChildComponents.append(self.canvas_window)
        NemoDraw.ChildComponents.append(self.statusBar)
        NemoDraw.ChildComponents.append(self.upload_button)
        NemoDraw.ChildComponents.append(self.save_button)
        NemoDraw.ChildComponents.append(self.apply_button)
        NemoDraw.ChildComponents.append(self.back_button)
        NemoDraw.ChildComponents.append(self.size_8_button)
        NemoDraw.ChildComponents.append(self.size_16_button)
        NemoDraw.ChildComponents.append(self.size_32_button)
        
        self.apply_childs()
        self.set_individual_componets()
        self.apply_style_sheet()
        self.set_button_event()
    

    def apply_childs(self):
        for comp in NemoDraw.ChildComponents:
            comp.setParent(self)

    def set_individual_componets(self):
        self.setGeometry(0, 0, 1980, 1080)
        self.canvas_window.setGeometry(10,10,1024,1024)

        self.upload_button.setGeometry(1044, 984, 200, 50)
        self.save_button.setGeometry(1044,914, 200, 50)
        self.apply_button.setGeometry(1044, 844, 200, 50)
        self.back_button.setGeometry(1044, 774, 200,50)
        self.size_8_button.setGeometry(1044, 704,60, 50 )
        self.size_16_button.setGeometry(1114, 704, 60, 50)
        self.size_32_button.setGeometry(1184, 704, 60, 50)

        statusbar_height = 30
        self.statusBar.setGeometry(0, 1080-statusbar_height, 1980, statusbar_height)
        
        self.canvas_window.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.canvas_window.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def apply_style_sheet(self):
      
        self.canvas_window.setStyleSheet('''
                                  QGraphicsView {
                                        border-style: solid;
                                        border-width: 2px;
                                        border-color: black;
                                  }
                                  ''')
        self.upload_button.setStyleSheet("background-color:#CCCCFF;")
        self.save_button.setStyleSheet("background-color:#CCCCFF;")
        self.apply_button.setStyleSheet("background-color:#CCCCFF;")
        self.back_button.setStyleSheet("background-color:#CCCCFF;")
        self.size_8_button.setStyleSheet("background-color:#CCCCFF;")
        self.size_16_button.setStyleSheet("background-color:#CCCCFF;")
        self.size_32_button.setStyleSheet("background-color:#CCCCFF;")
        self.statusBar.setStyleSheet("background-color:#CCCCFF;")
        
    def set_button_event(self):
        self.upload_button.clicked.connect(self.canvas_window.set_canvas)
        self.save_button.clicked.connect(self.canvas_window.save_problem)
        self.apply_button.clicked.connect(self.canvas_window.apply)
        self.back_button.clicked.connect(partial(self.app.goto, 0))

        self.size_8_button.clicked.connect(partial(self.canvas_window.set_problem_size, 8))
        self.size_16_button.clicked.connect(partial(self.canvas_window.set_problem_size, 16))
        self.size_32_button.clicked.connect(partial(self.canvas_window.set_problem_size, 32))
        
##########
#End here#
##########






