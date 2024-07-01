############
#Start here#
############
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from Resources.Widgets.NemoHome import NemoHome
from Resources.Widgets.NemoDraw import NemoDraw
from Resources.Widgets.NemoSolve import NemoSolve


widget_size = {
    0 : QSize(240,300), #home widget
    1 : QSize(1300, 1080), #problem making widget
    2:  QSize(1980, 1080)
} 

class NemoApp(QStackedWidget):
    ChildComponents = []
    def __init__(self):
        super().__init__()
        
        self.home_widget = NemoHome(self) #0번 위젯
        self.draw_widget = NemoDraw(self) #1번 위젯
        self.solve_widget = NemoSolve(self)#2번위젯
   
        self.apply_childs()
        self.addWidget(self.home_widget)
        self.addWidget(self.draw_widget)
        self.addWidget(self.solve_widget)
        self.goto(0)
      
    def apply_childs(self):
        for comp in NemoApp.ChildComponents:
            comp.setParent(self)

    def goto(self, k):

        self.setCurrentIndex(k)
        self.resize(widget_size[k])
        self.move_center()
    
    def move_center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = NemoApp()
    myapp.show()
    sys.exit(app.exec())

##########
#End here#
##########