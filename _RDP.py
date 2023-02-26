from Stack import Stack
from graphviz import Digraph
from Forecasting_Parse import ForecastingParse


class variable:  # 变量
    def __init__(self):
        self.address = 0  # 地址
        self.genus = 0  # 值
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


class RDP:
    def __init__(self, gram,fp):
        self.gram = gram
        self.start = self.gram[0]
        self.gram = self.gram.split('\n')
        self.color = ['red', 'blue', 'green', 'black', 'pink', 'orange', 'purple']
        self.end, self.not_end = fp.getend()
        self.Vn, self.Vt = self.not_end, self.end
        self.start = gram[0][0]
        self.temp = []
        self.index = 0
        self.s = ''
        self.first_ls = {}
        self.follow_ls = {}
        self.first_ls, self.follow_ls = fp.first_ls,fp.follow_ls
        self.dot = Digraph('grammar tree')
        self.id = 0
    def analy(self, a):
        t = ''
        root = self.id - 1
        for i in self.gram:
            t = i.split('->')
            if t[0] == a:
                break  # 得到当前非终结符所在的产生式
        flag = 0  # 输入符号是否在候选式first
        for i in t[1].split('|'):  # 遍历每个产生式
            if self.s[self.index] in fp.long_first(i):  # 判断当前要匹配字符是否在候选式first
                flag = 1
                for k in i:
                    self.dot.node(str(self.id), str(k))
                    self.dot.edge(str(root), str(self.id), color=self.color[self.id % 7])
                    self.id += 1  # draw
                    if k in self.end:
                        if k == self.s[self.index]:
                            if self.index < len(self.s) - 1:
                                self.index = self.index + 1
                            print(k, self.index)  # 接受匹配
                        else:
                            print('error')
                            break
                    else:  # 如果不是终结符进递归
                        self.analy(k)
        if flag == 0:
            if 'ε' in t[1].split('|'):
                if self.s[self.index] not in self.follow_ls[a]:
                    print('error')
            else:
                print('error')



gram = '''E->TN
N->+TN|ε
T->FM
M->*FM|ε
F->(E)|i'''
if __name__ == '__main__':
    fp = ForecastingParse(gram)
    rr = RDP(gram,fp)
    rr.s = 'i+i*i*(i*i+i*(i+i))#'
    print(rr.first_ls)
    rr.dot.node(str(rr.id), str(rr.start))
    rr.id = rr.id + 1
    rr.analy(rr.start)
    rr.dot.view()