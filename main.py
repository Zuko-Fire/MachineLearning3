# import requests
# import time
# from bs4 import BeautifulSoup as bs
# import pandas as pd
# import numpy as np
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

import cianParser


class Program():

    def __init__(self):
        self.app = QApplication([])
        self.mainWidget = QWidget()

        self.rooms = QLineEdit()
        self.rooms.setAlignment(Qt.AlignTop)
        self.labelRooms = QLabel('Колличество комнат')
        self.labelRooms.setAlignment(Qt.AlignCenter)

        self.floor = QLineEdit()
        self.labelFloor = QLabel('Этаж')
        self.labelFloor.setAlignment(Qt.AlignCenter)

        self.floorsHome = QLineEdit()
        self.labelFloorsHome = QLabel('Количество этажей')
        self.labelFloorsHome.setAlignment(Qt.AlignCenter)

        self.square = QLineEdit()
        self.labelSquare = QLabel('Площадь в м2')
        self.labelSquare.setAlignment(Qt.AlignCenter)

        self.ceilingHeight = QLineEdit()
        self.labelCeilingHeight = QLabel('Высота потолков')
        self.labelCeilingHeight.setAlignment(Qt.AlignCenter)

        self.parkBox = QGroupBox('Парковка')
        self.parkBoxlayout = QVBoxLayout()

        self.radioParkNeverMind = QRadioButton('Не важно')
        self.radioParkTwo= QRadioButton('Наземная')
        self.radioParkThree = QRadioButton('Подземная')

        self.windowBox = QGroupBox('Окно')
        self.windowLayout = QVBoxLayout()
        self.radioWindowNeverMind = QRadioButton('Не важно')
        self.radioWindowTwo = QRadioButton('На улицу')
        self.radioWindowThree = QRadioButton('Во двор')
        self.radioWindowFour = QRadioButton('На улицу и во двор')

        self.repairBox =




        self.mainLayout = QHBoxLayout()

        self.oneLayout = QVBoxLayout()
        self.twoLayout = QVBoxLayout()
        self.threeLayout = QVBoxLayout()

        self.widgets()


    def widgets(self):

        self.mainWidget.resize(900,600)
        self.mainWidget.setWindowTitle('Pricer')

        self.parkBoxlayout.addWidget(self.radioParkNeverMind)
        self.parkBoxlayout.addWidget(self.radioParkTwo)
        self.parkBoxlayout.addWidget(self.radioParkThree)
        self.parkBox.setLayout(self.parkBoxlayout)

        self.windowLayout.addWidget(self.radioWindowNeverMind)
        self.windowLayout.addWidget(self.radioWindowTwo)
        self.windowLayout.addWidget(self.radioWindowThree)
        self.windowLayout.addWidget(self.radioWindowFour)
        self.windowBox.setLayout(self.windowLayout)

        self.oneLayout.addWidget(self.labelRooms)
        self.oneLayout.addWidget(self.rooms)

        self.oneLayout.addWidget(self.labelSquare)
        self.oneLayout.addWidget(self.square)
        self.oneLayout.addWidget(self.parkBox)
        self.oneLayout.addWidget(self.windowBox)


        self.twoLayout.addWidget(self.labelFloor)
        self.twoLayout.addWidget(self.floor)

        self.threeLayout.addWidget(self.labelFloorsHome)
        self.threeLayout.addWidget(self.floorsHome)

        self.threeLayout.addWidget(self.labelCeilingHeight)
        self.threeLayout.addWidget(self.ceilingHeight)



        #
        # self.oneLayout.setSpacing(1)
        # self.twoLayout.setSpacing(1)
        # self.threeLayout.setSpacing(1)
        #
        # self.mainLayout.addSpacing(1)

        self.mainLayout.addLayout(self.oneLayout,stretch=1)
        self.mainLayout.addLayout(self.twoLayout,stretch=1)
        self.mainLayout.addLayout(self.threeLayout,stretch=1)

        self.mainWidget.setLayout(self.mainLayout)


cianParser.test()


program = Program()
program.mainWidget.show()
program.app.exec_()

