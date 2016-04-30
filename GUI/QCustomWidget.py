'''
Created on Apr 30, 2016

@author: Arthur
'''
from PyQt5.QtWidgets import *
from PyQt5 import *

class QCustomQWidget (QWidget):
    def __init__ (self, parent = None):
        super(QCustomQWidget, self).__init__(parent)
        self.textQVBoxLayout = QVBoxLayout()
        self.ifQHBoxLayout = QHBoxLayout()
        self.thenQHBoxLayout = QHBoxLayout()
        
        self.ifTextQLabel = QLabel('If',self)
        self.ifTextQComboBox    = QComboBox(self)
        
        self.equalTextQLabel = QLabel(' = ',self)
        self.equalTextQComboBox    = QComboBox(self)
        
        self.thenTextQLabel = QLabel('Then ', self)
        self.thenTextQComboBox    = QComboBox(self)
        
        
        self.ifQHBoxLayout.addWidget(self.ifTextQLabel)
        self.ifQHBoxLayout.addWidget(self.ifTextQComboBox)
        self.ifQHBoxLayout.addWidget(self.equalTextQLabel)
        self.ifQHBoxLayout.addWidget(self.equalTextQComboBox)
        
        self.thenQHBoxLayout.addWidget(self.thenTextQLabel)
        self.thenQHBoxLayout.addWidget(self.thenTextQComboBox)
        
        self.textQVBoxLayout.addLayout(self.ifQHBoxLayout,0)
        self.textQVBoxLayout.addLayout(self.thenQHBoxLayout,1)
        self.allQHBoxLayout  = QHBoxLayout()
        self.iconQLabel      = QLabel()
        self.allQHBoxLayout.addWidget(self.iconQLabel, 0)
        self.allQHBoxLayout.addLayout(self.textQVBoxLayout, 1)
        self.setLayout(self.allQHBoxLayout)
        # setStyleSheet
        self.ifTextQComboBox.setStyleSheet('''
            color: rgb(0, 0, 255);
        ''')
        self.equalTextQComboBox.setStyleSheet('''
            color: rgb(0, 0, 255);
        ''')
        self.thenTextQComboBox.setStyleSheet('''
            color: rgb(255, 0, 0);
        ''')

    def setIfConditions (self, list_of_strings):
        self.ifTextQComboBox.addItems(list_of_strings)
    def setEqualConditions (self, list_of_strings):
        self.equalTextQComboBox.addItems(list_of_strings)
    def setThenConditions (self, list_of_strings):
        self.thenTextQComboBox.addItems(list_of_strings)