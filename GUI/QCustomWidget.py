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
        
        self.equalPart = QCustomEqualField(self)
        
        self.textQVBoxLayout = QVBoxLayout()
        self.ifQHBoxLayout = QHBoxLayout()
        self.thenQHBoxLayout = QHBoxLayout()
        
        self.algoQLabel = QLabel()
        
        self.ifTextQLabel = QLabel('If',self)
        self.ifTextQComboBox    = QComboBox(self)
        self.ifTextQComboBox.activated[str].connect(self.equalPart.refresh)
        self.ifTextQComboBox.activated[str].connect(self.refresh)
        
        
        self.thenTextQLabel = QLabel('Then ', self)
        self.thenTextQComboBox    = QComboBox(self)
        
        
        self.ifQHBoxLayout.addWidget(self.ifTextQLabel)
        self.ifQHBoxLayout.addWidget(self.ifTextQComboBox)
        self.ifQHBoxLayout.addSpacing(2)
        self.ifQHBoxLayout.addLayout(self.equalPart)
        
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
        self.equalPart.setStyleSheet('''
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
    def refresh(self):
        self.ifQHBoxLayout.update()
        self.thenQHBoxLayout.update()
        self.setLayout(self.allQHBoxLayout)
        
            
        
        
class QCustomEqualField(QWidget):
    def __init__ (self, parent = None):
        super(QCustomEqualField, self).__init__(parent)
        self.initUI()
        
    def initUI(self):
        self.intEntryField = QLineEdit()
        self.select = QComboBox()
        self.select.addItems(["true","false"])
        self.relationQCombomBox = QComboBox()
        self.relationQCombomBox.addItems([" > ", " >= ", " = ", " <= ", " < "])
        self.equalQLabel = QLabel(' = ', self)
        self.currLayout = QHBoxLayout()
        self.currLayout.addWidget(self.select)
        self.setLayout(self.currLayout)
        
    def refresh(self, str):
        if 'Num' in str:
            print 'isNum'
            self.currLayout.replaceWidget(self.equalQLabel, self.relationQCombomBox)
            self.currLayout.replaceWidget(self.select, self.intEntryField)
            self.currLayout.removeWidget(self.select)
            self.currLayout.removeWidget(self.equalQLabel)
        elif 'is' in str:
            print 'isNot'
            self.currLayout.replaceWidget(self.relationQCombomBox,self.equalQLabel)
            self.currLayout.replaceWidget(self.intEntryField,self.select)
            self.currLayout.removeWidget(self.relationQCombomBox)
            self.currLayout.removeWidget(self.intEntryField)

        
        #self.currLayout.activate()
        self.setLayout(self.currLayout)
        