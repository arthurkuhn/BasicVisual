'''
Created on Apr 30, 2016

@author: Arthur

'''
import cv2
#import numpy as np
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication
from Tix import Grid
from PyQt5.Qt import QLabel
from QCustomWidget import *

class Capture():
    def __init__(self):
        self.capturing = False
        self.c = cv2.VideoCapture(0)

    def startCapture(self):
        print "pressed start"
        self.capturing = True
        cap = self.c
        while(self.capturing):
            ret, frame = cap.read()
            cv2.imshow("Capture", frame)
            cv2.waitKey(5)
        cv2.destroyAllWindows()

    def endCapture(self):
        print "pressed End"
        self.capturing = False
        # cv2.destroyAllWindows()

    def quitCapture(self):
        print "pressed Quit"
        cap = self.c
        cv2.destroyAllWindows()
        cap.release()
        QCoreApplication.quit()
        
    
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.initUI()
    
    def initUI(self):
        #Possible options
        self.possibleAlgos = ["Recognize faces", "Recognize bodies"]
        self.possibleIfs = [["num faces","is face"],["num bodies","is body"]]
        self.possibleEquals = ["1","2","3"]
        self.possibleThen = ["Send to FB","Sent to Google Drive"]
        
        
        self.capture = Capture()
        
        self.start_button = QPushButton('Start', self)
        self.start_button.clicked.connect(self.capture.startCapture)
    
        self.end_button = QPushButton('End', self)
        self.end_button.clicked.connect(self.capture.endCapture)
    
        self.quit_button = QPushButton('Quit', self)
        self.quit_button.clicked.connect(self.capture.quitCapture)
        
        self.currActionsLabel = QLabel('Current Actions:')
        
        self.conditions = QComboBox(self) 
        self.conditions.addItems(self.possibleAlgos)
        #self.conditions.activated[str].connect(self.conditionChosen)
        
        self.listWidget = QListWidget()

        self.addAction_button = QPushButton('Add an action', self)
        self.addAction_button.clicked.connect(self.conditionChosen)
        
        
        grid = QGridLayout()
        grid.addWidget(self.currActionsLabel)
        grid.addWidget(self.listWidget)
        grid.addWidget(self.conditions)
        grid.addWidget(self.addAction_button)
        grid.addWidget(self.start_button)
        grid.addWidget(self.end_button)
        grid.addWidget(self.quit_button)

        self.setLayout(grid)
        self.setGeometry(300,300,300,300)
        self.setWindowTitle('Facebook Sydney Hackathon')
        self.show()
        
    def conditionChosen(self):
        #Get the number of the chosen algo (to retrieve the choices)
        chosen_algo = self.possibleAlgos.index(self.conditions.currentText())
        myQCustomQWidget = QCustomQWidget(self)
        myQCustomQWidget.setIfConditions(self.possibleIfs[chosen_algo])
        myQCustomQWidget.setEqualConditions(self.possibleEquals)
        myQCustomQWidget.setThenConditions(self.possibleThen)
        myQListWidgetItem = QListWidgetItem(self.listWidget)
        myQListWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())
        self.listWidget.addItem(myQListWidgetItem)
        self.listWidget.setItemWidget(myQListWidgetItem, myQCustomQWidget)
    
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
