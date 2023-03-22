from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, QRect, QEventLoop
from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber, QPushButton, QGridLayout, QVBoxLayout
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QSound
from PyQt5 import uic
from ElevatorBackendLogic import elevator


class ElevateInterior(QMainWindow):

    def __init__(self):
        super(ElevateInterior, self).__init__()
        uic.loadUi("ElevateInterior.ui", self)
        self.show()
        self.signal = 0

        self.resetFloorStyle = "background-color: rgb(176, 174, 178); border-style: outset; border-width: 2px; border-radius: 16px; border-color: black;"
        self.clickedStyle = "background-color: orange; border-style: outset; border-width: 2px; border-radius: 16px; border-color: black;"
        self.clickedCall = "background-color: green; border-style: outset; border-width: 2px; border-radius: 16px; border-color: black; font: bold 14px;"
        self.clickedHelp = "background-color: red; border-style: outset; border-width: 2px; border-radius: 16px; border-color: black; font: bold 14px;"
        self.arrowStyle = "background-color: orange; font: 32pt;"
        self.resetArrowStyle = "background-color: rgb(0, 0, 0); font: 32pt;"

        self.elevator1 = elevator(10, 5)
        self.elevator1.setFloorQueue()

        self.floorButtons = [self.pressButton1,
        self.pressButton2,
        self.pressButton3,
        self.pressButton4,
        self.pressButton5,
        self.pressButton6,
        self.pressButton7,
        self.pressButton8,
        self.pressButton9,
        self.pressButton10]

        #connecting Button clicks
        for flrBtn in self.floorButtons:
            flrBtn.clicked.connect(self.floorButtonClicked)

        self.serviceButtons = [self.holdOpen,
        self.holdClose.clicked,
        self.pressCallButton,
        self.pressHelpButton,]

        self.displayFloor.display(1)

    def floorButtonClicked(self):
        btn = self.sender()

        btn.setStyleSheet(self.clickedStyle)
        self.elevator1.toggleOn(int(btn.text()) - 1)
        self.displayFloor.setDigitCount(2)

        while (self.signal != 1 and 1 in self.elevator1.floorQueue):
            self.move_elevator()

        if 1 not in self.elevator1.floorQueue:
            self.upArrow.setStyleSheet(self.resetArrowStyle)
            self.downArrow.setStyleSheet(self.resetArrowStyle)


    def serviceButtonClicked(self):
        button = self.sender()


    def move_elevator(self):
        self.elevator1.setDirection()
        self.signal = 1

        if self.elevator1.direction == "Up" and self.elevator1.currentFloor != self.elevator1.nextFloor:
            self.downArrow.setStyleSheet(self.resetArrowStyle)
            self.upArrow.setStyleSheet(self.arrowStyle)

            self.elevator1.getNextFloor()
            print(f"The next floor for {self.elevator1.currentFloor + 1} is {self.elevator1.nextFloor + 1}")
            self.elevator1.currentFloor += 1

            loop = QEventLoop()
            QTimer.singleShot(self.elevator1.elevatorMoveTime * 1000, loop.quit)
            loop.exec_()

            self.displayFloor.display(self.elevator1.currentFloor + 1)
            print(self.elevator1.floorQueue)
            self.move_elevator()

        elif self.elevator1.direction == "Down" and self.elevator1.currentFloor != self.elevator1.nextFloor:
            self.upArrow.setStyleSheet(self.resetArrowStyle)
            self.downArrow.setStyleSheet(self.arrowStyle)

            self.elevator1.getNextFloor()
            print(f"The next floor for {self.elevator1.currentFloor + 1} is {self.elevator1.nextFloor + 1}")
            self.elevator1.currentFloor -= 1

            loop = QEventLoop()
            QTimer.singleShot(self.elevator1.elevatorMoveTime * 1000, loop.quit)
            loop.exec_()

            self.displayFloor.display(self.elevator1.currentFloor + 1)
            print(self.elevator1.floorQueue)
            self.move_elevator()

        elif self.elevator1.currentFloor == self.elevator1.nextFloor:
            self.signal = 0
            self.elevator1.reachedFloor()

            print("Reached Floor Bitches \n")
            print(self.elevator1.currentFloor + 1)

            self.floorButtons[self.elevator1.currentFloor].setStyleSheet(self.resetFloorStyle)


        # def elevatorDoorMovement():


def main():
    app = QApplication([])
    window = ElevateInterior()
    app.exec_()


if __name__ == '__main__':
    main()
