# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Monitor_Form.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Monitors_Form(object):
    def setupUi(self, Monitors_Form):
        Monitors_Form.setObjectName("Monitors_Form")
        Monitors_Form.resize(430, 480)
        self.pushButton_monitor_help = QtWidgets.QPushButton(Monitors_Form)
        self.pushButton_monitor_help.setGeometry(QtCore.QRect(320, 430, 93, 28))
        self.pushButton_monitor_help.setObjectName("pushButton_monitor_help")
        self.pushButton_monitor_back_nagivator = QtWidgets.QPushButton(Monitors_Form)
        self.pushButton_monitor_back_nagivator.setGeometry(QtCore.QRect(20, 420, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_monitor_back_nagivator.setFont(font)
        self.pushButton_monitor_back_nagivator.setObjectName("pushButton_monitor_back_nagivator")
        self.pushButton_brainGraph_monitor = QtWidgets.QPushButton(Monitors_Form)
        self.pushButton_brainGraph_monitor.setGeometry(QtCore.QRect(90, 60, 260, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_brainGraph_monitor.setFont(font)
        self.pushButton_brainGraph_monitor.setObjectName("pushButton_brainGraph_monitor")
        self.pushButton_brainWeb_monitor = QtWidgets.QPushButton(Monitors_Form)
        self.pushButton_brainWeb_monitor.setGeometry(QtCore.QRect(90, 170, 260, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_brainWeb_monitor.setFont(font)
        self.pushButton_brainWeb_monitor.setObjectName("pushButton_brainWeb_monitor")
        self.pushButton_timefrequence_monitor = QtWidgets.QPushButton(Monitors_Form)
        self.pushButton_timefrequence_monitor.setGeometry(QtCore.QRect(90, 280, 260, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_timefrequence_monitor.setFont(font)
        self.pushButton_timefrequence_monitor.setObjectName("pushButton_timefrequence_monitor")

        self.retranslateUi(Monitors_Form)
        QtCore.QMetaObject.connectSlotsByName(Monitors_Form)

    def retranslateUi(self, Monitors_Form):
        _translate = QtCore.QCoreApplication.translate
        Monitors_Form.setWindowTitle(_translate("Monitors_Form", "Form"))
        self.pushButton_monitor_help.setText(_translate("Monitors_Form", "帮助"))
        self.pushButton_monitor_back_nagivator.setText(_translate("Monitors_Form", "返回导航界面"))
        self.pushButton_brainGraph_monitor.setText(_translate("Monitors_Form", "脑地形图监测"))
        self.pushButton_brainWeb_monitor.setText(_translate("Monitors_Form", "脑功能网络监测"))
        self.pushButton_timefrequence_monitor.setText(_translate("Monitors_Form", "时频能量监测"))
