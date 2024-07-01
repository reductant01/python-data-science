############
#Start here#
############
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import gzip
import pickle
import os.path as osp
from functools import partial

from Resources.Components.NemoWelcome import NemoWelcom
from Resources.Components.NemoSolvingBoard import SolvingBoard
from Resources.Logical.utils import convert_to_nums

#widget #2
class NemoSolve(QWidget):
    ChildComponents = []
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.load_problem_button = QPushButton("문제 불러오기")
        self.is_correct_button = QPushButton("정답 확인하기")
        self.back_button = QPushButton("뒤로가기")
        self.statusbar = QStatusBar()
        self.row_hint_table = QPlainTextEdit()
        self.col_hint_table = QPlainTextEdit()
        self.welcome_window = NemoWelcom()

        self.problem = None
        self.solving_board = None

        NemoSolve.ChildComponents.append(self.load_problem_button)
        NemoSolve.ChildComponents.append(self.is_correct_button)
        NemoSolve.ChildComponents.append(self.back_button)
        NemoSolve.ChildComponents.append(self.statusbar)
        NemoSolve.ChildComponents.append(self.row_hint_table)
        NemoSolve.ChildComponents.append(self.col_hint_table)

        self.apply_childs()
        self.set_individual_componets()
        self.apply_style_sheet()
        self.set_button_event()
    
    def apply_childs(self):
        for comp in NemoSolve.ChildComponents:
            comp.setParent(self)

    def set_individual_componets(self):
        self.setGeometry(0, 0, 1980, 1080)
        self.load_problem_button.setGeometry(1760, 20, 200, 50)
        self.is_correct_button.setGeometry(1760, 80, 200, 50)
        self.back_button.setGeometry(1760, 140, 200, 50)
        statusbar_height = 30
        self.statusbar.setGeometry(0, 1080-statusbar_height, 1980, statusbar_height)

        self.row_hint_table.setGeometry(1120,100, 300,800)
        self.col_hint_table.setGeometry(1440,100, 300,800)
  
    def apply_style_sheet(self):
        self.statusbar.setStyleSheet("background-color:#CCCCFF;")
        self.load_problem_button.setStyleSheet("background-color:#CCCCFF;")
        self.is_correct_button.setStyleSheet("background-color:#CCCCFF;")
        self.back_button.setStyleSheet("background-color:#CCCCFF;")

    def set_button_event(self):
        self.load_problem_button.clicked.connect(self.load_problem)
        self.is_correct_button.clicked.connect(self.compare_with_users)
        self.back_button.clicked.connect(partial(self.app.goto, 0))

    def load_problem(self):
        load_path = QFileDialog.getOpenFileName()[0]
        problem_name = osp.splitext(osp.basename(load_path))[0]
        try:
            with gzip.open(load_path, 'rb') as f:
                self.problem = pickle.load(f)
            f.close()

            if self.solving_board != None:
                
                self.solving_board.setParent(None)

            self.solving_board = SolvingBoard(self.problem.size)
            self.solving_board.setParent(self)
            self.solving_board.show()
            
            row_hint, col_hint = convert_to_nums(self.problem.ans_arr)
            self.update_hint_table(self.row_hint_table, row_hint, "row")
            self.update_hint_table(self.col_hint_table, col_hint, "col")
            text = f"now solving '{problem_name}'"
            self.display_state(text)

        except:
            text = f"failed to load problem '{problem_name}'"
            self.display_state(text)
            return
    
    def display_state(self, text):
        self.statusbar.showMessage(f"{text}")

    def update_hint_table(self, table:QPlainTextEdit, hints:list[tuple], kind)->None:
        table.clear()
        if len(hints):
            for idx, hint in enumerate(hints):
                table.appendPlainText(f"{kind} {idx+1}=> {hint} ")

    def compare_with_users(self):
        if self.problem is not None:
            user_answer = self.solving_board.get_user_answer()

            if False not in (user_answer == self.problem.ans_arr):
                self.welcome_window.center()
                self.welcome_window.show()
            else:   
                self.display_state("땡! 틀렸습니다.")
                
        else:
            text = "문제를 먼저 로드해 주세요."
            self.display_state(text)

##########
#End here#
##########