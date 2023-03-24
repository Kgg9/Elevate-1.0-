import math
import sys, os
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, QRect, QEventLoop
from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber, QPushButton, QGridLayout, QVBoxLayout
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5 import uic
from ElevatorBackendLogic import elevator
from PyQt5 import QtCore
from time import sleep


class ElevateInterior(QMainWindow):

    def __init__(self):
        super(ElevateInterior, self).__init__()
        uic.loadUi("ElevateInterior.ui", self)
        self.show()
        self.signal = 0
        self.CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
        self.soundPlayer = QMediaPlayer()


        self.resetFloorStyle = "background-color: rgb(176, 174, 178); border-style: outset; border-width: 2px; border-radius: 16px; border-color: black;"
        self.clickedStyle = "background-color: orange; border-style: outset; border-width: 2px; border-radius: 16px; border-color: black;"
        self.clickedCall = "background-color: green; border-style: outset; border-width: 2px; border-radius: 16px; border-color: black; font: bold 14px;"
        self.clickedHelp = "background-color: red; border-style: outset; border-width: 2px; border-radius: 16px; border-color: black; font: bold 14px;"
        self.arrowStyle = "background-color: orange; font: 32pt;"
        self.resetArrowStyle = "background-color: rgb(0, 0, 0); font: 32pt;"

        self.pushExit.clicked.connect(self.exitElevator)

        self.elevator1 = elevator(10, 2)
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


        self.closeIntDoors()

        #connecting Button clicks
        for flrBtn in self.floorButtons:
            flrBtn.clicked.connect(self.floorButtonClicked)

        exterior.exteriorElevatorBtn.clicked.connect(self.exteriorFloorButtonClicked)

        self.serviceButtons = [self.holdOpen, self.holdClose.clicked]

        self.pressCallButton.clicked.connect(self.callIsPressed)
        self.pressHelpButton.clicked.connect(self.helpIsPressed)

        self.displayFloor.display(1)

    def floorButtonClicked(self):
        btn = self.sender()

        btn.setStyleSheet(self.clickedStyle)
        self.elevator1.toggleOn(int(btn.text()) - 1)
        self.displayFloor.setDigitCount(2)

        while (self.signal != 1 and 1 in self.elevator1.floorQueue):
            self.move_elevator()

        if 1 not in self.elevator1.floorQueue:
            self.intUpArrow.setStyleSheet(self.resetArrowStyle)
            self.intDownArrow.setStyleSheet(self.resetArrowStyle)

    def exteriorFloorButtonClicked(self):
        btn = exterior.sender()

        btn.setStyleSheet(self.clickedStyle)
        # print(exterior.lcdFloorDisplay.value())
        # self.elevator1.toggleOn(int(exterior.lcdFloorDisplay.value()) - 1)

    def playAudioInterior(self, sound):
        url = QUrl.fromLocalFile(os.path.join(self.CURRENT_DIR, sound))
        content = QMediaContent(url)
        self.soundPlayer.setMedia(content)
        self.soundPlayer.play()

    def callIsPressed(self):
        self.pressCallButton.setStyleSheet(self.clickedCall)
        self.playAudioInterior("callSound.mp3")
        self.pressCallButton.clicked.connect(self.callIsPressedAgain)

    def callIsPressedAgain(self):
        self.soundPlayer.stop()
        self.pressCallButton.setStyleSheet(self.resetFloorStyle)
        self.pressCallButton.clicked.connect(self.callIsPressed)

    def helpIsPressed(self):
        self.pressHelpButton.setStyleSheet(self.clickedHelp)
        self.playAudioInterior("alarmSound.mp3")
        self.pressHelpButton.clicked.connect(self.helpIsPressedAgain)

    def helpIsPressedAgain(self):
        self.pressHelpButton.setStyleSheet(self.resetFloorStyle)
        self.soundPlayer.stop()
        self.pressHelpButton.clicked.connect(self.helpIsPressed)


    def move_elevator(self):
        self.elevator1.setDirection()
        self.signal = 1

        if self.elevator1.direction == "Up" and self.elevator1.currentFloor != self.elevator1.nextFloor:
            self.intDownArrow.setStyleSheet(self.resetArrowStyle)
            self.intUpArrow.setStyleSheet(self.arrowStyle)

            exterior.extDownArrow.setStyleSheet(self.resetArrowStyle)
            exterior.extUpArrow.setStyleSheet(self.arrowStyle)

            self.elevator1.getNextFloor()
            self.elevator1.currentFloor += 1

            loop = QEventLoop()
            QTimer.singleShot(self.elevator1.elevatorMoveTime * 1000, loop.quit)
            loop.exec_()

            self.displayFloor.display(self.elevator1.currentFloor + 1)
            exterior.lcdFloorDisplay.display(self.elevator1.currentFloor + 1)
            self.move_elevator()

        elif self.elevator1.direction == "Down" and self.elevator1.currentFloor != self.elevator1.nextFloor:
            self.intUpArrow.setStyleSheet(self.resetArrowStyle)
            self.intDownArrow.setStyleSheet(self.arrowStyle)

            exterior.extUpArrow.setStyleSheet(self.resetArrowStyle)
            exterior.extDownArrow.setStyleSheet(self.arrowStyle)

            self.elevator1.getNextFloor()
            self.elevator1.currentFloor -= 1

            loop = QEventLoop()
            QTimer.singleShot(self.elevator1.elevatorMoveTime * 1000, loop.quit)
            loop.exec_()

            self.displayFloor.display(self.elevator1.currentFloor + 1)
            exterior.lcdFloorDisplay.display(self.elevator1.currentFloor + 1)
            self.move_elevator()

        elif self.elevator1.currentFloor == self.elevator1.nextFloor:
            self.signal = 0
            self.elevator1.reachedFloor()

            self.floorButtons[self.elevator1.currentFloor].setStyleSheet(self.resetFloorStyle)
            exterior.exteriorElevatorBtn.setStyleSheet(self.resetFloorStyle)
            self.openIntDoors()

            self.playAudioInterior("reachingFloors.mp3")

            loop = QEventLoop()
            QTimer.singleShot(5 * 1000, loop.quit)
            loop.exec_()

            self.closeIntDoors()


    def openIntDoors(self):

        self.intLefta = QPropertyAnimation(self.intLeft, b"geometry")
        self.intLefta.setDuration(1000)
        self.intLefta.setStartValue(QRect(90, 10, 211, 691))
        self.intLefta.setEndValue(QRect(90, 10, 41, 691))
        self.intLefta.setEasingCurve(QEasingCurve.InOutCubic)

        self.intRighta = QPropertyAnimation(self.intRight, b"geometry")
        self.intRighta.setDuration(1000)
        self.intRighta.setStartValue(QRect(300, 10, 201, 691))
        self.intRighta.setEndValue(QRect(460, 10, 41, 691))
        self.intRighta.setEasingCurve(QEasingCurve.InOutCubic)

        self.intLefta.start()
        self.intRighta.start()
    
        
    def closeIntDoors(self):
        self.intLefta = QPropertyAnimation(self.intLeft, b"geometry")
        self.intLefta.setDuration(1000)
        self.intLefta.setStartValue(QRect(90, 10, 41, 691))
        self.intLefta.setEndValue(QRect(90, 10, 211, 691))
        self.intLefta.setEasingCurve(QEasingCurve.InOutCubic)

        self.intRighta = QPropertyAnimation(self.intRight, b"geometry")
        self.intRighta.setDuration(1000)
        self.intRighta.setStartValue(QRect(460, 10, 41, 691))
        self.intRighta.setEndValue(QRect(300, 10, 201, 691))
        self.intRighta.setEasingCurve(QEasingCurve.InOutCubic)

        self.intLefta.start()
        self.intRighta.start()

    def exitElevator(self):
        self.soundPlayer.setMuted(True)
        widget.setCurrentIndex(1)


