class asm():
    def __init__(self,gen):
        self.GEN = gen
        self.asm = []
    def assembly(self):
        for index in range(len(self.GEN)):
            if self.GEN[index].op == 'sys' or index == len(self.GEN) - 1:
                self.asm.append('p'+str(index+1)+':')
                self.asm.append('CALL A')
            elif self.GEN[index].op == 'call' and self.GEN[index].arg1 == 'read':
                self.asm.append('p'+str(index+1)+':')
                self.asm.append('CALL A')
            elif self.GEN[index].op == 'call' and self.GEN[index].arg1 == 'write':
                self.asm.append('p'+str(index+1)+':')
                self.asm.append('CALL A')

            elif self.GEN[index].op == '+':
                self.asm.append('p'+str(index+1)+':')
                self.asm.append('MOV AX,'+self.GEN[index].arg1)
                self.asm.append('MOV AX,' + self.GEN[index].arg2)
                self.asm.append('MOV' + self.GEN[index].result+'AX')

            elif self.GEN[index].op == '-':
                self.asm.append('p'+str(index+1)+':')
                self.asm.append('MOV AX,' + self.GEN[index].arg1)
                self.asm.append('SUB AX,' + self.GEN[index].arg2)
                self.asm.append('MOV' + self.GEN[index].result + 'AX')

            elif self.GEN[index].op == '*':
                self.asm.append('p'+str(index+1)+':')
                self.asm.append('MOV AX,' + self.GEN[index].arg1)
                self.asm.append('MOV BX,' + self.GEN[index].arg2)
                self.asm.append('MUL BX')
                self.asm.append('MOV' + self.GEN[index].result + 'AX')

            elif self.GEN[index].op == '/':
                self.asm.append('p'+str(index+1)+':')
                self.asm.append('MOV AX,' + self.GEN[index].arg1)
                self.asm.append('MOV DX,0')
                self.asm.append('MOV BX,' + self.GEN[index].arg2)
                self.asm.append('DIV BX')
                self.asm.append('MOV ' + self.GEN[index].result + ' AX')
            # elif self.GEN[index].op == '%':
            elif self.GEN[index].op == '=':
                self.asm.append('p'+str(index+1)+':')
                self.asm.append('MOV AX,' + self.GEN[index].arg1)
                self.asm.append('MOV ' + self.GEN[index].result + ',AX')

            elif self.GEN[index].op[0] == 'j':
                if len(self.GEN[index].op) == 1:
                    self.asm.append('p'+str(index+1)+':')
                    self.asm.append('JMP far ptr P')

                elif self.GEN[index].op[1] == '>':
                    self.asm.append('p'+str(index+1)+':')
                    self.asm.append('MOV DX,1')
                    self.asm.append('MOV AX,'+ self.GEN[index].arg1)
                    self.asm.append('CMP AX,' + self.GEN[index].arg2)
                    self.asm.append('JA_GT')
                    self.asm.append('MOV DX,0')
                    self.asm.append('CMPn AX,0')
                    self.asm.append('JEN_NE')
                    self.asm.append('JMP far ptr ' + 'p'+str(self.GEN[index].result))
                    self.asm.append('_NE:NOP')
                elif self.GEN[index].op[1] == '<':
                    self.asm.append('p'+str(index+1)+':')
                    self.asm.append('MOV DX,1')
                    self.asm.append('MOV AX,' + self.GEN[index].arg1)
                    self.asm.append('CMP AX,,' + self.GEN[index].arg2)
                    self.asm.append('JB_LT')
                    self.asm.append('MOV DX,0')
                    self.asm.append('CMPn AX,0')
                    self.asm.append('JEN_NE')
                    self.asm.append('JMP far ptr ' + 'p'+str(self.GEN[index].result))
                    self.asm.append('_NE:NOP')
                elif self.GEN[index].op[1:] == '==':
                    self.asm.append('p'+str(index+1)+':')
                    self.asm.append('MOV DX,1')
                    self.asm.append('MOV AX,' + self.GEN[index].arg1)
                    self.asm.append('CMP AX,' + self.GEN[index].arg2)
                    self.asm.append('JE_EQ')
                    self.asm.append('MOV DX,0')
                    self.asm.append('CMPn AX,0')
                    self.asm.append('JEN_NE')
                    self.asm.append('JMP far ptr ' + 'p'+str(self.GEN[index].result))
                    self.asm.append('_NE:NOP')