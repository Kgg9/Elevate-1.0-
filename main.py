import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber, QPushButton, QGridLayout, QVBoxLayout
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer
from PyQt5 import uic

class ElevateInterior(QMainWindow): 

    def __init__(self):
        super(ElevateInterior, self).__init__()
        uic.loadUi("ElevateInterior.ui", self)
        self.show()

def main():
    app = QApplication([])
    window = ElevateInterior()
    app.exec_()

if __name__ == '__main__':
    main()