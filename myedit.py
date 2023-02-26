# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
from QCodeEditor import QCodeEditor
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.textEdit_3 = QCodeEditor(self.centralwidget)
        self.textEdit_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.textEdit_3.setObjectName("textEdit_3")
        self.gridLayout.addWidget(self.textEdit_3, 2, 2, 1, 1)

        self.textEdit_2 = QCodeEditor(self.centralwidget)
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout.addWidget(self.textEdit_2, 1, 2, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")


        self.tab = []
        self.gridLayout1 = []
        self.textEdit = []
        # self.tab = QtWidgets.QWidget()
        # self.tab.setObjectName("tab")
        # self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        # self.gridLayout_3.setObjectName("gridLayout_3")
        # self.textEdit = QCodeEditor(self.tab)
        # self.textEdit.setMinimumSize(QtCore.QSize(200, 0))
        # self.textEdit.setObjectName("textEdit")
        # self.gridLayout_3.addWidget(self.textEdit, 0, 0, 1, 1)
        # self.tabWidget.addTab(self.tab, "")
        #



        # self.tab_2 = QtWidgets.QWidget()
        # self.tab_2.setObjectName("tab_2")
        # self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2)
        # self.gridLayout_2.setObjectName("gridLayout_2")
        # self.plainTextEdit_4 = QCodeEditor(self.tab_2)
        # self.plainTextEdit_4.setMinimumSize(QtCore.QSize(200, 0))
        # self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        # self.gridLayout_2.addWidget(self.plainTextEdit_4, 0, 0, 1, 1)
        # self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 1, 0, 2, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setMaximumSize(QtCore.QSize(16777215, 30))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 825, 28))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 99, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 0, 99, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 0, 99, 28))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_4.setGeometry(QtCore.QRect(330, 0, 99, 28))
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_5.setGeometry(QtCore.QRect(440, 0, 99, 28))
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_6 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_6.setGeometry(QtCore.QRect(550, 0, 99, 28))
        self.pushButton_6.setObjectName("pushButton_6")


        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 849, 26))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        self.menuedit = QtWidgets.QMenu(self.menubar)
        self.menuedit.setObjectName("menuedit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionopen = QtWidgets.QAction(MainWindow)
        self.actionopen.setObjectName("actionopen")
        self.actionnew = QtWidgets.QAction(MainWindow)
        self.actionnew.setObjectName("actionnew")
        self.actionsave = QtWidgets.QAction(MainWindow)
        self.actionsave.setObjectName("actionsave")
        self.actionsaveas = QtWidgets.QAction(MainWindow)
        self.actionsaveas.setObjectName("actionsaveas")
        self.actioncopy = QtWidgets.QAction(MainWindow)
        self.actioncopy.setObjectName("actioncopy")
        self.actionpaste = QtWidgets.QAction(MainWindow)
        self.actionpaste.setObjectName("actionpaste")
        self.menufile.addAction(self.actionopen)
        self.menufile.addAction(self.actionnew)
        self.menufile.addAction(self.actionsave)
        self.menufile.addAction(self.actionsaveas)
        self.menuedit.addAction(self.actioncopy)
        self.menuedit.addAction(self.actionpaste)
        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuedit.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        # self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        # self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.pushButton.setText(_translate("MainWindow", "词法分析"))
        self.pushButton_2.setText(_translate("MainWindow", "语法语义code"))
        self.pushButton_3.setText(_translate("MainWindow", "代码优化"))
        self.pushButton_4.setText(_translate("MainWindow", "自动词法分析"))
        self.pushButton_5.setText(_translate("MainWindow", "run"))
        self.pushButton_6.setText(_translate("MainWindow", "asm"))
        self.menufile.setTitle(_translate("MainWindow", "file"))
        self.menuedit.setTitle(_translate("MainWindow", "edit"))
        self.actionopen.setText(_translate("MainWindow", "open"))
        self.actionnew.setText(_translate("MainWindow", "new"))
        self.actionsave.setText(_translate("MainWindow", "save"))
        self.actionsaveas.setText(_translate("MainWindow", "save as"))
        self.actioncopy.setText(_translate("MainWindow", "copy"))
        self.actionpaste.setText(_translate("MainWindow", "paste"))

