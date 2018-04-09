# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator_main.py'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys
import calculator_qt_father
from PyQt5 import QtCore, QtGui, QtWidgets

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = calculator_qt_father.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

