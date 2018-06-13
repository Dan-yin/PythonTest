# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\GitHub\Public\PythonTest\PyQt5\check.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EQCCheck(object):
    def setupUi(self, EQCCheck):
        EQCCheck.setObjectName("EQCCheck")
        EQCCheck.resize(529, 208)
        self.centralwidget = QtWidgets.QWidget(EQCCheck)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.gridLayout.setContentsMargins(19, 21, 33, 16)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(19)
        self.gridLayout.setObjectName("gridLayout")
        self.Load = QtWidgets.QPushButton(self.centralwidget)
        self.Load.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Load.sizePolicy().hasHeightForWidth())
        self.Load.setSizePolicy(sizePolicy)
        self.Load.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Load.setFont(font)
        self.Load.setAutoRepeatDelay(100)
        self.Load.setObjectName("Load")
        self.gridLayout.addWidget(self.Load, 0, 1, 1, 1)
        self.LoadCSV = QtWidgets.QLineEdit(self.centralwidget)
        self.LoadCSV.setInputMethodHints(QtCore.Qt.ImhPreferUppercase)
        self.LoadCSV.setObjectName("LoadCSV")
        self.gridLayout.addWidget(self.LoadCSV, 0, 0, 1, 1)
        self.SaveCSV = QtWidgets.QLineEdit(self.centralwidget)
        self.SaveCSV.setObjectName("SaveCSV")
        self.gridLayout.addWidget(self.SaveCSV, 1, 0, 1, 1)
        self.Save = QtWidgets.QPushButton(self.centralwidget)
        self.Save.setObjectName("Save")
        self.gridLayout.addWidget(self.Save, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(348, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.Run = QtWidgets.QPushButton(self.centralwidget)
        self.Run.setObjectName("Run")
        self.gridLayout_2.addWidget(self.Run, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        EQCCheck.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EQCCheck)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 529, 23))
        self.menubar.setObjectName("menubar")
        EQCCheck.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(EQCCheck)
        self.toolBar.setObjectName("toolBar")
        EQCCheck.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusBar = QtWidgets.QStatusBar(EQCCheck)
        self.statusBar.setObjectName("statusBar")
        EQCCheck.setStatusBar(self.statusBar)

        self.retranslateUi(EQCCheck)
        QtCore.QMetaObject.connectSlotsByName(EQCCheck)

    def retranslateUi(self, EQCCheck):
        _translate = QtCore.QCoreApplication.translate
        EQCCheck.setWindowTitle(_translate("EQCCheck", "EQCCHECK"))
        self.Load.setText(_translate("EQCCheck", "Load"))
        self.Save.setText(_translate("EQCCheck", "Save"))
        self.Run.setText(_translate("EQCCheck", "Run"))
        self.toolBar.setWindowTitle(_translate("EQCCheck", "toolBar"))

