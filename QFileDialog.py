#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QIcon

#QFileDialog是允许用户选择文件或目录的对话框.文件可以是打开或保存

#这个例子显示了一个菜单栏和一个状态栏,
#是间是一个文本编辑器部件.菜单项里显示了QtGui.QFileDialog,
#它用于选择一个文件.文件的内容会被加载到文本编辑器部件内.
class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('c1.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)       
        
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')
        self.show()
        
        
    def showDialog(self):

        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        #弹出一个QFileDialog.
        #在getOpenFileName()方法的第一个字符串是标题.
        #第二个字符串指定对话框的工作目录.默认情况下,文件过滤器被设置为允许所有文件(*).
        f = open(fname, 'r')
        
        with f:        
            data = f.read()
            self.textEdit.setText(data) 
                                
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())