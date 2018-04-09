
import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication


class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        btn1 = QPushButton("Button 1", self)
        btn1.move(30, 50)

        btn2 = QPushButton("Button 2", self)
        btn2.move(150, 50)
      
        btn1.clicked.connect(self.buttonClicked)  #两个按钮被连接到相同的槽          
        btn2.clicked.connect(self.buttonClicked)
        
        self.statusBar()
        
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()
        
    #我们通过调用sender()方法来决定信号来源.在程序的状态栏,会显示按钮标签被点击      
    def buttonClicked(self):
      
        sender = self.sender()#通过调用sender()方法我们会知道哪个按钮被点击
        self.statusBar().showMessage(sender.text() + ' was pressed')
        #print(sender.text())
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())