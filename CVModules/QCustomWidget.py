'''
Created on Apr 30, 2016

@author: Arthur
'''
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from PyQt5.QtCore import *
from Tkconstants import HORIZONTAL

class QCustomObjectWidget(QWidget):
    def __init__ (self, parent = None):
        super(QCustomObjectWidget, self).__init__(parent)
        self.initUI()
    def initUI(self):
        self.textQVBoxLayout = QVBoxLayout()
        self.ifQHBoxLayout = QHBoxLayout()
        self.thenQHBoxLayout = QHBoxLayout()
        self.timeQHBoxLayout = QHBoxLayout()
        
        # Font for title:
        font = QFont()
        font.setFamily(("FreeMono"))
        font.setBold(True)

        
        self.algoQLabel = QLabel()
        self.algoQLabel.setFont(font)
        self.ifTextQLabel = QLabel('If there is (use tags): ',self)
        self.tagEntryField = QLineEdit()
        
        self.ifQHBoxLayout.addWidget(self.ifTextQLabel)
        self.ifQHBoxLayout.addWidget(self.tagEntryField)
        
        self.thenTextQLabel = QLabel('Then ', self)
        self.thenTextQComboBox    = QComboBox(self)
        self.thenQHBoxLayout.addWidget(self.thenTextQLabel)
        self.thenQHBoxLayout.addWidget(self.thenTextQComboBox)
        
        self.timeLimitQLabel = QLabel('Time Interval (in seconds): ', self)
        self.timeLimitQComboBox = QComboBox(self)
        self.timeLimitQComboBox.addItems(["5","10","15","20","25","25","30","50","60","90","120"])
        self.timeQHBoxLayout.addWidget(self.timeLimitQLabel)
        self.timeQHBoxLayout.addWidget(self.timeLimitQComboBox)
        
        self.textQVBoxLayout.addWidget(self.algoQLabel)
        self.textQVBoxLayout.addLayout(self.ifQHBoxLayout,0)
        self.textQVBoxLayout.addLayout(self.thenQHBoxLayout,1)
        self.textQVBoxLayout.addLayout(self.timeQHBoxLayout,2)
        

        self.allQHBoxLayout  = QHBoxLayout()
        self.iconQLabel      = QLabel()
        self.allQHBoxLayout.addWidget(self.iconQLabel, 0)
        self.allQHBoxLayout.addLayout(self.textQVBoxLayout, 1)
        self.setLayout(self.allQHBoxLayout)
        
        
        # setStyleSheet
        self.thenTextQComboBox.setStyleSheet('''
            color: rgb(255, 0, 0);
        ''')
        
    def setAlgo (self, string):
        self.algoQLabel.setText(string)
    def getAlgo(self):
        return self.algoQLabel.text()
    def setThenConditions (self, list_of_strings):
        self.thenTextQComboBox.addItems(list_of_strings)
    def getTags(self):
        return self.tagEntryField.text()
    def getTimeInterval(self):
        return int(self.timeLimitQComboBox.currentText())
    def getIfCondition(self):
        return ""
    def getThenCondition(self):
        return self.thenTextQComboBox.currentText()
        
        
        

class QCustomDropDownWidget (QWidget):
    def __init__ (self, parent = None):
        super(QCustomDropDownWidget, self).__init__(parent)
        self.initUI()
        
    def initUI(self):
        
        self.textQVBoxLayout = QVBoxLayout()
        self.ifQHBoxLayout = QHBoxLayout()
        self.thenQHBoxLayout = QHBoxLayout()
        self.timeQHBoxLayout = QHBoxLayout()
        
        # Font for title:
        font = QFont()
        font.setFamily(("FreeMono"))
        font.setBold(True)
        
        self.algoQLabel = QLabel()
        self.algoQLabel.setFont(font)
        
        self.ifTextQLabel = QLabel('If',self)
        self.ifTextQComboBox    = QComboBox(self)
        self.ifTextQComboBox.activated[str].connect(self.refresh)
        
        
        self.intEntryField = QLineEdit()
        
        self.relationQCombomBox = QComboBox()
        self.relationQCombomBox.addItems([" > ", " >= ", " = ", " <= ", " < "])
        
        self.select = QComboBox()
        self.select.addItems(["True","False"])
        self.equalQLabel = QLabel(' = ', self)
        
        
        self.thenTextQLabel = QLabel('Then ', self)
        self.thenTextQComboBox    = QComboBox(self)
        
        self.timeLimitQLabel = QLabel('Time Interval (in seconds): ', self)
        self.timeLimitQComboBox = QComboBox(self)
        self.timeLimitQComboBox.addItems(["5","10","15","20","25","25","30","50","60","90","120"])
        self.timeQHBoxLayout.addWidget(self.timeLimitQLabel)
        self.timeQHBoxLayout.addWidget(self.timeLimitQComboBox)
        
        self.ifQHBoxLayout.addWidget(self.ifTextQLabel)
        self.ifQHBoxLayout.addWidget(self.ifTextQComboBox)
        self.ifQHBoxLayout.addWidget(self.equalQLabel)
        self.ifQHBoxLayout.addWidget(self.select)
        
        self.thenQHBoxLayout.addWidget(self.thenTextQLabel)
        self.thenQHBoxLayout.addWidget(self.thenTextQComboBox)
        
        self.textQVBoxLayout.addWidget(self.algoQLabel)
        self.textQVBoxLayout.addLayout(self.ifQHBoxLayout,0)
        self.textQVBoxLayout.addLayout(self.thenQHBoxLayout,1)
        self.textQVBoxLayout.addLayout(self.timeQHBoxLayout,2)
        
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
        elif 'Is' in str:
            print 'isNot'
            self.select = QComboBox()
            self.select.addItems(["True","False"])
            self.equalQLabel = QLabel(' = ', self)
            obj1 = self.ifQHBoxLayout.replaceWidget(self.relationQCombomBox,self.equalQLabel)
            obj2 = self.ifQHBoxLayout.replaceWidget(self.intEntryField,self.select)
            obj1.widget().deleteLater()
            obj2.widget().deleteLater()
        
        self.ifQHBoxLayout.update()
        self.thenQHBoxLayout.update()
        self.setLayout(self.allQHBoxLayout)
    def getAlgo(self):
        return self.algoQLabel.text()
    def getIfCondition(self):
        return self.ifTextQComboBox.currentText()
    def getThenCondition(self):
        return self.thenTextQComboBox.currentText()
    def getBooleanSelect(self):
        return self.select.currentText()
    def getComparisonOperator(self):
        return self.relationQCombomBox.currentText()
    def getEquality(self):
        return int(self.intEntryField.text())
    def getTimeInterval(self):
        return int(self.timeLimitQComboBox.currentText())
        