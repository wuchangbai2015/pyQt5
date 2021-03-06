# coding:utf-8

from PyQt5 import QtCore,QtWidgets,QtGui
import complexGUI
import sys

class MainWindow(object):
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = complexGUI.Ui_MainWindow()
        self.ui.setupUi(MainWindow)

        self.update_calendar()
        self.update_date()
        self.set_dial()
        self.set_lcd()
        self.zero_process()
        self.update_process()
        self.click_radio3()
        self.set_font()

        MainWindow.show()
        sys.exit(app.exec_())

    # 修改日期修改器数值
    def update_date(self):
        self.ui.dateEdit.setDate(self.ui.calendarWidget.selectedDate())

    # 日历信号槽
    def update_calendar(self):
        self.ui.calendarWidget.selectionChanged.connect(self.update_date)

    # 设置LCD数字
    def set_lcd(self):
        self.ui.lcdNumber.display(self.ui.dial.value())

    # 刻度盘信号槽
    def set_dial(self):
        self.ui.dial.valueChanged['int'].connect(self.set_lcd)

    #第二个按钮清零进度栏
    def zero_process(self):
        self.ui.radioButton_2.clicked.connect(self.ui.progressBar.reset)

    # 更新进度栏
    def update_process(self):
        value = self.ui.lcdNumber.value()
        self.ui.progressBar.setValue(value)

    # 点击按钮3
    def click_radio3(self):
        self.ui.radioButton_3.clicked.connect(self.update_process)

    #设置字体
    def set_font(self):
        self.ui.fontComboBox.activated['QString'].connect(self.ui.label.setText)


if __name__ == "__main__":
    MainWindow()
