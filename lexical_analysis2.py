# -*- coding: utf-8 -*-
"""
@author: Bu Shaofeng
@software: PyCharm
@file: Lexical_analysis.py
@time: 2022-03-23 17:17

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
//         佛祖保佑       永无BUG     永不修改                        //
//////////////////////////////////////////////////////////////////// 
"""

key_word = ['long', 'float', 'static', 'char', 'short', 'switch', 'int', 'const', 'if', 'then', 'else', 'for'
,'while', 'break', 'main']


operators = ['+', '-', '*', '/', ':', '&','<',  '>',  '=', ]

Delimiters =[';', '(', ')', '#', '{', '}', ',','[', ']', "'", '.', '"']

sign = ['+', '-', '*', '/', ':', ':=', '<', '<>', '<=', '>', '>=', '=', ';', '(', ')', '#', '==', '{', '}', ',',
'&', '[', ']', "'", '"']


_error = ['braces mismatching','parentheses mismatching','brackets mismatching',
          'expected unqualified-id before numeric constant','Numbers cannot start with zero','error','error',
         'error','error','error','error','error']

token = {}
token['+'] = 201
token['-'] = 202
token['*'] = 203
token['/'] = 204
token['='] = 205
token[':'] = 206
token['<'] = 207
token['>'] = 208
token['%'] = 209
token['&'] = 210
token['!'] = 211
token['('] = 212
token[')'] = 213
token['['] = 214
token[']'] = 215
token['{'] = 216
token['}'] = 217
token['#'] = 218
token['|'] = 219
token[','] = 220
token['"'] = 221
token['int'] = 101
token['char'] = 102
token['float'] = 103
token['return'] = 104
token['void'] = 105
token['if'] = 106
token['for'] = 107
token['while'] = 108
token['break'] = 109
token['continue'] = 110
token['do'] = 111
token['double'] = 112
token['main'] = 113
token['long'] = 114
token['then'] = 115
token['switch'] = 116
token['short'] = 117
token['include'] = 118
token['>='] = 131
token['>>'] = 132
token['=='] = 133
token['<='] = 134
token['<<'] = 135
class error:
    def __init__(self):
        self.row_index = 0
        self.error_code = -1
        self.col_index = 0

