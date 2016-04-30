'''
Created on Apr 30, 2016

@author: Arthur
'''
from PyQt5.QtWidgets import *
from PyQt5 import *

class QCustomDropDownWidget (QWidget):
    def __init__ (self, parent = None):
        super(QCustomDropDownWidget, self).__init__(parent)
        self.initUI()
        
    def initUI(self):
        
        self.textQVBoxLayout = QVBoxLayout()
        self.ifQHBoxLayout = QHBoxLayout()
        self.thenQHBoxLayout = QHBoxLayout()
        
        self.algoQLabel = QLabel()
        
        self.ifTextQLabel = QLabel('If',self)
        self.ifTextQComboBox    = QComboBox(self)
        self.ifTextQComboBox.activated[str].connect(self.refresh)
        
        
        self.intEntryField = QLineEdit()
        
        self.relationQCombomBox = QComboBox()
        self.relationQCombomBox.addItems([" > ", " >= ", " = ", " <= ", " < "])
        
        self.select = QComboBox()
        self.select.addItems(["true","false"])
        self.equalQLabel = QLabel(' = ', self)
        
        
        self.thenTextQLabel = QLabel('Then ', self)
        self.thenTextQComboBox    = QComboBox(self)
        
        
        self.ifQHBoxLayout.addWidget(self.ifTextQLabel)
        self.ifQHBoxLayout.addWidget(self.ifTextQComboBox)
        self.ifQHBoxLayout.addWidget(self.equalQLabel)
        self.ifQHBoxLayout.addWidget(self.select)
        
        self.thenQHBoxLayout.addWidget(self.thenTextQLabel)
        self.thenQHBoxLayout.addWidget(self.thenTextQComboBox)
        
        self.textQVBoxLayout.addWidget(self.algoQLabel)
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
        self.thenTextQComboBox.setStyleSheet('''
            color: rgb(255, 0, 0);
        ''')
    def setAlgo (self, string):
        self.algoQLabel.setText(string)
    def setIfConditions (self, list_of_strings):
        self.ifTextQComboBox.addItems(list_of_strings)
    def setThenConditions (self, list_of_strings):
        self.thenTextQComboBox.addItems(list_of_strings)
    def refresh(self,str):
        if 'Num' in str:
            print 'isNum'
            self.relationQCombomBox = QComboBox()
            self.relationQCombomBox.addItems([" > ", " >= ", " = ", " <= ", " < "])
            self.intEntryField = QLineEdit()
            obj1 = self.ifQHBoxLayout.replaceWidget(self.equalQLabel, self.relationQCombomBox)
            obj2 = self.ifQHBoxLayout.replaceWidget(self.select, self.intEntryField)
            obj1.widget().deleteLater()
            obj2.widget().deleteLater()
        elif 'is' in str:
            print 'isNot'
            self.select = QComboBox()
            self.select.addItems(["true","false"])
            self.equalQLabel = QLabel(' = ', self)
            obj1 = self.ifQHBoxLayout.replaceWidget(self.relationQCombomBox,self.equalQLabel)
            obj2 = self.ifQHBoxLayout.replaceWidget(self.intEntryField,self.select)
            obj1.widget().deleteLater()
            obj2.widget().deleteLater()
        
        self.ifQHBoxLayout.update()
        self.thenQHBoxLayout.update()
        self.setLayout(self.allQHBoxLayout)
        