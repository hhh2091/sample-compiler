
from Stack import Stack
from graphviz import Digraph
class ForecastingParse():
    def __init__(self,gram):
        self.deep = 0
        self.gram = gram
        self.start = self.gram[0]
        self.gram = self.gram.split('\n')
        self.color = ['red','blue','green','black','pink','orange','purple']
        self.end,self.not_end = self.getend()
        self.Vn,self.Vt = self.not_end,self.end 
        self.first_ls = {}
        self.follow_ls = {}
        self.start = gram[0][0]
        self.temp = []
        self.gram = self.convert()
        self.get_first_follow()
        self.Forecasting_Parse_list = self.make_Forecasting_Parse_list()


    def get_first_follow(self):
        for i in self.not_end:
            tem = self.first(i)
            self.first_ls[i] = tem

        for i in self.end:
            self.first_ls[i] = [i]

        for i in self.not_end:
            self.temp = []
            self.deep=0
            self.follow(i)

            self.temp = list(set(self.temp))
            while 'ε' in self.temp:
                self.temp.remove('ε')
            self.follow_ls[i] = self.temp.copy()
            print(i,self.temp)


    def first(self,l):#first集
        if l in self.end:
            return [l]
        else:
            t=[]
            for i in self.gram:
                tmp = i.split('->')
                if tmp[0] == l:
                    tmp1 = tmp[1].split('|')
                    for j in tmp1:
                        # if j[0] == 'ε':
                        #     t = t + ['ε']
                        #     continue
                        for k in range(len(j)):
                            tt = self.first(j[k])
                            tt1 = tt.copy()
                            while 'ε' in tt1:
                                tt1.remove('ε')
                            t = t + tt1
                            if 'ε' not in tt:
                                break
                            if k == len(j)-1 and 'ε' in tt:
                                t = t + ['ε']
            return list(set(t))
