import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider, 
    QVBoxLayout, QApplication)


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        lcd = QLCDNumber(self)#lcd
        sld = QSlider(Qt.Horizontal, self)#滑块

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)

        #连接滑动器上的valueChanged信号到lcd数字的display槽.
        #发送者是一个对象,它发送一个信号.接收者是一个对象,它接收信号.槽是作用于信号的方法.
        
        #信号和槽用于在对象之间通信.一个信号是在某特定事件发生时被发送的.
        #一个槽可以是任何的Python调用.一个槽当它连接的信号被发送的时候被调用.
        sld.valueChanged.connect(lcd.display)
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal & slot')
        self.show()
        

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())