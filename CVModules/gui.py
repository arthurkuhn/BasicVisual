'''
Created on Apr 30, 2016

@author: Arthur

'''
import cv2
# import numpy as np
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication
from Tix import Grid
from PyQt5.Qt import QLabel
from QCustomWidget import *
import run
import ifModule
from BasicVisual.CVModules import ifCreator
import os.path as osp
import sys

path = osp.join(osp.dirname(sys.modules[__name__].__file__), 'application-icon.png')

class Capture():
    def __init__(self,):
        self.capturing = False
        self.c = cv2.VideoCapture(0)

    def startCapture(self, actionList):
        
        if(len(actionList)==0):
            QMessageBox.about(QWidget(),"Error", "What are you doing? There are no actions!!!")
            return
        
        ifModules = []
        
        for action in actionList:
            if action is None:
                continue
            
            components = {}
            components["module"] = action.getAlgo().replace(" ", "")
            ifCondition = action.getIfCondition().replace(" ", "")
            components["var"] = ifCondition
            
            if ifCondition == "":
                components["comp"] = ""
                components["eq"] = action.getTags()
            elif 'Is' not in ifCondition:
                components["comp"] = action.getComparisonOperator().replace(" ", "")
                components["eq"] = action.getEquality()
            else:
                components["comp"] = "="
                components["eq"] = action.getBooleanSelect().replace(" ", "")
            components["expression"] = action.getThenCondition().replace(" ", "")
            components["time"] = action.getTimeInterval()
            print components
            
            ifModules.append(ifCreator.createIF(components))
        '''
        print "pressed start"
        self.capturing = True
        cap = self.c
        while(self.capturing):
            ret, frame = cap.read()
            cv2.imshow("Capture", frame)
            cv2.waitKey(5)
        cv2.destroyAllWindows()
        '''
        
        run.execute(ifModules)
        
        # run.execute()
        

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
    
    def run(self):
        self.capture.startCapture(self.actionList)
    
    def initUI(self):
        # Possible options
        self.possibleAlgos = ["Face Detect", "Body Detect", "Motion Detect", "Object Detect"]
        self.possibleIfs = [["There Is A Face", "Number Of Faces"], ["There Is A Body", "Number Of Bodies"], ["There Is Motion"]]
        self.possibleThen = ["Post Image To Facebook", "Post Image To Dropbox", "Send An Email", "Log To Sheets", "Send Text", "Send Tweet","Upload And Log"]
        
        
        self.listWidget = QListWidget()
        self.actionList = []
        
        self.capture = Capture()
        
        self.start_button = QPushButton('Start', self)
        self.start_button.clicked.connect(self.run)
    
        self.quit_button = QPushButton('Quit', self)
        self.quit_button.clicked.connect(self.capture.quitCapture)
        
        self.currActionsLabel = QLabel('Current Actions:')
        
        # List With the possible algorithms
        self.conditions = QComboBox(self) 
        self.conditions.addItems(self.possibleAlgos)
        
        self.listWidget = QListWidget()

        self.addAction_button = QPushButton('Add an action', self)
        self.addAction_button.clicked.connect(self.conditionChosen)
        
        self.removeAction_button = QPushButton('Delete selected', self)
        self.removeAction_button.clicked.connect(self.deleteCondition)
        
        
        listQVBox = QVBoxLayout()
        listQVBox.addWidget(self.currActionsLabel)
        listQVBox.addWidget(self.listWidget)
        listQVBox.addWidget(self.conditions)
        
        algoActionButtons = QHBoxLayout()
        algoActionButtons.addWidget(self.addAction_button)
        algoActionButtons.addWidget(self.removeAction_button)
        listQVBox.addLayout(algoActionButtons)
        
        videoActionButtons = QHBoxLayout()
        videoActionButtons.addWidget(self.start_button)
        videoActionButtons.addWidget(self.quit_button)
        listQVBox.addLayout(videoActionButtons)

        self.setLayout(listQVBox)
        self.setGeometry(400, 500, 500, 500)
        self.setWindowTitle('Facebook Sydney Hackathon')
        self.center()
        self.show()
        
    def deleteCondition(self):
        listItems = self.listWidget.selectedItems()
        if not listItems: return        
        for item in listItems:
            self.listWidget.takeItem(self.listWidget.row(item))
            del self.actionList[self.listWidget.row(item)]
    
    def conditionChosen(self):
        # Get the number of the chosen algo (to retrieve the choices)
        chosen_algo = self.possibleAlgos.index(self.conditions.currentText())
        if "Object" not in self.conditions.currentText():     
            myQCustomQWidget = QCustomDropDownWidget(self)
            myQCustomQWidget.setAlgo(self.possibleAlgos[chosen_algo])
            myQCustomQWidget.setIfConditions(self.possibleIfs[chosen_algo])
            myQCustomQWidget.setThenConditions(self.possibleThen)
            self.actionList.append(myQCustomQWidget)
            myQListWidgetItem = QListWidgetItem(self.listWidget)
            myQListWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())
            self.listWidget.addItem(myQListWidgetItem)
            self.listWidget.setItemWidget(myQListWidgetItem, myQCustomQWidget)
        else:
            myQCustomQWidget = QCustomObjectWidget(self)
            myQCustomQWidget.setAlgo(self.possibleAlgos[chosen_algo])
            myQCustomQWidget.setThenConditions(self.possibleThen)
            self.actionList.append(myQCustomQWidget)
            myQListWidgetItem = QListWidgetItem(self.listWidget)
            myQListWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())
            self.listWidget.addItem(myQListWidgetItem)
            self.listWidget.setItemWidget(myQListWidgetItem, myQCustomQWidget)
    
    def center(self):
        frameGm = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(path))
    window = Window()
    sys.exit(app.exec_())
