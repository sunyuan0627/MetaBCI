# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'data_cut.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_datacut(object):
    def setupUi(self, Dialog_datacut):
        Dialog_datacut.setObjectName("Dialog_datacut")
        Dialog_datacut.resize(456, 462)
        self.frame = QtWidgets.QFrame(Dialog_datacut)
        self.frame.setGeometry(QtCore.QRect(0, 0, 456, 381))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.checkBox_1 = QtWidgets.QCheckBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_1.setFont(font)
        self.checkBox_1.setCheckable(True)
        self.checkBox_1.setChecked(False)
        self.checkBox_1.setObjectName("checkBox_1")
        self.gridLayout.addWidget(self.checkBox_1, 1, 0, 1, 1)
        self.lineEdit_1f = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_1f.setFont(font)
        self.lineEdit_1f.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_1f.setObjectName("lineEdit_1f")
        self.gridLayout.addWidget(self.lineEdit_1f, 1, 1, 1, 1)
        self.lineEdit_1a = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_1a.setFont(font)
        self.lineEdit_1a.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_1a.setObjectName("lineEdit_1a")
        self.gridLayout.addWidget(self.lineEdit_1a, 1, 2, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 2, 0, 1, 1)
        self.lineEdit_2f = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_2f.setFont(font)
        self.lineEdit_2f.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2f.setObjectName("lineEdit_2f")
        self.gridLayout.addWidget(self.lineEdit_2f, 2, 1, 1, 1)
        self.lineEdit_2a = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_2a.setFont(font)
        self.lineEdit_2a.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2a.setObjectName("lineEdit_2a")
        self.gridLayout.addWidget(self.lineEdit_2a, 2, 2, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 3, 0, 1, 1)
        self.lineEdit_3f = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_3f.setFont(font)
        self.lineEdit_3f.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3f.setObjectName("lineEdit_3f")
        self.gridLayout.addWidget(self.lineEdit_3f, 3, 1, 1, 1)
        self.lineEdit_3a = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_3a.setFont(font)
        self.lineEdit_3a.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3a.setObjectName("lineEdit_3a")
        self.gridLayout.addWidget(self.lineEdit_3a, 3, 2, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout.addWidget(self.checkBox_4, 4, 0, 1, 1)
        self.lineEdit_4f = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_4f.setFont(font)
        self.lineEdit_4f.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4f.setObjectName("lineEdit_4f")
        self.gridLayout.addWidget(self.lineEdit_4f, 4, 1, 1, 1)
        self.lineEdit_4a = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_4a.setFont(font)
        self.lineEdit_4a.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4a.setObjectName("lineEdit_4a")
        self.gridLayout.addWidget(self.lineEdit_4a, 4, 2, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout.addWidget(self.checkBox_5, 5, 0, 1, 1)
        self.lineEdit_5f = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_5f.setFont(font)
        self.lineEdit_5f.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5f.setObjectName("lineEdit_5f")
        self.gridLayout.addWidget(self.lineEdit_5f, 5, 1, 1, 1)
        self.lineEdit_5a = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_5a.setFont(font)
        self.lineEdit_5a.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5a.setObjectName("lineEdit_5a")
        self.gridLayout.addWidget(self.lineEdit_5a, 5, 2, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_6.setFont(font)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout.addWidget(self.checkBox_6, 6, 0, 1, 1)
        self.lineEdit_6f = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_6f.setFont(font)
        self.lineEdit_6f.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6f.setObjectName("lineEdit_6f")
        self.gridLayout.addWidget(self.lineEdit_6f, 6, 1, 1, 1)
        self.lineEdit_6a = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_6a.setFont(font)
        self.lineEdit_6a.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6a.setObjectName("lineEdit_6a")
        self.gridLayout.addWidget(self.lineEdit_6a, 6, 2, 1, 1)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.checkBox_s1 = QtWidgets.QCheckBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_s1.sizePolicy().hasHeightForWidth())
        self.checkBox_s1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_s1.setFont(font)
        self.checkBox_s1.setObjectName("checkBox_s1")
        self.horizontalLayout_11.addWidget(self.checkBox_s1)
        self.lineEdit_s1 = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_s1.sizePolicy().hasHeightForWidth())
        self.lineEdit_s1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_s1.setFont(font)
        self.lineEdit_s1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_s1.setObjectName("lineEdit_s1")
        self.horizontalLayout_11.addWidget(self.lineEdit_s1)
        self.gridLayout.addLayout(self.horizontalLayout_11, 7, 0, 1, 1)
        self.lineEdit_7f = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_7f.setFont(font)
        self.lineEdit_7f.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_7f.setObjectName("lineEdit_7f")
        self.gridLayout.addWidget(self.lineEdit_7f, 7, 1, 1, 1)
        self.lineEdit_7a = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_7a.setFont(font)
        self.lineEdit_7a.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_7a.setObjectName("lineEdit_7a")
        self.gridLayout.addWidget(self.lineEdit_7a, 7, 2, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.checkBox_s2 = QtWidgets.QCheckBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_s2.sizePolicy().hasHeightForWidth())
        self.checkBox_s2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_s2.setFont(font)
        self.checkBox_s2.setObjectName("checkBox_s2")
        self.horizontalLayout_10.addWidget(self.checkBox_s2)
        self.lineEdit_s2 = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_s2.sizePolicy().hasHeightForWidth())
        self.lineEdit_s2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_s2.setFont(font)
        self.lineEdit_s2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_s2.setObjectName("lineEdit_s2")
        self.horizontalLayout_10.addWidget(self.lineEdit_s2)
        self.gridLayout.addLayout(self.horizontalLayout_10, 8, 0, 1, 1)
        self.lineEdit_8f = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_8f.setFont(font)
        self.lineEdit_8f.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_8f.setObjectName("lineEdit_8f")
        self.gridLayout.addWidget(self.lineEdit_8f, 8, 1, 1, 1)
        self.lineEdit_8a = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_8a.setFont(font)
        self.lineEdit_8a.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_8a.setObjectName("lineEdit_8a")
        self.gridLayout.addWidget(self.lineEdit_8a, 8, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.pushButton_startcut = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_startcut.setFont(font)
        self.pushButton_startcut.setObjectName("pushButton_startcut")
        self.verticalLayout.addWidget(self.pushButton_startcut)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.pushButton_close = QtWidgets.QPushButton(Dialog_datacut)
        self.pushButton_close.setGeometry(QtCore.QRect(10, 410, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_close.setFont(font)
        self.pushButton_close.setObjectName("pushButton_close")
        self.pushButton_help = QtWidgets.QPushButton(Dialog_datacut)
        self.pushButton_help.setGeometry(QtCore.QRect(360, 430, 75, 23))
        self.pushButton_help.setObjectName("pushButton_help")

        self.retranslateUi(Dialog_datacut)
        self.pushButton_close.clicked.connect(Dialog_datacut.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog_datacut)

    def retranslateUi(self, Dialog_datacut):
        _translate = QtCore.QCoreApplication.translate
        Dialog_datacut.setWindowTitle(_translate("Dialog_datacut", "Dialog"))
        self.label.setText(_translate("Dialog_datacut", "   标签   "))
        self.label_2.setText(_translate("Dialog_datacut", "Mark前(秒)"))
        self.label_3.setText(_translate("Dialog_datacut", "Mark后(秒)"))
        self.checkBox_1.setText(_translate("Dialog_datacut", "Mark：1"))
        self.lineEdit_1f.setText(_translate("Dialog_datacut", "0"))
        self.lineEdit_1a.setText(_translate("Dialog_datacut", "0"))
        self.checkBox_2.setText(_translate("Dialog_datacut", "Mark：2"))
        self.lineEdit_2f.setText(_translate("Dialog_datacut", "0"))
        self.lineEdit_2a.setText(_translate("Dialog_datacut", "0"))
        self.checkBox_3.setText(_translate("Dialog_datacut", "Mark：3"))
        self.lineEdit_3f.setText(_translate("Dialog_datacut", "0"))
        self.lineEdit_3a.setText(_translate("Dialog_datacut", "0"))
        self.checkBox_4.setText(_translate("Dialog_datacut", "Mark：4"))
        self.lineEdit_4f.setText(_translate("Dialog_datacut", "0"))
        self.lineEdit_4a.setText(_translate("Dialog_datacut", "0"))
        self.checkBox_5.setText(_translate("Dialog_datacut", "Mark：5"))
        self.lineEdit_5f.setText(_translate("Dialog_datacut", "0"))
        self.lineEdit_5a.setText(_translate("Dialog_datacut", "0"))
        self.checkBox_6.setText(_translate("Dialog_datacut", "Mark：6"))
        self.lineEdit_6f.setText(_translate("Dialog_datacut", "0"))
        self.lineEdit_6a.setText(_translate("Dialog_datacut", "0"))
        self.checkBox_s1.setText(_translate("Dialog_datacut", "Mark："))
        self.lineEdit_7f.setText(_translate("Dialog_datacut", "0"))
        self.lineEdit_7a.setText(_translate("Dialog_datacut", "0"))
        self.checkBox_s2.setText(_translate("Dialog_datacut", "Mark："))
        self.lineEdit_8f.setText(_translate("Dialog_datacut", "0"))
        self.lineEdit_8a.setText(_translate("Dialog_datacut", "0"))
        self.pushButton_startcut.setText(_translate("Dialog_datacut", "开始分割"))
        self.pushButton_close.setText(_translate("Dialog_datacut", "关闭"))
        self.pushButton_help.setText(_translate("Dialog_datacut", "帮助"))