class ElevateExterior(QMainWindow):

    def __init__(self):
        super(ElevateExterior, self).__init__()
        uic.loadUi("ElevateExterior.ui", self)
        self.show()
        self.displaySignal = QtCore.pyqtSignal(str)


        self.pushEnter.clicked.connect(self.enterElevator)

        self.extClose.clicked.connect(self.closeExtDoors)
        self.extOpen.clicked.connect(self.openExtDoors)

        self.lcdFloorDisplay.setDigitCount(2)
        self.lcdFloorDisplay.display(2)

        self.arrowStyle = "background-color: orange; font: 32pt;"
        self.resetArrowStyle = "background-color: rgb(0, 0, 0); font: 32pt;"



    def openExtDoors(self):

        self.extLefta = QPropertyAnimation(self.extLeft, b"geometry")
        self.extLefta.setDuration(1000)
        self.extLefta.setStartValue(QRect(0, 0, 221, 591))
        self.extLefta.setEndValue(QRect(0, 0, 41, 591))
        self.extLefta.setEasingCurve(QEasingCurve.InOutCubic)

        self.extRighta = QPropertyAnimation(self.extRight, b"geometry")
        self.extRighta.setDuration(1000)
        self.extRighta.setStartValue(QRect(220, 0, 211, 591))
        self.extRighta.setEndValue(QRect(390, 0, 41, 591))
        self.extRighta.setEasingCurve(QEasingCurve.InOutCubic)

        self.extLefta.start()
        self.extRighta.start()
    
        
    def closeExtDoors(self):
        self.extLefta = QPropertyAnimation(self.extLeft, b"geometry")
        self.extLefta.setDuration(1000)
        self.extLefta.setStartValue(QRect(0, 0, 41, 591))
        self.extLefta.setEndValue(QRect(0, 0, 221, 591))
        self.extLefta.setEasingCurve(QEasingCurve.InOutCubic)

        self.extRighta = QPropertyAnimation(self.extRight, b"geometry")
        self.extRighta.setDuration(1000)
        self.extRighta.setStartValue(QRect(390, 0, 41, 591))
        self.extRighta.setEndValue(QRect(220, 0, 211, 591))
        self.extRighta.setEasingCurve(QEasingCurve.InOutCubic)

        self.extLefta.start()
        self.extRighta.start()

    def enterElevator(self):
        widget.setCurrentIndex(0)


    "function to change the extUpArrow and extDownArrow "

    
    
#main
if __name__ == '__main__':
    app = QApplication([])
    widget = QtWidgets.QStackedWidget()
    exterior = ElevateExterior()
    interior = ElevateInterior()
    widget.addWidget(interior)
    widget.addWidget(exterior)
    widget.setFixedHeight(720)
    widget.setFixedWidth(1280)
    widget.show()
    app.exec_()
