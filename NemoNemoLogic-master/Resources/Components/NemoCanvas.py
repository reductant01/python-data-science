############
#Start here#
############
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import numpy as np
import cv2, gzip, pickle
from PIL import Image

from Resources.Logical.utils import *
from Resources.Logical.Problem import Problem


class NemoCanvas(QGraphicsView):
    def __init__(self, form_statusbar):
        super().__init__()
        self.form_statusbar = form_statusbar
        self.canvas = np.ones((1024,1024,3))*255
        self.click_status = False
        self.thickness= 10
        self.pen_mode = 1
        self.pen_color = (0, 0, 0)
        self.problem_size = 16
        self.canvas_scene = QGraphicsScene()
        
        self.setScene(self.canvas_scene)
        self.update_scene()


    def update_scene(self):
        self.canvas_scene.clear()
        self.canvas_scene.addPixmap(np2pixmap(self.canvas))


    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.click_status = True
        return super().mousePressEvent(event)
    

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        self.click_status = False
        return super().mouseMoveEvent(event)
    

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if self.click_status:
            x = event.pos().x()
            y = event.pos().y()
            cv2.circle(self.canvas, (x, y) ,self.thickness, self.pen_color, -1, cv2.LINE_AA)
            self.update_scene()
        return super().mouseMoveEvent(event)
    

    def wheelEvent(self, event: QWheelEvent) -> None:
        self.thickness+= int(event.angleDelta().y()/10)
        if self.thickness< 0:
            self.thickness = 10
        if self.thickness> 75:
            self.thickness = 75
        self.display_state()
        return super().wheelEvent(event)
    
    def keyPressEvent(self, event: QKeyEvent) -> None:
        #change pen color between black and white 
        if event.key() == Qt.Key_C:
            if self.pen_mode:
                self.pen_color = (255,255,255)
            else:
                self.pen_color = (0, 0, 0)
            self.pen_mode = (self.pen_mode+1)%2
            self.display_state()
        
        if event.key() == Qt.Key_X:
            self.canvas = np.ones((1024,1024,3))*255
            self.update_scene()
        return super().keyPressEvent(event)
    

    def set_canvas(self):
        img_path = QFileDialog.getOpenFileName()[0]
        img = np.array(Image.open(img_path).resize((1024,1024)))
        self.canvas = img
        self.update_scene()

    def save_problem(self):
        try:
            temp_problem = Problem(self.canvas, self.problem_size)
            save_path = QFileDialog.getSaveFileName()[0]
            with gzip.open(save_path, "wb") as f:
                pickle.dump(temp_problem, f,  pickle.HIGHEST_PROTOCOL)
            f.close()
            self.form_statusbar.showMessage("문제저장 성공")
        except:
            self.form_statusbar.showMessage("문제저장 실패")
            pass

    def apply(self):
        self.canvas = Problem(self.canvas, self.problem_size).preview
        self.form_statusbar.showMessage("도트로 변환했습니다.")
        self.update_scene()
        
    def set_problem_size(self, n):
        self.problem_size = n
        self.display_state()

    def display_state(self):
        mode = "Draw" if self.pen_mode == 1 else "Erase"
        self.form_statusbar.showMessage(f"Thickness: {self.thickness} Mode: {mode} Problem_size: {self.problem_size}")

##########
#End here#
##########