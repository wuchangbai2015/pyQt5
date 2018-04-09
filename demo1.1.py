#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
 
 
class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI() #界面绘制交给InitUi方法
        
        
    def initUI(self):
        #设置窗口的位置和大小
        #前两个参数定位了窗口的x轴和y轴位置。
        #第三个参数是定义窗口的宽度，
        #设置窗口的标题第四个参数是定义窗口的高度。
        self.setGeometry(300, 330, 300, 220)  
        self.setWindowTitle('demo1.1')
        #设置窗口的图标，引用当前目录下的图片 搜索.ico图片
        self.setWindowIcon(QIcon('c1.png'))        
        
        #显示窗口
        self.show()
        
        
if __name__ == '__main__':
    #创建应用程序和对象
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_()) 



    




