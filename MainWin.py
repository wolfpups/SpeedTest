# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 500)
        Form.setMinimumSize(QtCore.QSize(400, 500))
        Form.setMaximumSize(QtCore.QSize(400, 500))
        Form.setFocusPolicy(QtCore.Qt.StrongFocus)
        Form.setStyleSheet("background-color: rgb(11, 11, 27);\n"
"font: 75 12pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);")
        self.schoolName = QtWidgets.QLabel(Form)
        self.schoolName.setGeometry(QtCore.QRect(11, 36, 371, 21))
        self.schoolName.setObjectName("schoolName")
        self.startButton = QtWidgets.QPushButton(Form)
        self.startButton.setGeometry(QtCore.QRect(120, 420, 140, 50))
        self.startButton.setMaximumSize(QtCore.QSize(140, 50))
        self.startButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.startButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.startButton.setStyleSheet("border-image: url(:/pic/buttonBgm.png);")
        self.startButton.setFlat(False)
        self.startButton.setObjectName("startButton")
        self.clientIsp = QtWidgets.QLabel(Form)
        self.clientIsp.setGeometry(QtCore.QRect(150, 330, 240, 16))
        self.clientIsp.setMaximumSize(QtCore.QSize(240, 16))
        self.clientIsp.setObjectName("clientIsp")
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 110, 301, 98))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.download = QtWidgets.QLabel(self.gridLayoutWidget)
        self.download.setObjectName("download")
        self.gridLayout.addWidget(self.download, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.downloadUnit = QtWidgets.QLabel(self.gridLayoutWidget)
        self.downloadUnit.setObjectName("downloadUnit")
        self.gridLayout.addWidget(self.downloadUnit, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.upload = QtWidgets.QLabel(self.gridLayoutWidget)
        self.upload.setObjectName("upload")
        self.gridLayout.addWidget(self.upload, 1, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.uploadUnit = QtWidgets.QLabel(self.gridLayoutWidget)
        self.uploadUnit.setObjectName("uploadUnit")
        self.gridLayout.addWidget(self.uploadUnit, 2, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.pingUnit = QtWidgets.QLabel(self.gridLayoutWidget)
        self.pingUnit.setObjectName("pingUnit")
        self.gridLayout.addWidget(self.pingUnit, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setMaximumSize(QtCore.QSize(30, 30))
        self.graphicsView.setStyleSheet("background-image: url(:/pic/upload.png);")
        self.graphicsView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout.addWidget(self.graphicsView)
        self.uploadLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.uploadLabel.setObjectName("uploadLabel")
        self.horizontalLayout.addWidget(self.uploadLabel)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 2, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.gridLayoutWidget)
        self.graphicsView_2.setMaximumSize(QtCore.QSize(30, 30))
        self.graphicsView_2.setStyleSheet("background-image: url(:/pic/download.png);")
        self.graphicsView_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.horizontalLayout_2.addWidget(self.graphicsView_2)
        self.downloadLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.downloadLabel.setObjectName("downloadLabel")
        self.horizontalLayout_2.addWidget(self.downloadLabel)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.gridLayoutWidget)
        self.graphicsView_3.setMaximumSize(QtCore.QSize(30, 30))
        self.graphicsView_3.setStyleSheet("background-image: url(:/pic/ping.png);")
        self.graphicsView_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.graphicsView_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.horizontalLayout_3.addWidget(self.graphicsView_3)
        self.pingLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pingLabel.sizePolicy().hasHeightForWidth())
        self.pingLabel.setSizePolicy(sizePolicy)
        self.pingLabel.setMaximumSize(QtCore.QSize(70, 30))
        self.pingLabel.setStyleSheet("")
        self.pingLabel.setObjectName("pingLabel")
        self.horizontalLayout_3.addWidget(self.pingLabel)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.ping = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.ping.setFont(font)
        self.ping.setObjectName("ping")
        self.gridLayout.addWidget(self.ping, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(150, 250, 284, 61))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.gridLayoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.serverSponsor = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.serverSponsor.setMaximumSize(QtCore.QSize(240, 16))
        self.serverSponsor.setObjectName("serverSponsor")
        self.verticalLayout.addWidget(self.serverSponsor)
        self.serverName = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.serverName.setMaximumSize(QtCore.QSize(240, 16))
        self.serverName.setObjectName("serverName")
        self.verticalLayout.addWidget(self.serverName)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 250, 126, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.graphicsView_4 = QtWidgets.QGraphicsView(self.horizontalLayoutWidget)
        self.graphicsView_4.setMinimumSize(QtCore.QSize(55, 55))
        self.graphicsView_4.setMaximumSize(QtCore.QSize(55, 55))
        self.graphicsView_4.setStyleSheet("background-image: url(:/pic/sponsor.png);")
        self.graphicsView_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.horizontalLayout_4.addWidget(self.graphicsView_4)
        self.testNodeLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.testNodeLabel.setObjectName("testNodeLabel")
        self.horizontalLayout_4.addWidget(self.testNodeLabel)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 310, 127, 61))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.graphicsView_5 = QtWidgets.QGraphicsView(self.horizontalLayoutWidget_2)
        self.graphicsView_5.setMinimumSize(QtCore.QSize(55, 55))
        self.graphicsView_5.setMaximumSize(QtCore.QSize(54, 55))
        self.graphicsView_5.setStyleSheet("background-image: url(:/pic/isp.png);")
        self.graphicsView_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.graphicsView_5.setObjectName("graphicsView_5")
        self.horizontalLayout_5.addWidget(self.graphicsView_5)
        self.ispLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.ispLabel.setObjectName("ispLabel")
        self.horizontalLayout_5.addWidget(self.ispLabel)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.schoolName.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#9193a8;\">XX学校网络速度</span></p></body></html>"))
        self.startButton.setText(_translate("Form", "开始测速"))
        self.clientIsp.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">China Telecom Sichuan</span></p></body></html>"))
        self.download.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:18pt;\">87.22</span></p></body></html>"))
        self.downloadUnit.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#9193a8;\">兆/秒</span></p></body></html>"))
        self.upload.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:18pt;\">101.44</span></p></body></html>"))
        self.uploadUnit.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#9193a8;\">兆/秒</span></p></body></html>"))
        self.pingUnit.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#9193a8;\">毫秒</span></p></body></html>"))
        self.uploadLabel.setText(_translate("Form", "上传"))
        self.downloadLabel.setText(_translate("Form", "下载"))
        self.pingLabel.setText(_translate("Form", "PING"))
        self.ping.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:18pt;\">10</span></p></body></html>"))
        self.serverSponsor.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">China Mobile Group Sichuan Co.,Ltd.</span></p></body></html>"))
        self.serverName.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Chengdu</span></p></body></html>"))
        self.testNodeLabel.setText(_translate("Form", "节   点："))
        self.ispLabel.setText(_translate("Form", "运营商："))

import res_rc
