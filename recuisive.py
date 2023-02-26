from Stack import Stack
from graphviz import Digraph
from Assembly import asm

class variable:  # 变量
    def __init__(self):
        self.address = 0  # 地址
        self.value = 0  # 值
        self.type = ''  # 类型
        self.name = ''  # 变量名
        self.scope = ''  # 范围


class function:
    def __init__(self):
        self.name = ''  # 函数名
        self.type = ''  # 返回值类型
        self.parameter = 0  # 参数个数
        self.parameterType = []  # 参数的返回值类型
        self.parameterNum = []


class quaternion:
    def __init__(self):
        self.op = ' '
        self.arg1 = ' '
        self.arg2 = ' '
        self.result = ' '


class recuisive:
    def __init__(self):
        self.valist = []
        self.funlist = []
        self.deep = 0
        self.gram ='''<函数定义闭包>-><函数定义> <函数定义闭包> |ε
<函数定义>-><修饰词闭包> <类型> <变量> <函数定义或全局变量> 
<函数定义或全局变量>->[(] <参数声明> [)] [{] <函数块> [}] |[=] <右值> [;] |ε
<修饰词闭包>-><修饰词> <修饰词闭包> |ε
<修饰词>->[public] |[private] |[protected] 
<类型>->[int] <取地址> |[char] <取地址> |[boolean] <取地址> |[void] <取地址> 
<取地址>-><星号> <取地址> |ε
<星号>->[*]
<变量>-><标志符> <数组下标> 
<标志符>->[id]
<数组下标>->[[] <因式> []] |ε 
<因式>->[(] <表达式> [)] |<变量> <函数调用> |<数字> 
<数字>->[digit]
<表达式>-><因子> <项> 
<因子>-><因式> <因式递归> 
<因式递归>->[*] <因式> <因式递归> |[/] <因式> <因式递归> |[%] <因式> <因式递归> |ε 
<项>->[+] <因子> <项> |[-] <因子> <项> |ε 
<参数声明>-><声明> <声明闭包> |ε
<声明>-><修饰词闭包> <类型> <变量> <是否赋初值> 
<是否赋初值>->[=] <赋初值> |ε 
<赋初值>-><标志符> [(] <参数列表> [)] [;] |<右值> |ε 
<右值>-><表达式> |[{] <多个数据> [}] 
<多个数据>-><数字> <数字闭包> 
<数字闭包>->[,] <数字> <数字闭包> |ε 
<声明闭包>->[,] <声明> <声明闭包> |ε 
<函数块>-><声明语句闭包> <函数块闭包> 
<声明语句闭包>-><声明语句> <声明语句闭包> |ε
<声明语句>-><声明> [;]
<函数块闭包>-><赋值函数> <函数块闭包>|<wihle循环> <函数块闭包> |<for循环> <函数块闭包> |<条件语句> <函数块闭包> |<函数返回> <函数块闭包>|[break]|ε
<wihle循环>->[while] [(] <逻辑表达式> [)] [{] <函数块> [}] 
<赋值函数>-><变量> [=] <赋值或函数调用> 
<函数调用>-> [(] <参数列表> [)] |ε
<赋值或函数调用>-><右值> [;] 
<参数列表>-><参数> <参数闭包> 
<参数闭包>->[,] <参数> <参数闭包> |ε 
<参数>-><标志符> |<数字> |<字符串> 
<字符串>->[string]
<for循环>->[for] [(] <赋值函数> <逻辑表达式> [;] <后缀表达式> [)] [{] <函数块> [}] 
<逻辑表达式>-><表达式> <逻辑或空>
<逻辑或空>-><逻辑运算符> <表达式> |ε
<逻辑运算符>->[<] |[>] |[==] |[!=] |[<]] |[>=]
<后缀表达式>-><变量> <后缀运算符> 
<后缀运算符>->[++] |[--] 
<条件语句>->[if] [(] <逻辑表达式> [)] [{] <函数块> [}] <否则语句> 
<否则语句>->[else] [{] <函数块> [}] |ε 
<函数返回>->[return] <因式> [;] '''
        self.gram = self.gram.split('\n')
        self.color = ['red', 'blue', 'green', 'black', 'pink', 'orange', 'purple']
        self.end, self.not_end = self.getend()
        self.Vn, self.Vt = self.not_end, self.end
        self.start = self.gram[0].split('->')[0]
        self.temp = []
        self.index = 0
        self.s = ''
        self.first_ls = {}
        self.follow_ls = {}
        self.first_ls, self.follow_ls = self.get_first_follow()
        self.dot = Digraph('grammar tree')
        self.id = 0
        self.GEN = []
        self.tmp=0
        self.breakflag = Stack()
    def gencode(self, op, a1, a2, result):
        g = quaternion()
        g.op = op
        g.arg1 = a1
        g.arg2 = a2
        g.result = result
        self.GEN.append(g)
    def printgen(self,g):
        print(g.op,'\t',g.arg1,'\t',g.arg2,'\t',g.result)
    def first(self, l):  # first集
        if l in self.end:
            return [l]
        else:
            t = []
            for i in self.gram:
                tmp = i.split('->')
                if tmp[0] == l:
                    tmp1 = tmp[1].split('|')
                    for j in tmp1:
                        j = j.split()

                        for k in range(len(j)):
                            tt = self.first(j[k])
                            tt1 = tt.copy()
                            while 'ε' in tt1:
                                tt1.remove('ε')
                            t = t + tt1
                            if 'ε' not in tt:
                                break
                            if k == len(j) - 1 and 'ε' in tt:
                                t = t + ['ε']
            return list(set(t))


    def long_first(self, j):
        t = []

        for k in range(len(j)):
            tt = self.first_ls[j[k]]
            tt1 = tt.copy()
            while 'ε' in list(set(tt1)):
                tt1.remove('ε')
            t = t + tt1
            if 'ε' not in tt:
                break
            if k == len(j) - 1 and 'ε' in tt:
                t = t + ['ε']
        return t

    def follow(self, l):  # follow集
        self.deep = self.deep + 1
        if self.deep > len(self.gram * 10):
            return
        if l == self.start:
            self.temp.append('#')
        for i in self.gram:
            tmp = i.split('->')
            tmp1 = tmp[1].split('|')
            for j in tmp1:
                j = j.split()
                for k in j:
                    if k == l:
                        tt = j.index(k)
                        if tt == len(j) - 1:
                            try:
                                self.temp += (self.follow_ls[tmp[0]])
                            except:
                                if tmp[0] != k:
                                    self.follow(tmp[0])
                        else:
                            tp = self.long_first(j[tt + 1:])
                            self.temp += tp
                            if 'ε' in tp:
                                try:
                                    self.temp += (self.follow_ls[tmp[0]])
                                except:
                                    if tmp[0] != k:
                                        self.follow(tmp[0])

    def get_first_follow(self):
        for i in self.not_end:
            self.temp = []
            self.temp = self.first(i)
            while None in self.temp:
                self.temp.remove(None)
            self.first_ls[i] = self.temp
        for i in self.end:
            self.first_ls[i] = [i]
        for i in self.not_end:
            self.temp = []
            self.deep=0
            self.follow(i)
            self.temp = list(set(self.temp))
            while 'ε' in self.temp:
                self.temp.remove('ε')
            self.follow_ls[i] = self.temp
        return self.first_ls, self.follow_ls

    def backPath(self, e_tc, t):
        self.GEN[e_tc].result = t
    def newTemp(self):
        ch = 't'+str(self.tmp)
        self.tmp = self.tmp + 1
        self.ch = ch
        return ch
    def analy(self, a):
        root = self.id - 1
        # print(a)
        for i in self.gram:
            t = i.split('->')
            if t[0] == a:
                break  # 得到当前非终结符所在的产生式
        flag = 0  # 输入符号是否在候选式first
        for i in t[1].split('|'):  # 遍历每个产生式
            i = i.split()

            if self.s[self.index][3] in self.long_first(i):  # 判断当前要匹配字符是否在候选式first
                flag = 1
                #####################################构造符号表
                if a == '<声明>':
                    va = variable()
                    va.type = self.s[self.index][3]
                    if self.s[self.index+1][3] == '[digit]':
                        va.value = self.s[self.index+1][1]
                    va.name = self.s[self.index+1][1]
                    self.valist.append(va)
                    # print(va.name,va.value, '1111111111111va')
                elif a=='<函数定义>' and self.s[self.index+2][1] == '(':
                    fun = function()
                    fun.name = self.s[self.index+1][1]
                    fun.type = self.s[self.index][3]
                    self.funlist.append(fun)
                    # print(fun.name,'1111111111111fun')
                #####################################构造符号表
                for k in i:
                    ifflag = 0
                    while_flag = 0
                    for_flag = 0
                    elseflag = 0

                    if k in self.end:
                        if a == '<函数块闭包>' and self.s[self.index][3] == '[break]':
                            self.gencode('j', '', '', self.breakflag.pop())
                        if k == self.s[self.index][3]:
                            # if self.s[self.index][3] == '[]'
                            self.dot.node(str(self.id), str(self.s[self.index][1]), fontname="FZFangSong-Z02")
                            self.dot.edge(str(root), str(self.id), color=self.color[self.id % 7])
                            self.id += 1  # draw
                            if self.index < len(self.s) - 1:
                                self.index = self.index + 1
                            print(self.s[self.index][1], self.index)  # 接受匹配
                        else:
                            print('应该是',k,'but',self.s[self.index][3])

                            break
                    else:  # 如果不是终结符进递归
                        if a == '<条件语句>' and self.s[self.index - 1][3] == '[{]':
                            ifflag = 1
                            self.gencode('j' + self.s[self.index - 4][1], self.s[self.index - 5][1],
                                         self.s[self.index - 3][1], len(self.GEN)+3)
                            self.gencode('j','','','')
                            if_bac = len(self.GEN) - 1

                        elif a=='<条件语句>' and self.s[self.index][3] == '[else]':
                            elseflag=1
                            self.gencode('j', '', '', '')
                            else_bac=len(self.GEN) - 1


                        elif a == '<赋值函数>' and self.s[self.index - 1][3] == '[=]':
                            if self.s[self.index][3] == '[id]' and self.s[self.index + 1][3] == '[(]':
                                self.gencode('call', self.s[self.index][1], '', self.s[self.index - 2][1])
                            if self.s[self.index][3] == '[(]':
                                # self.gencode(self.s[self.index + 2][1], self.s[self.index + 1][1],
                                #              self.s[self.index + 3][1], self.s[self.index - 2][1])
                                self.gencode(self.s[self.index + 2][1], self.s[self.index + 1][1],
                                             self.s[self.index + 3][1],self.newTemp())
                                self.gencode('=', self.ch,' ', self.s[self.index - 2][1])
                        elif a == '<声明>' and self.s[self.index][3] == '[id]' and self.s[self.index + 3][3] == '[;]':
                            self.gencode('=', self.s[self.index+2][1], ' ', self.s[self.index][1])

                        elif a == '<wihle循环>' and self.s[self.index - 1][3] == '[{]':
                            while_flag = 1
                            self.gencode('j' + self.s[self.index - 4][1], self.s[self.index - 5][1],
                                         self.s[self.index - 3][1], len(self.GEN) + 3)
                            self.gencode('j', '', '', '')
                            while_bac = len(self.GEN) - 1
                            self.breakflag.push(while_bac+1)

                        elif a == '<for循环>' and self.s[self.index - 1][3] == '[{]':
                            self.gencode('=', self.s[self.index - 10][1], '', self.s[self.index - 4][1])
                            for_flag = 1
                            self.gencode('j' + self.s[self.index - 7][1], self.s[self.index - 8][1],
                                         self.s[self.index - 6][1], len(self.GEN) + 3)
                            self.gencode('j', '', '', '')
                            for_bac = len(self.GEN) - 1
                            self.breakflag.push(for_bac+1)
                            # self.gencode('+', self.s[self.index - 4][1], '1', self.s[self.index - 4][1])
                            self.gencode('+', self.s[self.index - 4][1], '1', self.newTemp())
                            self.gencode('=', self.ch, ' ', self.s[self.index - 4][1])


                        self.dot.node(str(self.id), str(k), fontname="FZFangSong-Z02")
                        self.dot.edge(str(root), str(self.id), color=self.color[self.id % 7])
                        self.id += 1  # draw
                        self.analy(k)#进入递归

                        if a == '<条件语句>' and ifflag==1:
                            self.backPath(if_bac, str(len(self.GEN)+1))
                        if a=='<wihle循环>' and while_flag==1:
                            self.gencode('j',' ',' ',while_bac)
                            self.backPath(while_bac,str(len(self.GEN)+1))
                        if a == '<for循环>' and for_flag==1:
                            self.gencode('j', ' ', ' ', for_bac)
                            self.backPath(for_bac, str(len(self.GEN) + 1))
                        if a=='<条件语句>' and elseflag==1:
                            self.GEN[if_bac].result = str(int(self.GEN[if_bac].result)+1)
                            self.backPath(else_bac, str(len(self.GEN) + 1))

        # if flag == 0:
        #     if 'ε' in t[1].split('|'):
        #         if self.s[self.index] not in self.follow_ls[a]:
        #             print('error')
        #     else:
        #         print('error')


    def getend(self):
        not_end = []
        for i in self.gram:
            not_end.append(i.split('->')[0])
        not_end = list(set(not_end))

        end = []
        for i in self.gram:
            i = i.split('->')
            i = i[1].split('|')
            for j in i:
                j = j.split()
                for m in j:
                    if m not in not_end:
                        end.append(m)
        while '' in end:
            end.remove('')
        end.append('#')
        end = list(set(end))
        print(end)
        print(not_end)
        return end, not_end
    def reconvert(self,gram):
        gram = gram.split('\n')
        gram = [i for i in gram if len(i)>0]
        jj=[]
        t=gram[0][0]
        tmp = gram[0]
        for i in gram[1:]:
            if i.split('->')[0] == t:
                tmp+='|'+i.split('->')[1]
            else:
                jj.append(tmp)
                t = i.split('->')[0]
                tmp = i
        jj.append(tmp)
        return jj
    def c_gram(self,gram):
        gg=[]
        for i in range(len(gram)):
            tmp = gram[i].split('->')[0]+'->'
            m=gram[i].split('->')[1]
            for j in m:
                tmp+=j
                if (j=='>' or j == ']')and m.index(j)<len(m)-2:
                    tmp+=' '
            gg.append(tmp)
        return gg
    def convert(self,s):
        s=[i for i in s.split('\n') if len(i)>0]
        ss=[]
        for i in s:
            ss.append(i.split())
        for i in ss:
            if i[0] == '300' or i[0] == '400':
                i.append('[digit]')
            elif i[1] == 'break':
                i.append('[break]')
            elif i[0] == '500' or  i[0] == '130':
                i.append('[id]')
            else:
                i.append('['+i[1] +']')
            print(i[3],ss.index(i))
        return ss

    def getva(self,name):
        for i in self.valist:
            if i.name == name:
                return i.value
    def setva(self,name,value):
        for i in self.valist:
            if i.name == name:
                i.value = value

    def runner(self):
        va = {}
        for i in range(10000):
            va[str(i)] = i
            va[i] = i

        s = self.GEN
        index=0
        self.gencode('sys','','','')
        while True:
            if s[index].op == 'sys' or index == len(s)-1:
                break
            elif s[index].op == 'call' and s[index].arg1 == 'read':
                # tmp = input('input')
                i, okPressed = Start.ui.QInputDialog.getInt(self, "Get integer", "Percentage:", 28, 0, 100, 1)
                va[s[index].result] = i
            elif s[index].op == 'call' and s[index].arg1 == 'write':
                print('result',va[s[index].result])

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


