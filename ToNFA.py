# -*- coding: utf-8 -*-

"""
@author: Bu Shaofeng
@software: PyCharm
@file: ToNFA.py
@time: 2022-04-13 14:31
"""
from graphviz import Digraph
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):  # 判断栈是否为空
        return self.items == []

    def size(self):  # 获取栈中元素的个数
        return len(self.items)

    def push(self, item):  # 入栈
        self.items.append(item)

    def pop(self):  # 出栈
        return self.items.pop()

    def top(self):  # 获取栈顶元素
        if len(self.items):
            return self.items[len(self.items) - 1]
        return None


#   构建字母表如：ab|c(d*|a),添加乘法点->a·b|c·(d*|a)
def add_sign(str):
    ls = list(str) + ['!']
    length = len(ls)
    i = 0
    while ls[i] != '!':
        if ls[i].isalpha() and ls[i + 1].isalpha():
            ls.insert(i + 1, "·")
            i += 1
        if ls[i].isalpha() and ls[i + 1] == "(":
            ls.insert(i + 1, "·")
            i += 1
        if ls[i] == ")" and ls[i + 1].isalpha():
            ls.insert(i + 1, "·")
            i += 1
        if ls[i] == "*" and ls[i + 1].isalpha():
            ls.insert(i + 1, "·")
            i += 1
        if ls[i] == ")" and ls[i + 1] == "(":
            ls.insert(i + 1, "·")
            i += 1
        if ls[i] == "*" and ls[i + 1] == "(":
            ls.insert(i + 1, "·")
            i += 1
        i += 1
    del ls[-1]
    newstr = ''.join(ls)
    return newstr

def priority(z):
    if z == '+':
        return 1
    if z == '|':
        return 2
    if z == '·':
        return 3
    if z == '*':
        return 4

def in2post(expr):

    stack = []  # 存储栈
    post = []  # 后缀表达式存储
    for z in expr:
        if z not in ['·','×', '*', '|', '+', '-', '(', ')']:  # 字符直接输出
            post.append(z)
        else:
            if z != ')' and (not stack or z == '(' or stack[-1] == '('or priority(z) > priority(stack[-1])):
                stack.append(z)     # 运算符入栈

            elif z == ')':  # 右括号出栈
                while True:
                    x = stack.pop()
                    if x != '(':
                        post.append(x)
                        print(2, post)
                    else:
                        break
            else:   # 比较运算符优先级，看是否入栈出栈
                while True:
                    if stack and stack[-1] != '(' and priority(z) <= priority(stack[-1]):
                        post.append(stack.pop())
                        print(3, post)
                    else:
                        stack.append(z)
                        break
    while stack:    # 还未出栈的运算符，需要加到表达式末尾
        post.append(stack.pop())
    return post


# class NFA():
#     def __init__(self, start, accepted,move):
#         self.start = start
#         self.accepted = accepted
#         self.move = move
class NFA:
    def __init__(self, ID, start=None, accepted=None,move = None):
        self.ID = ID
        self.start = start
        self.accepted = accepted
        self.move = move

class Transition:
    def __init__(self, sourcestate, targetstate, char='ε'):
        self.sourcestate = sourcestate
        self.targetstate = targetstate
        self.char = char
    def print_side(self):
        print("{0}-->{1},值：{2}".format(self.sourcestate.ID, self.targetstate.ID, self.char))


# def make_begin():
#     start = State('start')

def make_state_list(state_list, now_state_id, values, state):  #move列表
    dic = {}
    dic1 = {}
    dic1[values] = state.ID
    dic[now_state_id] = dic1
    state_list.append(dic)

def is_alpha(now_state_id, cnt_State, values, state_list):
    a = NFA(now_state_id)
    b = NFA(now_state_id + 1)
    make_state_list(state_list, now_state_id, values, b)
    side = Transition(a, b, values)
    side.print_side()
    return NFA(cnt_State, a, b), state_list


