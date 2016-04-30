'''
Created on Apr 30, 2016

@author: Arthur

'''
import cv2
#import numpy as np
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QVBoxLayout
from PyQt5.QtCore import QCoreApplication


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
        
        self.capture = Capture()
        self.start_button = QPushButton('Start', self)
        self.start_button.clicked.connect(self.capture.startCapture)
    
        self.end_button = QPushButton('End', self)
        self.end_button.clicked.connect(self.capture.endCapture)
    
        self.quit_button = QPushButton('Quit', self)
        self.quit_button.clicked.connect(self.capture.quitCapture)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.start_button)
        vbox.addWidget(self.end_button)
        vbox.addWidget(self.quit_button)

        self.setLayout(vbox)
        self.setGeometry(100,100,200,200)
        self.show()
    
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
