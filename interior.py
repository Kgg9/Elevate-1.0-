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

    def initUI(self):
        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle('Elevator Control Panel')
 
        self.displayFloor = QLCDNumber(self)
        self.displayFloor.setDigitCount(2)
        self.displayFloor.display(1)

        self.displayArrow = QLCDNumber(self)
        self.displayArrow.setSegmentStyle(QLCDNumber.Flat)
        self.displayArrow.display("↑")

        grid = QGridLayout()
        grid.addWidget(self.displayFloor, 0, 0, 1, 2)
        grid.addWidget(self.displayArrow, 1, 1)

        floor_buttons = QVBoxLayout()
        for i in range(1, 11):
            button = QPushButton(str(i), self)
            button.clicked.connect(self.button_clicked)
            floor_buttons.addWidget(button)

        grid.addLayout(floor_buttons, 2, 0, 1, 2)

        self.setLayout(grid)

        self.show()

    def button_clicked(self):
        button = self.sender()
        floor = int(button.text())

        current_floor = int(self.displayFloor.value())

        if floor > current_floor:
            direction = "↑"
            step = 1
        elif floor < current_floor:
            direction = "↓"
            step = -1
        else:
            return

        self.timer = QTimer()
        self.timer.timeout.connect(lambda: self.update_floor(floor, step, direction))
        self.timer.start(500)
    def update_floor(self, target_floor, step, direction):
        current_floor = int(self.displayFloor.value())
        if current_floor == target_floor:
            self.timer.stop()
            self.displayArrow.display(" ")
            return

        self.displayArrow.display(direction)
        self.displayFloor.display(current_floor + step)

if __name__ == '__main__':
    main()