s='''100 int INT
130 main MAIN
718 ( parentheses
719 ) parentheses
201 { braces
500 n ID
731 = EQUAL
500 read ID
718 ( parentheses
719 ) parentheses
203 ; COMMA
115 if IF
718 ( parentheses
500 n ID
707 > GT
300 10 INTEGER
719 ) parentheses
201 { braces
100 int INT
500 i ID
731 = EQUAL
300 0 INTEGER
203 ; COMMA
113 for FOR
718 ( parentheses
500 i ID
731 = EQUAL
300 0 INTEGER
203 ; COMMA
500 i ID
706 < LT
500 n ID
203 ; COMMA
500 i ID
726 ++ pp
719 ) parentheses
201 { braces
500 n ID
731 = EQUAL
500 write ID
718 ( parentheses
719 ) parentheses
203 ; COMMA
202 } braces
202 } braces
109 else ELSE
201 { braces
131 while WHILE
718 ( parentheses
500 n ID
707 > GT
300 0 INTEGER
719 ) parentheses
201 { braces
500 n ID
731 = EQUAL
718 ( parentheses
500 n ID
702 - MINUS
300 1 INTEGER
719 ) parentheses
203 ; COMMA
123 break break
201 } braces
500 n ID
731 = EQUAL
500 write ID
718 ( parentheses
719 ) parentheses
203 ; COMMA
202 } braces
202 } braces
202 } braces
'''

if __name__ == '__main__':
    rr = recuisive()
    # rr.s = ['[void]','[id]','[(]','[)]','[{]','[int]','[id]','[=]','[digit]','[;]','[}]','aaaa']
    # for i in rr.first_ls.keys():
    #     print(i,rr.first_ls[i])
    # print(rr.start)
    # print(rr.follow_ls)
    rr.s = rr.convert(s)
    # print(rr.s)
    rr.dot.node(str(rr.id), str(rr.start),fontname = "FZFangSong-Z02")
    rr.id = rr.id + 1
    rr.analy(rr.start)

    # rr.dot.view()
    print(len(rr.valist))
    for i in rr.GEN:
        print(rr.GEN.index(i)+1,'\t',end='')
        rr.printgen(i)
    aa = asm(rr.GEN)
    aa.assembly()
    for i in aa.asm:
        print(i)
    # rr.runner()
    #
