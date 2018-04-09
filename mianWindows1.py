# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mianWindows-1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Dialog1

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(500, 400)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 30, 471, 131))
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(180, 90, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(170, 40, 221, 21))
        self.label.setObjectName("label")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 23))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)


        self.pushButton.clicked.connect(self.click_open)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "mainWindows(请关注头条号：小5嵌入式)"))
        self.groupBox.setTitle(_translate("mainWindow", "主页面对话框控制界面"))
        self.pushButton.setText(_translate("mainWindow", "open"))
        self.label.setText(_translate("mainWindow", "<html><head/><body><p><br/></p></body></html>"))

    def click_open(self):
        Dialog = QtWidgets.QDialog()
        ui = Dialog1.Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        #Dialog.exec_()
        rsp = Dialog.exec_()
        #print(rsp)
        if rsp == QtWidgets.QDialog.Accepted:#表示的是对话框的接收事件
            self.label.setText("点击了OK")
        else:
            self.label.setText("点击了Cannel")

if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication, QMainWindow
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
