# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Paradigm_MI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimediaWidgets import QVideoWidget

class Ui_Form_MI(object):
    def setupUi(self, Form_MI):
        Form_MI.setObjectName("Form_MI")
        Form_MI.resize(1600, 1200)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form_MI)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.stackedWidget_MI = QtWidgets.QStackedWidget(Form_MI)
        self.stackedWidget_MI.setObjectName("stackedWidget_MI")
        self.page_begin = QtWidgets.QWidget()
        self.page_begin.setObjectName("page_begin")
        self.gridLayout = QtWidgets.QGridLayout(self.page_begin)
        self.gridLayout.setObjectName("gridLayout")
        self.label_begin = QtWidgets.QLabel(self.page_begin)
        font = QtGui.QFont()
        font.setPointSize(80)
        self.label_begin.setFont(font)
        self.label_begin.setAlignment(QtCore.Qt.AlignCenter)
        self.label_begin.setObjectName("label_begin")
        self.gridLayout.addWidget(self.label_begin, 0, 0, 1, 1)
        self.pushButton_start = QtWidgets.QPushButton(self.page_begin)
        self.pushButton_start.setGeometry(QtCore.QRect(20, 1150, 93, 28))
        self.pushButton_start.setObjectName("pushButton_start")
        self.stackedWidget_MI.addWidget(self.page_begin)
        self.page_openeye = QtWidgets.QWidget()
        self.page_openeye.setObjectName("page_openeye")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page_openeye)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_openeye = QtWidgets.QLabel(self.page_openeye)
        font = QtGui.QFont()
        font.setPointSize(100)
        self.label_openeye.setFont(font)
        self.label_openeye.setAlignment(QtCore.Qt.AlignCenter)
        self.label_openeye.setObjectName("label_openeye")
        self.gridLayout_5.addWidget(self.label_openeye, 0, 0, 1, 1)
        self.stackedWidget_MI.addWidget(self.page_openeye)
        self.page_closeeye = QtWidgets.QWidget()
        self.page_closeeye.setObjectName("page_closeeye")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page_closeeye)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_closeeye = QtWidgets.QLabel(self.page_closeeye)
        font = QtGui.QFont()
        font.setPointSize(100)
        self.label_closeeye.setFont(font)
        self.label_closeeye.setAlignment(QtCore.Qt.AlignCenter)
        self.label_closeeye.setObjectName("label_closeeye")
        self.gridLayout_6.addWidget(self.label_closeeye, 0, 0, 1, 1)
        self.stackedWidget_MI.addWidget(self.page_closeeye)
        self.page_wait = QtWidgets.QWidget()
        self.page_wait.setObjectName("page_wait")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.page_wait)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_wait = QtWidgets.QLabel(self.page_wait)
        font = QtGui.QFont()
        font.setPointSize(100)
        self.label_wait.setFont(font)
        self.label_wait.setAlignment(QtCore.Qt.AlignCenter)
        self.label_wait.setObjectName("label_wait")
        self.gridLayout_7.addWidget(self.label_wait, 0, 0, 1, 1)
        self.stackedWidget_MI.addWidget(self.page_wait)
        self.page_display = QtWidgets.QWidget()
        self.page_display.setObjectName("page_display")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.page_display)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.widget_display = QVideoWidget(self.page_display)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.widget_display.sizePolicy().hasHeightForWidth())
        self.widget_display.setSizePolicy(sizePolicy)
        self.widget_display.setObjectName("widget_display")
        self.gridLayout_8.addWidget(self.widget_display, 0, 0, 1, 1)
        self.label_display = QtWidgets.QLabel(self.page_display)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_display.sizePolicy().hasHeightForWidth())
        self.label_display.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(60)
        self.label_display.setFont(font)
        self.label_display.setAlignment(QtCore.Qt.AlignCenter)
        self.label_display.setObjectName("label_display")
        self.gridLayout_8.addWidget(self.label_display, 1, 0, 1, 1)
        self.stackedWidget_MI.addWidget(self.page_display)
        self.page_imagery = QtWidgets.QWidget()
        self.page_imagery.setObjectName("page_imagery")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_imagery)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_imagery_picture = QtWidgets.QLabel(self.page_imagery)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.label_imagery_picture.sizePolicy().hasHeightForWidth())
        self.label_imagery_picture.setSizePolicy(sizePolicy)
        self.label_imagery_picture.setText("")
        self.label_imagery_picture.setAlignment(QtCore.Qt.AlignCenter)
        self.label_imagery_picture.setObjectName("label_imagery_picture")
        self.gridLayout_3.addWidget(self.label_imagery_picture, 0, 0, 1, 1)
        self.label_imagery = QtWidgets.QLabel(self.page_imagery)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_imagery.sizePolicy().hasHeightForWidth())
        self.label_imagery.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(60)
        self.label_imagery.setFont(font)
        self.label_imagery.setAlignment(QtCore.Qt.AlignCenter)
        self.label_imagery.setObjectName("label_imagery")
        self.gridLayout_3.addWidget(self.label_imagery, 1, 0, 1, 1)
        self.stackedWidget_MI.addWidget(self.page_imagery)
        self.page_rest = QtWidgets.QWidget()
        self.page_rest.setObjectName("page_rest")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_rest)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_rest = QtWidgets.QLabel(self.page_rest)
        font = QtGui.QFont()
        font.setPointSize(100)
        self.label_rest.setFont(font)
        self.label_rest.setAlignment(QtCore.Qt.AlignCenter)
        self.label_rest.setObjectName("label_rest")
        self.gridLayout_4.addWidget(self.label_rest, 0, 0, 1, 1)
        self.stackedWidget_MI.addWidget(self.page_rest)
        self.page_end = QtWidgets.QWidget()
        self.page_end.setObjectName("page_end")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.page_end)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_end = QtWidgets.QLabel(self.page_end)
        font = QtGui.QFont()
        font.setPointSize(80)
        self.label_end.setFont(font)
        self.label_end.setAlignment(QtCore.Qt.AlignCenter)
        self.label_end.setObjectName("label_end")
        self.gridLayout_9.addWidget(self.label_end, 0, 0, 1, 1)
        self.pushButton_close = QtWidgets.QPushButton(self.page_end)
        self.pushButton_close.setGeometry(QtCore.QRect(1460, 1140, 93, 28))
        self.pushButton_close.setObjectName("pushButton_close")
        self.stackedWidget_MI.addWidget(self.page_end)
        self.gridLayout_2.addWidget(self.stackedWidget_MI, 0, 0, 1, 1)

        self.retranslateUi(Form_MI)
        self.stackedWidget_MI.setCurrentIndex(6)
        self.pushButton_close.clicked.connect(self.label_end.close)
        QtCore.QMetaObject.connectSlotsByName(Form_MI)

    def retranslateUi(self, Form_MI):
        _translate = QtCore.QCoreApplication.translate
        Form_MI.setWindowTitle(_translate("Form_MI", "Form"))
        self.label_begin.setText(_translate("Form_MI", "运动想象MI范式\n"
"按任意键5秒后开始范式"))
        self.pushButton_start.setText(_translate("Form_MI", "开始范式"))
        self.label_openeye.setText(_translate("Form_MI", "+\n"
"睁眼阶段"))
        self.label_closeeye.setText(_translate("Form_MI", "+\n"
"闭眼阶段"))
        self.label_wait.setText(_translate("Form_MI", "请睁眼"))
        self.label_display.setText(_translate("Form_MI", "动作展示阶段"))
        self.label_imagery.setText(_translate("Form_MI", "想象阶段"))
        self.label_rest.setText(_translate("Form_MI", "休息阶段"))
        self.label_end.setText(_translate("Form_MI", "实验结束\n"
"按Esc键关闭范式"))
        self.pushButton_close.setText(_translate("Form_MI", "关闭"))

