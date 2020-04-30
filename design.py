# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(481, 234)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("python.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineFile = QtWidgets.QLineEdit(self.centralwidget)
        self.lineFile.setObjectName("lineFile")
        self.verticalLayout.addWidget(self.lineFile)
        self.lineFolder = QtWidgets.QLineEdit(self.centralwidget)
        self.lineFolder.setObjectName("lineFolder")
        self.verticalLayout.addWidget(self.lineFolder)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btnSelectFile = QtWidgets.QPushButton(self.centralwidget)
        self.btnSelectFile.setObjectName("btnSelectFile")
        self.verticalLayout_2.addWidget(self.btnSelectFile)
        self.btnSelectFolder = QtWidgets.QPushButton(self.centralwidget)
        self.btnSelectFolder.setObjectName("btnSelectFolder")
        self.verticalLayout_2.addWidget(self.btnSelectFolder)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelFound = QtWidgets.QLabel(self.centralwidget)
        self.labelFound.setObjectName("labelFound")
        self.horizontalLayout_2.addWidget(self.labelFound)
        self.labelChanged = QtWidgets.QLabel(self.centralwidget)
        self.labelChanged.setObjectName("labelChanged")
        self.horizontalLayout_2.addWidget(self.labelChanged)
        self.btnStart = QtWidgets.QPushButton(self.centralwidget)
        self.btnStart.setEnabled(True)
        self.btnStart.setCheckable(False)
        self.btnStart.setObjectName("btnStart")
        self.horizontalLayout_2.addWidget(self.btnStart)
        self.labelInfo = QtWidgets.QLabel(self.centralwidget)
        self.labelInfo.setMidLineWidth(2)
        self.labelInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelInfo.setObjectName("labelInfo")
        self.horizontalLayout_2.addWidget(self.labelInfo)
        self.btnChange = QtWidgets.QPushButton(self.centralwidget)
        self.btnChange.setObjectName("btnChange")
        self.horizontalLayout_2.addWidget(self.btnChange)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_3.addWidget(self.listWidget)
        self.listErrors = QtWidgets.QListWidget(self.centralwidget)
        self.listErrors.setObjectName("listErrors")
        self.verticalLayout_3.addWidget(self.listErrors)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Replacer"))
        self.lineFile.setText(_translate("MainWindow", "No file is selected"))
        self.lineFolder.setText(_translate("MainWindow", "No destination is selected"))
        self.btnSelectFile.setText(_translate("MainWindow", "Select file"))
        self.btnSelectFolder.setText(_translate("MainWindow", "Select dest"))
        self.labelFound.setText(_translate("MainWindow", "Total: 0"))
        self.labelChanged.setText(_translate("MainWindow", "Changed: 0"))
        self.btnStart.setText(_translate("MainWindow", "Find"))
        self.labelInfo.setText(_translate("MainWindow", "->"))
        self.btnChange.setText(_translate("MainWindow", "Change"))
