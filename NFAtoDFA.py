# -*- coding: utf-8 -*-

"""
@author: Bu Shaofeng
@software: PyCharm
@file: NFAtoDFA.py
@time: 2022-04-13 15:49

"""
from graphviz import Digraph
from ToNFA import Stack
import ToNFA
class Nfa:
    def __init__(self, start, accepted, move):
        self.start = start
        self.accepted = accepted
        self.move = move

    # dfs
    def make_Closure(self, ls):
        # print('ls')
        # print(ls)
        u = []
        stack = Stack()
        for i in ls:  # 先把状态集全部压入栈
            stack.push(i)
            u.append(i)
        while not (stack.is_empty()):
            i = stack.pop()  # 取出栈顶元素
            for d in self.move:  # 遍历状态表，如果存在空符号，则压入栈
                try:
                    if 'ε' in d.get(i):
                        a = d.get(i)['ε']
                        if a not in u:
                            stack.push(a)
                            u.append(a)
                    else:
                        pass
                except:
                    pass
        return u



    def make_move(self, ls, char):
        u = []
        for i in ls:
            for d in self.move:
                try:
                    if char in d.get(i):
                        a = d.get(i)[char]
                        if a not in u:
                            u.append(a)
                except:
                    pass
        return u

    def get_alpha(self, ls):
        ls1 = []
        for i in ls:
            if i.isalpha() and i not in ls1:
                ls1.append(i)
        return ls1


def find0(flag):
    for i in range(len(flag)):
        if flag[i] ==0:
            return i
    return False

def nfatodfa(Nfa,ls,end):
        state_list = Nfa.move
        ans = []
        flag = []
        Dstates = []
        endlist = []
        slist = [0]
        word_list = Nfa.get_alpha(ls)
        dfa_start_state = Nfa.make_Closure([Nfa.start])
        print(dfa_start_state)
        T = tuple(dfa_start_state)
        Dstates.append(T)
        flag.append(0)
        dot = Digraph('nfatodfa')
        while 0 in flag:
            i = find0(flag)
            flag[i] = 1
            T = Dstates[i]
            for ch in word_list:
                U = tuple(Nfa.make_Closure(Nfa.make_move(T, ch)))
                # if U not in Dstates and len(U)>0:
                if len(U)>0:
                    if U not in Dstates:
                        Dstates.append(U)
                        if end in U:
                            endlist.append(Dstates.index(U))
                        else:
                            slist.append(Dstates.index(U))
                        flag.append(0)
                    dic = {}
                    dic1 = {}
                    dic1[ch] = Dstates.index(U)  # 存放在字典里
                    dic[Dstates.index(T)] = dic1
                    ans.append(dic)
                    # print(dic)
                    dot.node(str(Dstates.index(T)), str(Dstates.index(T)))
                    dot.node(str(Dstates.index(U)), str(Dstates.index(U)))
                    dot.edge(str(Dstates.index(T)), str(Dstates.index(U)), label=str(ch), color='red')
        dot.view()
        # print(endlist,slist)
        return ans,endlist,slist

if __name__ == '__main__':
    ss = '(a*|b)abbb*'
    # ss = '(a*|ab(aa|ab*)*|a)'
    # ss = '(a|b)*aab*cc'
    s = ToNFA.add_sign(ss)
    sss = ToNFA.in2post(s)
    a,b,c,end= ToNFA.toNFA(sss)
    n = Nfa(a,b,c)
    nfatodfa(n,sss,end)
