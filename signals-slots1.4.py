#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication

#创建一个新的信号叫closeApp.这个信号在鼠标被点击的时候被发送.信号连接到QMainWindow的close()槽.

class Communicate(QObject):
    
    closeApp = pyqtSignal() 
    

class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      
        #一个信号被创建,pyqtSignal()作为Communicate类的外部属性.
        self.c = Communicate()
        self.c.closeApp.connect(self.close) #把pyqtSignal()这个信号连接到close这个槽上  
        
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit signal')
        self.show()
        
    #当我们在窗口上点击鼠标的时候,closeApp信号就会被发送,程序就会被终止.       
    def mousePressEvent(self, event):
        
        self.c.closeApp.emit()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())