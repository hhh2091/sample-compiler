# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NFA_DFA_MFA.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from itertools import combinations
from graphviz import Digraph
from ToNFA import Stack
import ToNFA
from NFAtoDFA import Nfa
from NFAtoDFA import nfatodfa
from PyQt5 import QtCore, QtGui, QtWidgets
import DFAtoMFA
class Ui_Form(object):
    def __init__(self):
        self.re = ''
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1100, 801)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(60, 40, 831, 51))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(50, 130, 301, 591))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(396, 140, 271, 581))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_4.setGeometry(QtCore.QRect(730, 140, 311, 581))
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(920, 50, 112, 34))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 740, 112, 34))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(480, 740, 112, 34))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(870, 750, 112, 34))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton.clicked.connect(self.check)
        self.pushButton_2.clicked.connect(self.nfa)
        self.pushButton_3.clicked.connect(self.dfa)
        self.pushButton_4.clicked.connect(self.mfa)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "确定"))
        self.pushButton_2.setText(_translate("Form", "NFA"))
        self.pushButton_3.setText(_translate("Form", "DFA"))
        self.pushButton_4.setText(_translate("Form", "MFA"))


    def nfa(self):
        text = ''
        s = ToNFA.add_sign(self.re)
        self.sss = ToNFA.in2post(s)
        self.a, self.b, self.c, self.end = ToNFA.toNFA(self.sss)
        for i in self.c:
            text = text+str(i)+'\n'
        self.plainTextEdit_2.setPlainText(text)

    def dfa(self):
        t = ''
        n = Nfa(self.a, self.b, self.c)
        self.d, self.accepted, self.startlist = nfatodfa(n, self.sss, self.end)
        for i in self.d:
            t = t+str(i)+'\n'
        self.plainTextEdit_3.setPlainText(t)
    def mfa(self):
        try:
            t=''
            move = ['a', 'b']
            dfa = DFAtoMFA.convert(self.d)
            self.ll = DFAtoMFA.mindfa(dfa, self.startlist, self.accepted, move)

            l=DFAtoMFA.draw(self.ll, dfa, move)
            for i in l:
                t = t+str(i)+'\n'
            self.plainTextEdit_4.setPlainText(t)
        except:
            t = ''
            n = Nfa(self.a, self.b, self.c)
            self.d, self.accepted, self.startlist = nfatodfa(n, self.sss, self.end)
            for i in self.d:
                t = t + str(i) + '\n'
            self.plainTextEdit_4.setPlainText(t)
    def check(self):
        self.re = self.plainTextEdit.toPlainText()
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
import sys
if __name__ == "__main__":
    app = QApplication(sys.argv)
    nfa_widget = QWidget()
    nfa_window = Ui_Form()
    nfa_window.setupUi(nfa_widget)
    nfa_widget.show()
    sys.exit(app.exec_())