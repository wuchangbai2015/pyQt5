#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, 
    QInputDialog, QApplication)


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)
        
        self.le = QLineEdit(self)
        self.le.move(130, 22)
        
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Input dialog')
        self.show()
        
        
    def showDialog(self):
        #用于显示输入对话框.
        #第一个字符串是对话框的标题,
        #第二个是对话框的信息.
        #对话框返回输入的文本和一个布尔型的值.如果我们点击Okbutton,那么布尔型的值为真.      
        text, ok = QInputDialog.getText(self, 'Input Dialog', 
            'Enter your name:')
        #print(ok)
        #print(text)
        
        if ok:
            self.le.setText(str(text))#从对话框收到的文本会被设置到行编辑器部件中.
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())