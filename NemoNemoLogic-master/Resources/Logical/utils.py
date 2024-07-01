############
#Start here#
############
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import numpy as np

def np2pixmap(array):   
    q_img = QImage(array.astype(np.uint8), array.shape[0], array.shape[1],  QImage.Format_RGB888)
    return QPixmap.fromImage(q_img)
    
def calc_numbers(row):
    results = []
    temp = ""
    for c in row :
        temp += str(c)
    
    parsed_zero = temp.split("1")
    for subset in parsed_zero:
        if subset == "":
            continue
        results.append(len(subset))

    if len(results) == 0:
        return (0)
    else:
        return tuple(results)


def convert_to_nums(arr):
    #for rows
    row_tuples = []
    for row in arr:
        row_tuples.append(calc_numbers(list(row.astype(np.uint8))))

    #for colums
    col_tuples = []
    for col in np.transpose(arr):
        col_tuples.append(calc_numbers(list(col.astype(np.uint8))))

    return row_tuples, col_tuples
##########
#End here#
##########
        