# 预定义的可以分析的各种字符和关键字，依个人需求可进行修改


key_word = ['long', 'float', 'static',
            'char', 'short', 'switch', 'int',
            'const', 'if', 'then', 'else', 'for'
    , 'while', 'break', 'main']



operators = ['+', '-', '*', '/', ':', '&', ]               
Delimiters =[ '<',  '>',  '=', ';', '(', ')', '#', '{', '}', ',',
             '[', ']', "'", '.', '"']
sign = ['+', '-', '*', '/', ':', ':=', '<', '<>', '<=', '>', '>=', '=', ';', '(', ')', '#', '==', '{', '}', ',',
            '&', '[', ']', "'", '.', '"']
_error = ['braces mismatching','parentheses mismatching','brackets mismatching','expected unqualified-id before numeric constant']

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

class error:
    def __init__(self):
        self.row_index = 0
        self.error_code = -1

class rec():
    def __init__(self):
        self.index = 0
        self.result = []
        self.result1 = []
        self.string = ""
        self.row = 0
        self.row_index = 0
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
        while self.index <= (lenth - 2):
            ii = self.index
            flag = 0  # 空白
            state = 0

            while True:
                # self.index = self.index+1
                # print(state, self.index, self.Isend(self,self.string[self.index]),self.string[self.index])
                if self.string[self.index] == '\n':
                    self.row_index = self.row_index+1
                if state == 0 and self.Isend(self, self.string[self.index]):
                    state = -1
                if (state == 0) and self.IsLetter(self, self.string[self.index]):
                    state = 1
                elif state == 1 and (
                        self.IsDigit(self, self.string[self.index]) or self.IsLetter(self, self.string[self.index])):
                    state = 2
                elif state == 2 and (
                        self.IsDigit(self, self.string[self.index]) or self.IsLetter(self, self.string[self.index])):
                    state = 2
                elif (state == 2 or state == 1) and self.Isend(self, self.string[self.index]):
                    state = -1
                    flag = 1  # 标识符

                elif (state == 0 or state == 3) and self.IsDigit(self, self.string[self.index]):
                    state = 3
                elif state == 3 and self.IsLetter(self, self.string[self.index]):
                    state = -1
                    flag = 2
                    e = error()
                    e.error_code = 4#不能识别
                    e.row_index = self.row_index
                    self.error_code.append(e)
                elif state == 3 and self.Isend(self, self.string[self.index]):
                    state = -1
                    flag = 2  # 数字

                self.index = self.index + 1
                if state == -1:
                    break

            tmp = self.string[ii:self.index - 1]
            if tmp:
                if flag == 1:
                    try:
                        tmptoken = tmp +'  '+ str(token[tmp])
                    except:
                        tmptoken = tmp + '  '+'400'
                    if tmp in key_word:
                        res = res + '<' + str(tmptoken) + '>' + '  关键字' + '\n'
                    else:
                        res = res + '<' + str(tmptoken) + '>' + '  标识符' + '\n'
                elif flag == 2:
                    try:
                        tmptoken = tmp + '  '+str(token[tmp])
                    except:
                        tmptoken = tmp + '  '+'500'
                    res = res + '<' + str(tmptoken) + '>' + '  数字' + '\n'

            tmp1 = self.string[self.index - 1]
            if tmp1 in operators:
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
            self.error_code.append(e)
        if parentheses != 0:
            e = error()
            e.error_code = 2
            e.row_index = self.row
            self.error_code.append(e)
        if brackets != 0:
            e = error()
            e.error_code = 3
            e.row_index = self.row
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
                    str(self.error_code[i].row_index+1)+'\n'
        else:
            e = 'finish\nyour code have no error!'
        print(e)
        return e

if __name__ == '__main__':
    string = '#include<bits/stdc++.h> using namespace std; int main(){     int a=6;     \nint d=6;     int b=10;     ' \
             'int c=20;     a=b+c;     c=a-b; \n    b=a+c;  123aaa \n  d=1a-c; \n    c=a+b;    \n d=b-a; \n   a=c-b; }}))]] ' \
             '  cout<<a;}'
    rec.recog(rec, string)