#{'C': ['d', 'c', 'a'], 'B': ['ε', 'b'], 'E': ['c', 'g'], 'A': ['c', 'b', 'd', 'g', 'a'], 'D': ['d', 'ε'],
    # def follow(self,l):#follow集
    #     # print(l)
    #     if len(self.temp)>10:
    #         if self.temp.count(self.temp[0])>10:
    #             return
    #     if l==self.start:
    #         self.temp.append('#')
    #     for i in self.gram:
    #         tmp = i.split('->')
    #         tmp1 = tmp[1].split('|')
    #         for j in tmp1:
    #             for k in j:
    #                 if k == l:
    #                     # tt = j.index(k)
    #                     if j.index(k)<len(j)-1:
    #                         for f in self.first_ls[j[j.index(k)+1]]:
    #                             self.temp.append(f)
    #                         if 'ε' in self.first_ls[j[j.index(k)+1]]:
    #                             try:
    #                                 self.temp+=(self.follow_ls[tmp[0]])
    #                             except:
    #                                 if tmp[0]!=k:
    #                                     self.follow(tmp[0])
    #                     elif j.index(k) == len(j)-1:
    #                         try:
    #                            self.temp+=(self.follow_ls[tmp[0]])
    #                         except:
    #                             if tmp[0]!=k:
    #                                 self.follow(tmp[0])
    def long_first(self,j):
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
    def follow(self,l):#follow集
        print(l,self.start)
        self.deep = self.deep+1
        if self.deep>len(self.gram):
            # if self.temp.count(self.temp[0])>5:
            #     return
            return
        if l==self.start:
            self.temp.append('#')
        for i in self.gram:
            tmp = i.split('->')
            tmp1 = tmp[1].split('|')
            for j in tmp1:
                for k in j:
                    if k == l:
                        tt = j.index(k)
                        if tt == len(j)-1:
                            try:
                               self.temp+=(self.follow_ls[tmp[0]])
                            except:
                                if tmp[0]!=k:
                                    self.follow(tmp[0])
                        else:
                            tp = self.long_first(j[tt+1:])
                            self.temp+=tp
                            if 'ε' in tp:
                                try:
                                    self.temp += (self.follow_ls[tmp[0]])
                                except:
                                    if tmp[0] != k:
                                        self.follow(tmp[0])

    def error(self):
        print('error')
        exit()

    def Forecasting_Parse(self,w):
        s = Stack()
        dott = Stack()
        s.push('#')
        dott.push(0)
        id=1
        root = id

        s.push(self.start)
        dott.push(id)
        ip = 0
        a=w[ip]
        x=s.pop()
        id = dott.pop()
        dot = Digraph('grammar tree')
        dot.node(str(id),str(x))
        id+=1
        while(x!='#'):
            if x==a:
                print([i for i in s.items],'\t\t\t',[w[i] for i in range(ip,len(w))],'\t\t\t','\t\taccept',x)
                ip = ip+1
                a = w[ip]
            elif x in self.Vt:
                self.error()
            elif x in self.Vn:
                if self.Forecasting_Parse_list[x][a] == '!':
                    self.error()
                else:
                    print([i for i in s.items],'\t\t\t',[w[i] for i in range(ip,len(w))],'\t\t\t',self.Forecasting_Parse_list[x][a])
                    for i in self.Forecasting_Parse_list[x][a].split('->')[1][::-1]:
                        if i != 'ε':
                            s.push(i)
                            dott.push(id)
                            dot.node(str(id),str(i))
                            dot.edge(str(root),str(id),color=self.color[id%7])
                            id+=1
                        elif i == 'ε':
                            dot.node(str(id),'ε')
                            dot.edge(str(root),str(id),color=self.color[id%7])
                            id+=1
                            pass
            x=s.pop()
            root = dott.pop()
        dot.view()

    def make_Forecasting_Parse_list(self):
        Forecasting_Parse_list = {}
        for x in self.not_end:
            t = {}
            for a in self.end:
                t[a] = '!'
            Forecasting_Parse_list[x] = t
        for i in self.gram:
            A = i.split('->')[0]
            a = i.split('->')[1]
            for j in self.long_first(a):
                    Forecasting_Parse_list[A][j] = i
            if 'ε' in self.long_first(a):
                for b in self.follow_ls[A]:
                    Forecasting_Parse_list[A][b] = i
        return Forecasting_Parse_list
    def convert(self):
        jj=[]
        for i in self.gram:
            t = i.split('->')[1].split('|')
            for j in t:
                jj.append(str(str(i[0])+'->'+str(j)))
        return jj
    def reconvert(self):
        jj=[]
        tmp = []
        t=self.gram[0][0]
        tmp = gram[0]
        for i in self.gram:
            if i.split('->')[0] == t:
                tmp+=i.split('->')[1]
            else:
                tmp.append(jj)
                t = i.split('->')[0]
                jj = i
        return tmp

    def getend(self):
        not_end = []
        for i in self.gram:
            not_end.append(i[0])
        not_end = list(set(not_end))

        end = []
        for i in self.gram:
            i = i.split('->')
            for j in i[1]:
                j = j.split('|')
                for k in j:
                    if k not in not_end:
                        end.append(k)
        while '' in end:
            end.remove('')
        end.append('#')
        end = list(set(end))

        return end,not_end
    def c(self):
        self.gram = self.gram.split('\n\n')
# gram = '''P->bTd
# T->SF
# F->;SF|ε
# S->N|C
# N->a
# C->ID
# D->eS|ε
# I->ZN
# Z->ict'''
# gram = '''A->BCc|gDB
# B->bCDE|ε
# C->DaB|ca
# D->dD|ε
# E->gAf|c'''
gram = '''E->TN
N->+TN|ε
T->FM
M->*FM|ε
F->(E)|i'''
if __name__ == '__main__':
       
    fp = ForecastingParse(gram)
    print(fp.first_ls)
    print(fp.follow_ls)
    print('================================')
    # for i in fp.Forecasting_Parse_list.keys():
    #     print(i,fp.Forecasting_Parse_list[i])
    s='i+i*i#'
    fp.Forecasting_Parse(s)
    # file = open("c.txt", 'r')
    # text = file.read()
    # file.close()
    # gram = text.split('\n\n')
    # gg = []
    # for i in gram:
    #     Candidate = i.split('\n')
    #     # print(Candidate)
        
    #     for k in range(1,len(Candidate)):
    #         l=[Candidate[0]]
    #         t = Candidate[k].split(' ')
    #         if '\t' not in t and len(t)>1:
    #             l = l+t
    #         while('\t:' in l):
    #             l.remove('\t:')
    #         while('\t|' in l):
    #             l.remove('\t|')
    #         if len(l)>=2:
    #             gg.append(l)
    #             print(l)
            

