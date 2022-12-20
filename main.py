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
        self.labelRooms = QLabel('Колличество комнат')

        self.floor = QLineEdit()
        self.labelFloor = QLabel('Этаж')

        self.floorsHome = QLineEdit()
        self.labelFloorsHome = QLabel('Количество этажей')

        self.square = QLineEdit()
        self.labelSquare = QLabel('Площадь в м2')

        self.ceilingHeight = QLineEdit()
        self.labelCeilingHeight = QLabel('Высота потолков')

        self.widgets()


    def widgets(self):

        self.mainWidget.resize(900,600)
        self.mainWidget.setWindowTitle('Pricer')


cianParser.test()


program = Program()
program.mainWidget.show()
program.app.exec_()

