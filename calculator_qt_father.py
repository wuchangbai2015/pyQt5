# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator_qt_father.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def __init__(self):
        self.__data = "0"
        self.__str1 = ''
        self.__str2 = ''



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 230)
        MainWindow.setMinimumSize(QtCore.QSize(500, 230))
        MainWindow.setMaximumSize(QtCore.QSize(500, 230))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 481, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setText(self.__data)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 60, 481, 112))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_2.addWidget(self.pushButton_5, 0, 1, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_2.addWidget(self.pushButton_9, 0, 2, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_2.addWidget(self.pushButton_13, 0, 3, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_2.addWidget(self.pushButton_6, 1, 1, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_2.addWidget(self.pushButton_10, 1, 2, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout_2.addWidget(self.pushButton_14, 1, 3, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 2, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_2.addWidget(self.pushButton_7, 2, 1, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_2.addWidget(self.pushButton_11, 2, 2, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout_2.addWidget(self.pushButton_15, 2, 3, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 3, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_2.addWidget(self.pushButton_8, 3, 1, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_2.addWidget(self.pushButton_12, 3, 2, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout_2.addWidget(self.pushButton_16, 3, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.menu.addAction(self.actionClose)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.actionClose.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.click_1)
        self.pushButton_5.clicked.connect(self.click_2)
        self.pushButton_9.clicked.connect(self.click_3)

        self.pushButton_14.clicked.connect(self.click_add)

    def click_1(self):
        if self.__data == "0":
            self.__data = '1'
        else:
            self.__data = self.__data + '1'
        self.label.setText(self.__data)

    def click_2(self):
        if self.__data == "0":
            self.__data = '2'
        else:
            self.__data = self.__data + '2'
        self.label.setText(self.__data)

    def click_3(self):
        if self.__data == "0":
            self.__data = '3'
        else:
            self.__data = self.__data + '3'
        #print(int(self.__data))
        self.label.setText(self.__data)
    def click_add(self):
        self.label.clear()
        self.label.setText("+")
        self.__data = "0"

    def cal(self):
        pass





    def retranslateUi(self,MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "calculator"))
        MainWindow.setStatusTip(_translate("MainWindow", "这是一个简单的计算器"))
        self.pushButton.setText(_translate("MainWindow", "1"))
        self.pushButton_5.setText(_translate("MainWindow", "2"))
        self.pushButton_9.setText(_translate("MainWindow", "3"))
        self.pushButton_13.setText(_translate("MainWindow", "C"))
        self.pushButton_2.setText(_translate("MainWindow", "4"))
        self.pushButton_6.setText(_translate("MainWindow", "5"))
        self.pushButton_10.setText(_translate("MainWindow", "6"))
        self.pushButton_14.setText(_translate("MainWindow", "+"))
        self.pushButton_3.setText(_translate("MainWindow", "7"))
        self.pushButton_7.setText(_translate("MainWindow", "8"))
        self.pushButton_11.setText(_translate("MainWindow", "9"))
        self.pushButton_15.setText(_translate("MainWindow", "-"))
        self.pushButton_4.setText(_translate("MainWindow", "0"))
        self.pushButton_8.setText(_translate("MainWindow", "*"))
        self.pushButton_12.setText(_translate("MainWindow", "/"))
        self.pushButton_16.setText(_translate("MainWindow", "="))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.actionClose.setText(_translate("MainWindow", "关闭"))
        self.actionClose.setStatusTip(_translate("MainWindow", "你确定要关闭吗？"))
        self.actionClose.setShortcut(_translate("MainWindow", "Ctrl+Q"))

