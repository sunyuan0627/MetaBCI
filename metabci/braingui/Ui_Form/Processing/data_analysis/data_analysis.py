# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'data_analysis.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_data_analysis(object):
    def setupUi(self, Dialog_data_analysis):
        Dialog_data_analysis.setObjectName("Dialog_data_analysis")
        Dialog_data_analysis.resize(920, 708)
        self.gridLayout = QtWidgets.QGridLayout(Dialog_data_analysis)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog_data_analysis)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_time_analysis_loaddata = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_time_analysis_loaddata.setObjectName("pushButton_time_analysis_loaddata")
        self.verticalLayout.addWidget(self.pushButton_time_analysis_loaddata)
        self.pushButton_time_analysis_trial_superimposing = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_time_analysis_trial_superimposing.setObjectName("pushButton_time_analysis_trial_superimposing")
        self.verticalLayout.addWidget(self.pushButton_time_analysis_trial_superimposing)
        self.pushButton_time_analysis_signal_average_amplitude = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_time_analysis_signal_average_amplitude.setObjectName("pushButton_time_analysis_signal_average_amplitude")
        self.verticalLayout.addWidget(self.pushButton_time_analysis_signal_average_amplitude)
        self.pushButton_time_analysis_signal_average_amplitude_lurk = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_time_analysis_signal_average_amplitude_lurk.setObjectName("pushButton_time_analysis_signal_average_amplitude_lurk")
        self.verticalLayout.addWidget(self.pushButton_time_analysis_signal_average_amplitude_lurk)
        self.pushButton_channel_index_position_get = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_channel_index_position_get.setObjectName("pushButton_channel_index_position_get")
        self.verticalLayout.addWidget(self.pushButton_channel_index_position_get)
        self.pushButton_peak_amplitude = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_peak_amplitude.setObjectName("pushButton_peak_amplitude")
        self.verticalLayout.addWidget(self.pushButton_peak_amplitude)
        self.pushButton_peak_amplitude_lurk = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_peak_amplitude_lurk.setObjectName("pushButton_peak_amplitude_lurk")
        self.verticalLayout.addWidget(self.pushButton_peak_amplitude_lurk)
        self.pushButton_onlydata_time_plot = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_onlydata_time_plot.setObjectName("pushButton_onlydata_time_plot")
        self.verticalLayout.addWidget(self.pushButton_onlydata_time_plot)
        self.pushButton_muldata_time_plot = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_muldata_time_plot.setObjectName("pushButton_muldata_time_plot")
        self.verticalLayout.addWidget(self.pushButton_muldata_time_plot)
        self.pushButton_time_braintopomap_plot = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_time_braintopomap_plot.setObjectName("pushButton_time_braintopomap_plot")
        self.verticalLayout.addWidget(self.pushButton_time_braintopomap_plot)
        self.pushButton_time_analysis_output_data = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_time_analysis_output_data.setObjectName("pushButton_time_analysis_output_data")
        self.verticalLayout.addWidget(self.pushButton_time_analysis_output_data)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.textEdit_time = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_time.setObjectName("textEdit_time")
        self.verticalLayout_2.addWidget(self.textEdit_time)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog_data_analysis)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_frequent_analysis_load = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_frequent_analysis_load.setObjectName("pushButton_frequent_analysis_load")
        self.verticalLayout_3.addWidget(self.pushButton_frequent_analysis_load)
        self.pushButton_frequent_analysis_trial_superimposing = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_frequent_analysis_trial_superimposing.setObjectName("pushButton_frequent_analysis_trial_superimposing")
        self.verticalLayout_3.addWidget(self.pushButton_frequent_analysis_trial_superimposing)
        self.pushButton_signal_psd = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_signal_psd.setObjectName("pushButton_signal_psd")
        self.verticalLayout_3.addWidget(self.pushButton_signal_psd)
        self.pushButton_average_psd_specific = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_average_psd_specific.setObjectName("pushButton_average_psd_specific")
        self.verticalLayout_3.addWidget(self.pushButton_average_psd_specific)
        self.pushButton_signal_noise_ratio = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_signal_noise_ratio.setObjectName("pushButton_signal_noise_ratio")
        self.verticalLayout_3.addWidget(self.pushButton_signal_noise_ratio)
        self.pushButton_frequent_braintopomap_plot = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_frequent_braintopomap_plot.setObjectName("pushButton_frequent_braintopomap_plot")
        self.verticalLayout_3.addWidget(self.pushButton_frequent_braintopomap_plot)
        self.pushButton_frequent_analysis_output_data = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_frequent_analysis_output_data.setObjectName("pushButton_frequent_analysis_output_data")
        self.verticalLayout_3.addWidget(self.pushButton_frequent_analysis_output_data)
        spacerItem = QtWidgets.QSpacerItem(10, 130, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem)
        self.textEdit_frequent = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit_frequent.setObjectName("textEdit_frequent")
        self.verticalLayout_3.addWidget(self.textEdit_frequent)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog_data_analysis)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_time_frequent_load_data = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_time_frequent_load_data.setObjectName("pushButton_time_frequent_load_data")
        self.verticalLayout_4.addWidget(self.pushButton_time_frequent_load_data)
        self.pushButton_wavelet_transform_calculation = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_wavelet_transform_calculation.setObjectName("pushButton_wavelet_transform_calculation")
        self.verticalLayout_4.addWidget(self.pushButton_wavelet_transform_calculation)
        self.pushButton_short_term_fourior_transform_calculation = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_short_term_fourior_transform_calculation.setObjectName("pushButton_short_term_fourior_transform_calculation")
        self.verticalLayout_4.addWidget(self.pushButton_short_term_fourior_transform_calculation)
        self.pushButton_hilbert_transform_calculation = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_hilbert_transform_calculation.setObjectName("pushButton_hilbert_transform_calculation")
        self.verticalLayout_4.addWidget(self.pushButton_hilbert_transform_calculation)
        self.pushButton_time_frequent_braintopomap_plot = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_time_frequent_braintopomap_plot.setObjectName("pushButton_time_frequent_braintopomap_plot")
        self.verticalLayout_4.addWidget(self.pushButton_time_frequent_braintopomap_plot)
        self.pushButton_time_frequent_output_data = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_time_frequent_output_data.setObjectName("pushButton_time_frequent_output_data")
        self.verticalLayout_4.addWidget(self.pushButton_time_frequent_output_data)
        spacerItem1 = QtWidgets.QSpacerItem(10, 165, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem1)
        self.textEdit_time_frequent = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit_time_frequent.setObjectName("textEdit_time_frequent")
        self.verticalLayout_4.addWidget(self.textEdit_time_frequent)
        self.gridLayout_4.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox_3)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog_data_analysis)
        QtCore.QMetaObject.connectSlotsByName(Dialog_data_analysis)

    def retranslateUi(self, Dialog_data_analysis):
        _translate = QtCore.QCoreApplication.translate
        Dialog_data_analysis.setWindowTitle(_translate("Dialog_data_analysis", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog_data_analysis", "时域分析"))
        self.pushButton_time_analysis_loaddata.setText(_translate("Dialog_data_analysis", "导入数据"))
        self.pushButton_time_analysis_trial_superimposing.setText(_translate("Dialog_data_analysis", "试次叠加"))
        self.pushButton_time_analysis_signal_average_amplitude.setText(_translate("Dialog_data_analysis", "信号平均振幅测量"))
        self.pushButton_time_analysis_signal_average_amplitude_lurk.setText(_translate("Dialog_data_analysis", "平均振幅潜伏期测量"))
        self.pushButton_channel_index_position_get.setText(_translate("Dialog_data_analysis", "导联索引位置获取"))
        self.pushButton_peak_amplitude.setText(_translate("Dialog_data_analysis", "信号峰振幅测量"))
        self.pushButton_peak_amplitude_lurk.setText(_translate("Dialog_data_analysis", "峰振幅潜伏期测量"))
        self.pushButton_onlydata_time_plot.setText(_translate("Dialog_data_analysis", "单试次时域波形绘制"))
        self.pushButton_muldata_time_plot.setText(_translate("Dialog_data_analysis", "多试次时域波形绘制"))
        self.pushButton_time_braintopomap_plot.setText(_translate("Dialog_data_analysis", "时域脑地形图绘制"))
        self.pushButton_time_analysis_output_data.setText(_translate("Dialog_data_analysis", "导出数据"))
        self.groupBox_2.setTitle(_translate("Dialog_data_analysis", "频域分析"))
        self.pushButton_frequent_analysis_load.setText(_translate("Dialog_data_analysis", "导入数据"))
        self.pushButton_frequent_analysis_trial_superimposing.setText(_translate("Dialog_data_analysis", "试次叠加"))
        self.pushButton_signal_psd.setText(_translate("Dialog_data_analysis", "信号功率谱计算"))
        self.pushButton_average_psd_specific.setText(_translate("Dialog_data_analysis", "指定频带范围功率谱均值计算"))
        self.pushButton_signal_noise_ratio.setText(_translate("Dialog_data_analysis", "信号信噪比计算"))
        self.pushButton_frequent_braintopomap_plot.setText(_translate("Dialog_data_analysis", "频域脑地形图绘制"))
        self.pushButton_frequent_analysis_output_data.setText(_translate("Dialog_data_analysis", "导出数据"))
        self.groupBox_3.setTitle(_translate("Dialog_data_analysis", "时频分析"))
        self.pushButton_time_frequent_load_data.setText(_translate("Dialog_data_analysis", "导入数据"))
        self.pushButton_wavelet_transform_calculation.setText(_translate("Dialog_data_analysis", "小波变换计算"))
        self.pushButton_short_term_fourior_transform_calculation.setText(_translate("Dialog_data_analysis", "短时傅里叶变换计算"))
        self.pushButton_hilbert_transform_calculation.setText(_translate("Dialog_data_analysis", "希尔伯特变换计算"))
        self.pushButton_time_frequent_braintopomap_plot.setText(_translate("Dialog_data_analysis", "时频域脑地形图绘制"))
        self.pushButton_time_frequent_output_data.setText(_translate("Dialog_data_analysis", "导出数据"))