class rec():
    def __init__(self):
        self.index = 0
        self.result = []
        self.result1 = []
        self.string = ""
        self.row = 0
        self.row_index = 0
        self.col_index = 0
        self.error_code = []

    # 判断是否字符
    def IsLetter(self, Char):
        if ('a' <= Char <= 'z') or ('A' <= Char <= 'Z'):
            return True
        else:
            return False

    # 判断是否是数字
    def IsDigit(self, Char):
        if '9' >= Char >= '0':
            return True
        else:
            return False
    def IsDigit_without0(self, Char):
        if '9' >= Char >= '1':
            return True
        else:
            return False
    def Is_Octal(self, Char):
        if '7' >= Char >= '0':
            return True
        else:
            return False

    def Is_hexadecimal(self, Char):
            if '9' >= Char >= '0' or 'a' <= Char <= 'f' or 'A' <= Char <= 'F' :
                return True
            else:
                return False



    def pre_treatment(self, a):
        self.row = a.count('\n')
        print(self.row)
        string = a.replace('\t', ' ').replace('\r', ' ')
        string = string + ' '
        return string

    def Isend(self, a):
        if a == ' ' or (a in sign) or self.index == len(self.string) - 1 or a == '\n':
            return True
        else:
            return False


    def recog(self, string):
        res = ""
        self.string = self.pre_treatment(self, string)
        state = 0  # 空白
        self.index = 0
        self.error_code = []
        lenth = len(self.string)
        braces = 0  # 大括号
        parentheses = 0  # 小括号
        brackets = 0  # 方括号
        error_code = -1
        self.row_index = 0
        self.col_index = 0
        while self.index <= (lenth - 2):
            ii = self.index
            flag = 0  # 空白
            state = 0
            sflag = True
            while True:
                sflag = True
                if self.string[self.index] == '\n':
                    self.row_index = self.row_index+1
                    self.col_index = 0

                # 开始
                if state == 0 and sflag:
                    if self.IsLetter(self, self.string[self.index]):
                        state = 20
                    elif self.IsDigit_without0(self, self.string[self.index]):
                        state = 1
                    elif self.string[self.index] == '0':
                        state = 3

                    elif self.string[self.index] == '"':
                        state = 30
                    elif self.string[self.index] == '\'':
                        state = 31

                    elif self.string[self.index] == '/' and self.string[self.index + 1] == '/':
                        state = 40
                    elif self.string[self.index] == '/' and self.string[self.index + 1] == '*':
                        state = 41
                    elif self.Isend(self, self.string[self.index]):
                        state = -1
                        #other

                elif state == 1 and sflag:
                    if self.IsDigit(self,self.string[self.index]):
                        state = 1
                    elif self.string[self.index] == '.':
                        state  = 8
                    elif self.string[self.index] == 'e' or self.string[self.index] == 'E':
                        state = 10

                    elif self.string[self.index] == '"':
                        state = 30
                    elif self.string[self.index] == '\'':
                        state = 31

                    elif self.string[self.index] == '/' and self.string[self.index + 1] == '/':
                        state = 40
                    elif self.string[self.index] == '/' and self.string[self.index + 1] == '*':
                        state = 41

                    elif self.Isend(self, self.string[self.index]):
                        state = -1
                        flag = 1  # 整数
                         
                    else:
                        state = -1
                        flag = 1
                        e = error()
                        e.error_code = 4  # 不能识别
                        e.row_index = self.row_index
                        e.col_index = self.col_index
                        self.error_code.append(e)

                elif state == 3 and sflag:
                    if self.string[self.index] == '.':
                        state  = 8
                    elif self.Is_Octal(self,self.string[self.index]):
                        state = 2
                    elif self.string[self.index] == 'x' or self.string[self.index] == 'X':
                        state = 5
                    elif self.Isend(self, self.string[self.index]):
                        state = -1
                        flag = 1#整数

                    elif self.string[self.index] == '"':
                        state = 30
                    elif self.string[self.index] == '\'':
                        state = 31
                    elif self.string[self.index] == '/' and self.string[self.index + 1] == '/':
                        state = 40
                    elif self.string[self.index] == '/' and self.string[self.index + 1] == '*':
                        state = 41

                    else:
                        state = -1
                        flag = 1
                        e = error()
                        e.error_code = 4  # 不能识别
                        e.row_index = self.row_index
                        e.col_index = self.col_index
                        self.error_code.append(e)

                elif state == 5 and sflag:
                    if self.Is_hexadecimal(self,self.string[self.index]):
                        state = 6

                    else:
                        state = -1
                        flag = 1
                        e = error()
                        e.error_code = 5  # 不能识别
                        e.row_index = self.row_index
                        e.col_index = self.col_index
                        self.error_code.append(e)


                elif state == 6 and sflag:
                    if self.Is_hexadecimal(self, self.string[self.index]):
                        state = 6
                    elif self.Isend(self,self.string[self.index]):
                        state = -1
                        flag = 4#16进制

                    elif self.string[self.index] == '"':
                        state = 30
                    elif self.string[self.index] == '\'':
                        state = 31

                    elif self.string[self.index] == '/' and self.string[self.index + 1] == '/':
                        state = 40
                    elif self.string[self.index] == '/' and self.string[self.index + 1] == '*':
                        state = 41
                    else:
                        state = -1
                        flag = 1
                        e = error()
                        e.error_code = 5  # 不能识别
                        e.row_index = self.row_index
                        e.col_index = self.col_index
                        self.error_code.append(e)

                elif state == 2 and sflag:
                    if self.Is_Octal(self, self.string[self.index]):
                        state = 2
                    elif self.Isend(self,self.string[self.index]):
                        state = -1
                        flag = 3#8进制

                    elif self.string[self.index] == '"':
                        state = 30
                    elif self.string[self.index] == '\'':
                        state = 31

                    elif self.string[self.index] == '/' and self.string[self.index + 1] == '/':
                        state = 40
                    elif self.string[self.index] == '/' and self.string[self.index + 1] == '*':
                        state = 41
                    else:
                        state = -1
                        flag = 1
                        e = error()
                        e.error_code = 5  # 不能识别
                        e.row_index = self.row_index
                        e.col_index = self.col_index
                        self.error_code.append(e)

                elif state == 8 and sflag:#小数点
                    if self.IsDigit(self,self.string[self.index]):
                        state = 9
                    else:
                        state = -1
                        flag = 1
                        e = error()
                        e.error_code = 6  # 不能识别（小数点）
                        e.row_index = self.row_index
                        e.col_index = self.col_index
                        self.error_code.append(e)

                elif state == 9 and sflag:
                    if self.IsDigit(self,self.string[self.index]):
                        state = 9
                    elif self.Isend(self,self.string[self.index]):
                        state = -1
                        flag = 2#小数
                    elif self.string[self.index] == 'e' or self.string[self.index] == 'E':
                        state = 10

                    elif self.string[self.index] == '"':
                        state = 30
                    elif self.string[self.index] == '\'':
                        state = 31

                    elif self.string[self.index] == '/' and self.string[self.index + 1] == '/':
                        state = 40
                    elif self.string[self.index] == '/' and self.string[self.index + 1] == '*':
                        state = 41
                         
                    else:
                        state = -1
                        flag = 1
                        e = error()
                        e.error_code = 6  # 不能识别（小数点）
                        e.row_index = self.row_index
                        e.col_index = self.col_index
                        self.error_code.append(e)

                elif state == 10 and sflag:
                    if self.string[self.index] == '+' or self.string[self.index] == '-':
                        state = 11
                    elif self.IsDigit(self,self.string[self.index]):
                        state = 12
                    else:
                        state = -1
                        flag = 1
                        e = error()
                        e.error_code = 6  # 不能识别（小数点）
                        e.row_index = self.row_index
                        e.col_index = self.col_index
                        self.error_code.append(e)

                elif state == 11 and sflag:
                    if self.IsDigit(self, self.string[self.index]):
                        state = 12
                    else:
                        state = -1
                        flag = 1
                        e = error()
                        e.error_code = 6  # 不能识别（小数点）
                        e.row_index = self.row_index
                        e.col_index = self.col_index
                        self.error_code.append(e)

                elif state == 12 and sflag:

                    if self.IsDigit(self, self.string[self.index]):
                        state = 12

                    elif self.string[self.index] == '"':
                        state = 30
                    elif self.string[self.index] == '\'':
                        state = 31
                    elif self.string[self.index] == '/' and self.string[self.index + 1] == '/':
                        state = 40
                    elif self.string[self.index] == '/' and self.string[self.index + 1] == '*':
                        state = 41

                    elif self.Isend(self, self.string[self.index]):
                        state = -1
                        flag = 5  # 科学计数法
                    else:
                        state = -1
                        flag = 1
                        e = error()
                        e.error_code = 6  # 不能识别（小数点）
                        e.row_index = self.row_index
                        e.col_index = self.col_index
                        self.error_code.append(e)

                elif state == 20 and sflag:
                    if self.IsLetter(self,self.string[self.index]) or self.IsDigit(self,self.string[self.index]):
                        state = 20
                    elif self.Isend(self, self.string[self.index]):
                        state = -1
                        flag = 10#标识符

                    elif self.string[self.index] == '"':
                        state = 30
                    elif self.string[self.index] == '\'':
                        state = 31
                    elif self.string[self.index] == '/' and self.string[self.index + 1] == '/':
                        state = 40
                    elif self.string[self.index] == '/' and self.string[self.index + 1] == '*':
                        state = 41
                         

                elif state == 30 and sflag:
                    if self.string[self.index] == '"':
                        state = -1
                        flag = 6
                    elif self.index == len(self.string):
                        state = -1
                        flag = 6#字符串
                        e = error()
                        e.error_code = 7  #字符串引号不匹配
                        e.row_index = self.row_index
                        e.col_index = self.col_index
                        self.error_code.append(e)

                elif state == 31 and sflag:
                    if self.string[self.index+1] == '\n':
                        self.index = self.index + 1
                        state = -1
                        flag = 7#字符

                elif state == 40 and sflag:
                    if self.string[self.index] == '\n' or self.index == len(self.string):
                        state = -1
                        flag = 0

                elif state == 41 and sflag:
                    if (self.string[self.index] == '*' and self.string[self.index + 1] == '/') or \
                        self.index == len(self.string):
                        state = -1
                        flag = 0
                        self.index = self.index+2

                self.index = self.index + 1
                self.col_index = self.col_index+1
                if state == -1:
                    break

            tmp = self.string[ii:self.index - 1]
            tmp1 = self.string[self.index - 1]
            if tmp:
                if flag == 1:
                    res = res + '<' + tmp + '  400' +'>' + '数字(整数)' + '\n'
                elif flag == 2:
                    res = res + '<' + tmp + '  400' +'>' + '数字(小数)' + '\n'
                elif flag == 3:
                    res = res + '<' + tmp + '  400' +'>' + '数字(8进制)' + '\n'
                elif flag == 4:
                    res = res + '<' + tmp + '  400' +'>' + '数字(十六进制)' + '\n'
                elif flag == 5:
                    res = res + '<' + tmp + '  400' +'>' + '数字(科学计数法)' + '\n'

                elif flag == 8:
                    ii = self.index

                elif flag == 9:
                    ii = self.index

                elif flag == 6:
                    res = res + '<' + str(tmp[0]) +'  221' + '>' + '  界符' + '\n'
                    res = res + '<' + str(tmp[1:]) + '  600' + '>' + '  字符串' + '\n'
                elif flag == 7:
                    res = res + '<' + str(tmp[0]) + '  221' + '>' + '  界符' + '\n'
                    res = res + '<' + str(tmp[1]) + '  601' + '>' + '  字符' + '\n'
                    res = res + '<' + str(tmp[2]) + '  221' + '>' + '  界符' + '\n'
                elif flag == 10:
                    try:
                        tmptoken = tmp +'  '+ str(token[tmp])
                    except:
                        tmptoken = tmp + '  '+ '500'
                    if tmp in key_word:
                        res = res + '<' + str(tmptoken) + '>' + '  关键字' + '\n'
                    else:
                        res = res + '<' + str(tmptoken) + '>' + '  标识符' + '\n'

                elif 31 <= flag <=35:
                    tmp = self.string[ii+1:self.index]
                    try:
                        tmptoken = tmp +'  '+ str(token[tmp])
                    except:
                        tmptoken = tmp + '  '+ '500'
                    res = res + '<' + str(tmptoken) + '>' + '  运算符' + '\n'



            if tmp1 in operators:
                if tmp1 == '>':
                    if self.string[self.index] == '>':
                        self.index = self.index + 1
                        tmp1 = '>>'
                    elif self.string[self.index] == '=':
                        self.index = self.index + 1
                        tmp1 = '>='

                elif tmp1 == '=':
                    if self.string[self.index ] == '=':
                        self.index = self.index + 1
                        tmp1 = '=='

                elif tmp1 == '<':
                    if self.string[self.index] == '<':
                        self.index = self.index + 1
                        tmp1 = '<<'
                    elif self.string[self.index] == '=':
                        self.index = self.index + 1
                        tmp1 = '<='
                elif tmp1 == '+':
                    if self.string[self.index] == '=':
                        self.index = self.index + 1
                        tmp1 = '+='
                    elif self.string[self.index] == '+':
                        self.index = self.index + 1
                        tmp1 = '++'
                elif tmp1 == '-':
                    if self.string[self.index] == '-':
                        self.index = self.index + 1
                        tmp1 = '--'
                    elif self.string[self.index] == '=':
                        self.index = self.index + 1
                        tmp1 = '-='

                try:
                    tmptoken = tmp1 +'  '+ str(token[tmp1])
                except:
                    tmptoken = tmp1 + '  '+'000'
                res = res + '<' + str(tmptoken) + '>' + '  运算符' + '\n'

            elif tmp1 in Delimiters:
                try:
                    tmptoken = tmp1 +'  '+ str(token[tmp1])
                except:
                    tmptoken = tmp1 + '  '+'000'
                res = res + '<' + str(tmptoken) + '>' + '  界符' + '\n'

                if tmp1 == '{':
                    braces = braces + 1
                elif tmp1 == '}':
                    braces = braces - 1
                elif tmp1 == '(':
                    parentheses = parentheses + 1
                elif tmp1 == ')':
                    parentheses = parentheses - 1
                elif tmp1 == '[':
                    brackets = brackets + 1
                elif tmp1 == ']':
                    brackets = brackets - 1

        if braces != 0:
            e = error()
            e.error_code = 1
            e.row_index = self.row
            e.col_index = 1
            self.error_code.append(e)
        if parentheses != 0:
            e = error()
            e.error_code = 2
            e.row_index = self.row
            e.col_index = 1
            self.error_code.append(e)
        if brackets != 0:
            e = error()
            e.error_code = 3
            e.row_index = self.row
            e.col_index = 1
            self.error_code.append(e)
        #
        # for i in self.error_code:
        #     print(i.error_code,i.row_index)
        error_text = self.disply_error(self)
        print(res)
        return res, error_text
    def disply_error(self):
        e=''
        if self.error_code:
            e='寄！your code have '+str(len(self.error_code))+' errors!\n'
            for i in range(len(self.error_code)):
                e = e + '[error' + str(i) + ']: ' + str(_error[self.error_code[i].error_code-1]) + ' in line ' + \
                    str(self.error_code[i].row_index+2)+ ' col ' +str(self.error_code[i].col_index)+'\n'
        else:
            e = 'finish\nyour code have no error!'
        print(e)
        return e

if __name__ == '__main__':
    string = '/*123*/\n//1==112.;a>=2;\n 0123; 1.02; 20; 0; abcc; 1e2; 8e-3;0x06; //sadfasdf\n ass=0; '
    # string = '#include<bits/stdc++.h> using namespace std; int main(){     int a=606;     \nint d=6;     int b=10;     ' \
    #          'int c=20;     a=b+c;   dd=0123;  c=a-b; \n    b=a+c;  a=123aaa \n  d=1a-c; \n    c=a+b;    \n d=b-a; \n  ' \
    #          ' a=c-b; }} \n     str a = "sdafasd"  cout<<a; 1.01;0x06;1e-2;/*jdhfjashd\ngdfg*/}'
    rec.recog(rec, string)

