# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_gui.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1029, 497)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(800, 270, 211, 61))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(540, 270, 211, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 270, 211, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 270, 211, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(290, 0, 471, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(270, 360, 211, 61))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(540, 360, 211, 61))
        self.pushButton_6.setObjectName("pushButton_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1029, 26))
        self.menubar.setObjectName("menubar")
        self.menuAboutMe = QtWidgets.QMenu(self.menubar)
        self.menuAboutMe.setObjectName("menuAboutMe")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuAboutMe.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_4.setText(_translate("MainWindow", "开启视频检测(VideoDection)"))
        self.pushButton_3.setText(_translate("MainWindow", "开始检测物体(Detection)"))
        self.pushButton.setText(_translate("MainWindow", "开始训练(Train)"))
        self.pushButton_2.setText(_translate("MainWindow", "开始测试模型(Test)"))
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">声明</span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">本程序版权归“快活似神仙”团队所有</span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">如有雷同，纯属巧合</span></p></body></html>"))
        self.pushButton_5.setText(_translate("MainWindow", "视频抽帧(GetFrame)"))
        self.pushButton_6.setText(_translate("MainWindow", "开启摄像头"))
        self.menuAboutMe.setTitle(_translate("MainWindow", "AboutMe"))


# class MainWindow(QtWidgets, Ui_MainWindow):
#
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setupUi(self)
#         self.pushButton.clicked.connect(self.on_pushButton_clicked)
#
#     def openfile(self):
#         # openfile_name的值形如('F:/test.txt', '文本文档(*.txt)')
#         # 后续需要使用路径的时候需要取openfile_name[0]
#         openfile_name = QFileDialog.getOpenFileName(self, '选择文件', '', '文本文档(*.txt)')
#
#     def onOpen_new_window(self):
#         pass
#
#     def onStartDetection(self):
#         pass
#
#     def onOpencv_videoDetection(self):
#         pass
#
#     def onOpen_Camera(self):
#         pass
#
#         self.pushButton.clicked.connect(self.onOpen_new_window())  # 开始训练(Train)
#         self.pushButton_2.clicked.connect(self.onOpen_new_window())  # 开始测试模型(Test)
#         self.pushButton_3.clicked.connect(self.onStartDetection())  # 开始检测物体(Detection)
#         self.pushButton_4.clicked.connect(self.onOpencv_videoDetection())  # 开启视频检测(VideoDection)
#         self.pushButton_5.clicked.connect(self.onOpen_new_window)  # 视频抽帧(GetFrame)
#         self.pushButton_6.clicked.connect(self.onOpen_Camera())  # 开启摄像头


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Ui_MainWindow()
    win.show()
    sys.exit(app.exec_())
