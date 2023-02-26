from itertools import combinations
from graphviz import Digraph
from ToNFA import Stack
import ToNFA
from NFAtoDFA import Nfa
from NFAtoDFA import nfatodfa
dfa = {'p1': {'c': 'p2', 'd': 'p6'},
       'p2': {'c': 'p7', 'd': 'p3'},
       'p3': {'c': 'p1', 'd': 'p3'},
       'p4': {'c': 'p3', 'd': 'p7'},
       'p5': {'c': 'p8', 'd': 'p6'},
       'p6': {'c': 'p3', 'd': 'p7'},
       'p7': {'c': 'p7', 'd': 'p5'},
       'p8': {'c': 'p7', 'd': 'p3'}}
# te = [{0: {'a': 1}}, {1: {'a': 2}}, {1: {'b': 3}}, {2: {'a': 2}}, {3: {'a': 4}}, {4: {'a': 5}},
#       {4: {'b': 6}}, {5: {'a': 5}}, {5: {'b': 6}}, {6: {'a': 4}}, {6: {'b': 6}}]
# startlist = ['p1','p2','p4','p5','p6','p7','p8']
# startlist = range(6)
# accepted = [6]
move = ['a','b']
def convert(ans):
    dd={}
    dic = {}
    for i in range(len(ans)):
        tmp = {}
        for j in ans[i].keys():
            tmp['a'] = ' '
            tmp['b'] = ' '
            dic[j] = tmp

    for i in range(len(ans)):
        tmp = {}
        tmp['a'] = ' '
        tmp['b'] = ' '
        a=' '
        b=' '
        try:
            for j in ans[i].keys():
                a = ans[i][j]['a']
        except:
            a=' '
            try:
                for j in ans[i].keys():
                    b = ans[i][j]['b']
            except:
                b=' '
        if b==' ':
            try:
                for j in ans[i].keys():
                    b = ans[i+1][j]['b']
            except:
                b =' '
        # print(i,a,b)
        if tmp['a'] == ' ' :
            tmp['a'] = a
        if tmp['b'] == ' ':
            tmp['b'] = b
        if tmp['a'] != ' ' or tmp['b'] != ' ':
            for j in ans[i].keys():
                if (dic[j]['a'] == ' ' and tmp['a']!=' ') or (dic[j]['b'] == ' ' and tmp['b']!=' '):
                    dic[j] = tmp
        # print('#',i, a, b,tmp)
    print(dic)
    return dic
def mindfa(dfa,startlist,accepted,move):
    list = [startlist,accepted]

    for i in move:
        for index,j in enumerate(list):
            tt = j[0]
            jj=[]
            new = []

            tmp = dfa[tt][i]
            # jj.append(tt)
            # print('j',j)
            for k in j:
                # print('11', k,dfa[k][i], tmp)
                try:
                    if dfa[k][i]!=tmp:
                        # print('22',k,dfa[k][i],tmp)
                        new.append(k)
                        # j.pop(j.index(k))
                    else:
                        jj.append(k)
                except:
                    pass
            # print('jj',jj,'j',j,'list',list)
            if jj:
                list[index] = jj
            # print('jj', jj, 'j', j,'list',list)
            if new:
                list.append(new)
                # print('new',new)
            # print('list',list)
    return list
def draw(list,dfa,move):
    dot = Digraph('mfa')
    dd={}
    for i in dfa:
        for j in move:
            for k in list:
                if dfa[i][j] in k:
                    dfa[i][j] = k[0]
    # print(dfa)
    for i in dfa.keys():
        for j in list:
            if i in j:
                dd[j[0]] = dfa[i]
    # print(dd)
    dic = {}
    t={}
    l=[]
    for i in dd.keys():
        for j in dd[i].keys():
            if dd[i][j]!= ' ':
                dic = {}
                t = {}
                dot.node(str(i), str(i))
                dot.node(str(dd[i][j]), str(dd[i][j]))
                dot.edge(str(i), str(dd[i][j]), label=str(j), color='red')
                t[j] = dd[i][j]
                dic[i] =  t
                l.append(dic)
    dot.view()
    return l
    # print(dd)
if __name__ == '__main__':
    # startlist = range(len(te)-2)
    # accepted = [len(te)]
    ss = '(a*|b)aba*'
    ss = '(a*|ab(aa|ab*)*|a)'
    s = ToNFA.add_sign(ss)
    sss = ToNFA.in2post(s)
    a, b, c, end = ToNFA.toNFA(sss)
    n = Nfa(a, b, c)
    te,accepted,startlist = nfatodfa(n, sss, end)
    print(te,accepted)
    dfa = convert(te)
    ll=(mindfa(dfa,startlist,accepted,move))
    print(ll)
    l=draw(ll,dfa,move)
    print(l)

