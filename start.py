# -*- coding: utf-8 -*-

"""
@author: Bu Shaofeng
@software: PyCharm
@file: start.py
@time: 2022-03-21 19:48
////////////////////////////////////////////////////////////////////
//                          _ooOoo_                               //
//                         o8888888o                              //
//                         88" . "88                              //
//                         (| ^_^ |)                              //
//                         O\  =  /O                              //
//                      ____/`---'\____                           //
//                    .'  \\|     |//  `.                         //
//                   /  \\|||  :  |||//  \                        //
//                  /  _||||| -:- |||||-  \                       //
//                  |   | \\\  -  /// |   |                       //
//                  | \_|  ''\---/''  |   |                       //
//                  \  .-\__  `-`  ___/-. /                       //
//                ___`. .'  /--.--\  `. . ___                     //
//              ."" '<  `.___\_<|>_/___.'  >'"".                  //
//            | | :  `- \`.;`\ _ /`;.`/ - ` : | |                 //
//            \  \ `-.   \_ __\ /__ _/   .-` /  /                 //
//      ========`-.____`-.___\_____/___.-`____.-'========         //
//                           `=---='                              //
//      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^        //
//             佛祖保佑       永无BUG     永不修改                    //
////////////////////////////////////////////////////////////////////
"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from myedit import Ui_MainWindow
from lexical_analysis2 import rec
from rec import error
from autolex2 import auto
from recuisive import recuisive
from Assembly import asm
from QCodeEditor import QCodeEditor
class Start(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # QtCore.QObject.connect(self.ui.button_open,QtCore.SIGNAL("clicked()"),self.file_dialog)
        # QtCore.QObject.connect(self.ui.button_save,QtCore.SIGNAL("clicked()"),self.file_save)
        self.ui.actionopen.triggered.connect(self.__openFile)
        self.ui.actionsave.triggered.connect(self.__saveFile)
        self.ui.actionnew.triggered.connect(self.__newFile)
        self.ui.actionsaveas.triggered.connect(self.__saveasFile)
        self.ui.pushButton.clicked.connect(self.__cifafenxi)
        self.ui.pushButton_4.clicked.connect(self.__autolex)
        self.ui.pushButton_2.clicked.connect(self.__yufa)
        self.ui.pushButton_5.clicked.connect(self.__run)
        self.ui.pushButton_6.clicked.connect(self.__asm)
        self.tabindex = -1
        self.ui.tabWidget.setTabsClosable(True)
        self.ui.tabWidget.tabCloseRequested.connect(self.close_tab)
        self.end_res=''
    def runner1(self):
        va = {}
        for i in range(10000):
            va[str(i)] = i
            va[i] = i

        s = self.rr.GEN
        index=0
        self.rr.gencode('sys','','','')
        while True:
            if s[index].op == 'sys' or index == len(s)-1:
                break
            elif s[index].op == 'call' and s[index].arg1 == 'read':
                # tmp = input('input')
                i, okPressed = QInputDialog.getInt(self,"Get integer", "Percentage:", 28, 0, 100, 1)
                va[s[index].result] = i
            elif s[index].op == 'call' and s[index].arg1 == 'write':
                # print('result',va[s[index].result])
                self.end_res+=str(va[s[index].result])+'\n'
            elif s[index].op == '+':
                va[s[index].result] = int(va[s[index].arg1]) + int(va[s[index].arg2])
            elif s[index].op == '-':
                va[s[index].result] = int(va[s[index].arg1]) - int(va[s[index].arg2])
            elif s[index].op == '*':
                va[s[index].result] = int(va[s[index].arg1]) * int(va[s[index].arg2])
            elif s[index].op == '/':
                va[s[index].result] = int(va[s[index].arg1]) / int(va[s[index].arg2])
            elif s[index].op == '%':
                va[s[index].result] = int(va[s[index].arg1]) % int(va[s[index].arg2])
            elif s[index].op == '=':
                va[s[index].result] = int(va[s[index].arg1])

            elif s[index].op[0] == 'j':
                if len(s[index].op) == 1:
                    index = int(s[index].result)-2

                elif s[index].op[1] == '>':
                    if int(va[s[index].arg1])>int(va[s[index].arg2]):
                        index = int(s[index].result)-2
                elif s[index].op[1] == '<':
                    if int(va[s[index].arg1])<int(va[s[index].arg2]):
                        index = int(s[index].result)-2
                elif s[index].op[1:] == '==':
                    if int(va[s[index].arg1])==int(va[s[index].arg2]):
                        index = int(s[index].result)-2
            index = index+1
    def __run(self):
        self.runner1()
        self.ui.textEdit_3.setPlainText(self.end_res)
    def __asm(self):

        aa = asm(self.rr.GEN)
        aa.assembly()
        self.asmcode=''
        for i in aa.asm:
            print(i)
            self.asmcode+=i+'\n'
        self.ui.textEdit_2.setPlainText(self.asmcode)
    def __yufa(self):
        self.gen = ''
        self.rr = recuisive()
        self.rr.s = self.rr.convert(self.result)
        self.rr.dot.node(str(self.rr.id), str(self.rr.start), fontname="FZFangSong-Z02")
        self.rr.id = self.rr.id + 1
        self.rr.analy(self.rr.start)
        self.rr.dot.view()
        for i in self.rr.valist:
            print(i.name, i.value, i.type)
        for i in self.rr.funlist:
            print(i.name, i.type)
        for i in self.rr.GEN:
            self.gen+=str(i.op)+'\t'+str(i.arg1)+'\t'+str(i.arg2)+'\t'+str(i.result)+'\n'
        print(self.gen)
        self.ui.textEdit_2.setPlainText(self.gen)

    def __autolex(self):
        if self.tabindex<0:
            return
        tmp=self.ui.textEdit[self.tabindex].toPlainText()
        aa = auto()
        self.result,error_text = aa.rec(tmp)
        self.ui.textEdit_2.setPlainText(self.result)
        self.ui.textEdit_3.setPlainText(error_text)
        # aa = auto()
        # result = aa.rec(tmp)
        # self.ui.textEdit_2.setPlainText(result)
    def __cifafenxi(self):
        if self.tabindex<0:
            return
        tmp=self.ui.textEdit[self.tabindex].toPlainText()
        print(rec.recog(rec,tmp))
        result,error_text = rec.recog(rec,tmp)
        self.ui.textEdit_2.setPlainText(result)
        self.ui.textEdit_3.setPlainText(error_text)
        # aa = auto()
        # result = aa.rec(tmp)
        # self.ui.textEdit_2.setPlainText(result)




    def __newFile(self):
        self.tabindex = self.tabindex + 1
        self.filename = ["未命名"]
        self.ui.tab.append(QtWidgets.QWidget())

        self.ui.gridLayout1.append(QtWidgets.QGridLayout(self.ui.tab[self.tabindex]))
        self.ui.textEdit.append(QCodeEditor(self.ui.tab[self.tabindex]))

        self.ui.gridLayout1[self.tabindex].addWidget(self.ui.textEdit[self.tabindex], 0, 0, 1, 1)
        self.ui.tabWidget.addTab(self.ui.tab[self.tabindex], "")


        self.ui.textEdit[self.tabindex].setPlainText("")
        self.ui.tabWidget.setTabText(self.tabindex, self.filename[0].split('/')[-1])
        self.ui.tabWidget.setCurrentIndex(self.tabindex)
        print(self.tabindex, len(self.ui.textEdit), len(self.ui.gridLayout1))

    def __openFile(self):  # 打开文件操作
        # fd = QtGui.QFileDialog(self)

        self.filename = QFileDialog.getOpenFileName()
        if self.filename[0]=="":
            return
        print(self.filename)
        try:
            text = open(self.filename[0]).read()
            self.tabindex = self.tabindex + 1
            self.ui.tab.append(QtWidgets.QWidget())
            # self.ui.tab[self.tabindex] =
            # self.ui.tab[self.tabindex].setObjectName("tab")
            # self.ui.gridLayout1[self.tabindex]= self.ui.QtWidgets.QGridLayout(self.ui.tab[self.tabindex])
            self.ui.gridLayout1.append(QtWidgets.QGridLayout(self.ui.tab[self.tabindex]))
            # self.gridLayout_3.setObjectName("gridLayout_3")
            # self.ui.textEdit[self.tabindex] = self.ui.QCodeEditor(self.ui.tab[self.tabindex])
            self.ui.textEdit.append(QCodeEditor(self.ui.tab[self.tabindex]))
            # self.textEdit.setMinimumSize(QtCore.QSize(200, 0))
            # self.textEdit.setObjectName("textEdit")
            self.ui.gridLayout1[self.tabindex].addWidget(self.ui.textEdit[self.tabindex], 0, 0, 1, 1)
            self.ui.tabWidget.addTab(self.ui.tab[self.tabindex], "")
            # self.ui.tabWidget.setTabsClosable(True)
            # self.ui.tabWidget.tabCloseRequested.connect(self.close_tab)
            self.ui.tabWidget.setCurrentIndex(self.tabindex)

            self.ui.textEdit[self.tabindex].setPlainText(text)
            self.ui.tabWidget.setTabText(self.tabindex, self.filename[0].split('/')[-1])
            print(self.tabindex, self.ui.tabWidget.currentIndex())
        except:
            reply = QtWidgets.QMessageBox.about(self,'提示','   打开失败      ')




    def __saveasFile(self):
        self.filename =QFileDialog.getSaveFileName()
        file = open(self.filename[0], 'w')
        file.write(self.ui.textEdit[self.tabindex].toPlainText())
        reply = QtWidgets.QMessageBox.about(self, '提示', '   已保存      ')
        self.ui.tabWidget.setTabText(self.tabindex, self.filename[0].split('/')[-1])
        file.close()
    def __saveFile(self):   #保存文件
        if (self.filename == ["未命名"]):
            self.__saveasFile()
            return
        file = open(self.filename[0],'w')
        file.write(self.ui.textEdit[self.tabindex].toPlainText())
        reply = QtWidgets.QMessageBox.about(self,'提示','   已保存      ')
        file.close()
    def close_tab(self,index):
        print(self.ui.gridLayout1)

        # del self.ui.textEdit[index]
        # del self.ui.gridLayout1[index]
        self.ui.tabWidget.removeTab(index)

        # self.tabindex = self.tabindex - 1
        print(self.tabindex, len(self.ui.textEdit), len(self.ui.gridLayout1))




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Start()
    MainWindow.show()
    sys.exit(app.exec_())