def is_or(now_state_id, cnt_State, state1, state2, state_list):
    a = NFA(now_state_id)
    b = NFA(now_state_id + 1)
    make_state_list(state_list, now_state_id, 'ε', state1.start)
    s1 = Transition(a, state1.start)
    s1.print_side()
    make_state_list(state_list, now_state_id, 'ε', state2.start)
    s2 = Transition(a, state2.start)
    s2.print_side()
    make_state_list(state_list, state1.accepted.ID, 'ε', b)
    s3 = Transition(state1.accepted, b)
    s3.print_side()
    make_state_list(state_list, state2.accepted.ID, 'ε', b)
    s4 = Transition(state2.accepted, b)
    s4.print_side()
    return NFA(cnt_State, a, b), state_list

def is_and(now_state_id, cnt_State, state1, state2, state_list):
    a = NFA(now_state_id)
    b = NFA(now_state_id + 1)
    make_state_list(state_list, now_state_id, 'ε', state1.start)
    s1 = Transition(a, state1.start)
    s1.print_side()
    make_state_list(state_list, state1.accepted.ID, 'ε', state2.start)
    s2 = Transition(state1.accepted, state2.start)
    s2.print_side()
    make_state_list(state_list, state2.accepted.ID, 'ε', b)
    s3 = Transition(state2.accepted, b)
    s3.print_side()
    return NFA(cnt_State, a, b), state_list


def is_repeat(now_state_id, cnt_State, state1, state_list):
    a = NFA(now_state_id)
    b = NFA(now_state_id + 1)
    make_state_list(state_list, now_state_id ,'ε', state1.start)
    s1 = Transition(a, state1.start)
    s1.print_side()
    make_state_list(state_list, state1.accepted.ID, 'ε', state1.start)
    s2 = Transition(state1.accepted, state1.start)
    s2.print_side()
    make_state_list(state_list, state1.accepted.ID, 'ε', b)
    s3 = Transition(state1.accepted, b)
    s3.print_side()
    make_state_list(state_list, now_state_id, 'ε', b)
    s4 = Transition(a, b)
    s4.print_side()
    return NFA(cnt_State, a, b), state_list


def toNFA(ls):
    sssstack = Stack()
    id = 1
    cnt_State = 1
    state_list = []
    for i in ls:
        if i.isalpha():
            nfa, state_list = is_alpha(id, cnt_State, i, state_list)
            sssstack.push(nfa)
            id += 2
        else:
            if i == '*':
                nfa = sssstack.pop()
                nfa, state_list = is_repeat(id, cnt_State, nfa, state_list)
                sssstack.push(nfa)
                id += 2
            elif i == '|':
                nfa1 = sssstack.pop()
                nfa2 = sssstack.pop()
                nfa, state_list = is_or(id, cnt_State, nfa2, nfa1, state_list)
                sssstack.push(nfa)
                id += 2
            elif i == '·':
                nfa1 = sssstack.pop()
                nfa2 = sssstack.pop()
                nfa, state_list = is_and(id, cnt_State,  nfa2, nfa1, state_list)
                sssstack.push(nfa)
                id += 2
    ans = sssstack.pop()
    dot = Digraph('test')
    for i in state_list:
        a, = i
        tmp, = i.values()
        b, = tmp.values()
        m, = tmp
        dot.node(str(a),str(a))
        dot.node(str(b), str(b))
        dot.edge(str(a),str(b),label = str(m),color='red',rankdir='LR')
        # edge = dot.get_edge(str(a),str(b))
    dot.graph_attr['rankdir'] = 'LR'
    dot.view()
    ans.move = state_list
    print('\n\n\n\n',ans.ID, ans.start.ID, ans.accepted.ID, ans.move)

    return ans.start.ID, ans.accepted.ID, state_list,id-1


if __name__ == '__main__':
    ss = '(a|b)*aab*cc'
    s = add_sign(ss)
    sss = in2post(s)
    a,b,c,end = toNFA(sss)