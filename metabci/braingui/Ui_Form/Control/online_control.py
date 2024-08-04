# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'online_control.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_online_Form(object):
    def setupUi(self, online_Form):
        online_Form.setObjectName("online_Form")
        online_Form.resize(547, 507)
        self.pushButton_back = QtWidgets.QPushButton(online_Form)
        self.pushButton_back.setGeometry(QtCore.QRect(10, 450, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_back.setFont(font)
        self.pushButton_back.setObjectName("pushButton_back")
        self.pushButton_help = QtWidgets.QPushButton(online_Form)
        self.pushButton_help.setGeometry(QtCore.QRect(450, 470, 93, 28))
        self.pushButton_help.setObjectName("pushButton_help")
        self.layoutWidget = QtWidgets.QWidget(online_Form)
        self.layoutWidget.setGeometry(QtCore.QRect(12, 12, 521, 411))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_gettype = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_gettype.setFont(font)
        self.label_gettype.setObjectName("label_gettype")
        self.horizontalLayout_2.addWidget(self.label_gettype)
        self.comboBox_gettype = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.comboBox_gettype.setFont(font)
        self.comboBox_gettype.setObjectName("comboBox_gettype")
        self.comboBox_gettype.addItem("")
        self.comboBox_gettype.addItem("")
        self.comboBox_gettype.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_gettype)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_robot_model = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_robot_model.setFont(font)
        self.label_robot_model.setObjectName("label_robot_model")
        self.horizontalLayout.addWidget(self.label_robot_model)
        self.comboBox_robot_model = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.comboBox_robot_model.setFont(font)
        self.comboBox_robot_model.setObjectName("comboBox_robot_model")
        self.comboBox_robot_model.addItem("")
        self.comboBox_robot_model.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_robot_model)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_paradigm_model = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_paradigm_model.setFont(font)
        self.label_paradigm_model.setObjectName("label_paradigm_model")
        self.horizontalLayout_3.addWidget(self.label_paradigm_model)
        self.comboBox_paradigm_model = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.comboBox_paradigm_model.setFont(font)
        self.comboBox_paradigm_model.setObjectName("comboBox_paradigm_model")
        self.comboBox_paradigm_model.addItem("")
        self.comboBox_paradigm_model.addItem("")
        self.comboBox_paradigm_model.addItem("")
        self.comboBox_paradigm_model.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_paradigm_model)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_connect_robot = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_connect_robot.setFont(font)
        self.pushButton_connect_robot.setObjectName("pushButton_connect_robot")
        self.gridLayout.addWidget(self.pushButton_connect_robot, 0, 0, 1, 1)
        self.pushButton_connect_get = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_connect_get.setFont(font)
        self.pushButton_connect_get.setObjectName("pushButton_connect_get")
        self.gridLayout.addWidget(self.pushButton_connect_get, 0, 1, 1, 1)
        self.pushButton_open_paradigm = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_open_paradigm.setFont(font)
        self.pushButton_open_paradigm.setObjectName("pushButton_open_paradigm")
        self.gridLayout.addWidget(self.pushButton_open_paradigm, 1, 0, 1, 1)
        self.pushButton_start_identify = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_start_identify.setFont(font)
        self.pushButton_start_identify.setObjectName("pushButton_start_identify")
        self.gridLayout.addWidget(self.pushButton_start_identify, 1, 1, 1, 1)
        self.textEdit_order = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit_order.setObjectName("textEdit_order")
        self.gridLayout.addWidget(self.textEdit_order, 2, 0, 1, 2)
        self.verticalLayout_3.addLayout(self.gridLayout)

        self.retranslateUi(online_Form)
        self.pushButton_back.clicked.connect(online_Form.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(online_Form)

    def retranslateUi(self, online_Form):
        _translate = QtCore.QCoreApplication.translate
        online_Form.setWindowTitle(_translate("online_Form", "Form"))
        self.pushButton_back.setText(_translate("online_Form", "返回"))
        self.pushButton_help.setText(_translate("online_Form", "帮助"))
        self.label_gettype.setText(_translate("online_Form", "采集设备类型："))
        self.comboBox_gettype.setItemText(0, _translate("online_Form", "采集设备"))
        self.comboBox_gettype.setItemText(1, _translate("online_Form", "W4多模态采集设备"))
        self.comboBox_gettype.setItemText(2, _translate("online_Form", "TGAM采集设备"))
        self.label_robot_model.setText(_translate("online_Form", "外骨骼类型："))
        self.comboBox_robot_model.setItemText(0, _translate("online_Form", "下肢外骨骼"))
        self.comboBox_robot_model.setItemText(1, _translate("online_Form", "上肢康复平台"))
        self.label_paradigm_model.setText(_translate("online_Form", "范式类型："))
        self.comboBox_paradigm_model.setItemText(0, _translate("online_Form", "下肢范式（MI）"))
        self.comboBox_paradigm_model.setItemText(1, _translate("online_Form", "上肢范式（MI）"))
        self.comboBox_paradigm_model.setItemText(2, _translate("online_Form", "SSVEP"))
        self.comboBox_paradigm_model.setItemText(3, _translate("online_Form", "注意力范式"))
        self.pushButton_connect_robot.setText(_translate("online_Form", "连接外骨骼"))
        self.pushButton_connect_get.setText(_translate("online_Form", "连接采集设备"))
        self.pushButton_open_paradigm.setText(_translate("online_Form", "开启范式"))
        self.pushButton_start_identify.setText(_translate("online_Form", "开始识别"))
