# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\GitHub\Public\PythonTest\PyQt5\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow
import sys
'''
app = QApplication(sys.argv) 
w = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(w)

sys.exit(app.exec_())
'''
class mywindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent = None):
        super(mywindow,self).__init__(parent)
        self.setupUi(self)

app = QApplication(sys.argv)
ui = mywindow()
ui.show()
sys.exit(app.exec_())