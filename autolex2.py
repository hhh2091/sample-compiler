# -*- coding: utf-8 -*-

"""
@author: Bu Shaofeng
@software: PyCharm
@file: autolex.py
@time: 2022-03-25 21:36

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
import ply.lex as lex
# 关键字列表
code = {'int': 100, 'float': 101, 'char': 102, 'case': 103, 'const': 104,
        'continue': 105, 'default': 106, 'do': 107, 'double': 108, 'else': 109,
        'enum': 110, 'extern': 111, 'break': 112, 'for': 113, 'goto': 114,
        'if': 115, 'auto': 116, 'long': 117, 'register': 118, 'return': 119,
        'short': 120, 'signed': 121, 'sizeof': 122, 'static': 123, 'struct': 124,
        'switch': 125, 'typedef': 126, 'unsigned': 127, 'union': 128, 'void': 129,'main':130,
        'volatile': 130, 'while': 131, '{': 201, '}': 202, ';': 203, ',': 204,
        '整数': 300, '小数': 400, '标识符': 500, '字符串': 600, '+': 701,'十六进制':320,'科学计数法':321,
        '-': 702, '*': 703, '/': 704, '%': 705, '<': 706, '>': 707,
        '<=': 708, '>=': 709, '==': 710, '!': 711, '!=': 712, '|': 713,
        '||': 714, '&': 715, '&&': 716, '.': 717, '(': 718, ')': 719,
        '[': 720, ']': 721, '/=': 722, '+=': 723, '-=': 724, '%=': 725,
        '++': 726, '--': 727, '?:': 728, '~': 729, '#': 730, '=': 731}
reserved = {
    'int': 'INT',
    'char': 'CHAR',
    'float': 'FLOAT',
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'while': 'WHILE',
    'return': 'RETURN',
    'void': 'VOID',
    'main': 'MAIN',
    # add more...
}
# List of token names.   This is always required
tokens = [
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'EQUAL',
    'ID',
    'COMMA',
    'INTEGER',
    'DECIMAL',
    'SCM',
    'Line_comment',
    'block_comment',
    'STRING',
    'HEX',
    'error1',
    'error2',
    'error3',
    'error4',
    'braces',
    'parentheses',
    'brackets',
    'SEMI',
    'AND',
    'OR',
    'POUND',
    'P',
    'LT',
    'LE',
    'GT',
    'GE',
    'D_EQUAL',
    'NEQ',
    'pp'


] + list(reserved.values())
error_list = ""
# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUAL = r'='
t_COMMA = r'\;'
t_braces = r'\{|\}'
t_parentheses = r'\(|\)'
t_brackets = r'\[|\]'
t_SEMI = r','
t_AND = r'(\&\&)|&'
t_OR = r'\|\|'
t_POUND = r'\#'
t_P = r'\%'
t_LT = r'\<'
t_LE = r'\<\='
t_GT = r'\>'
t_pp = r'\+\+'
t_GE = r'\>\='
t_D_EQUAL = r'\=\='
t_NEQ = r'\!\='

zero = r'0'
digit = r'([0-9])'
# digit_without0 = r'([1-9])'
letter = r'([_A-Za-z])'
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
def t_error1(t):
    r'[0]([0-9]+)'
    global error_list
    error_list += f'数字（不能以0开始）错误{t.value} 在 {t.lineno+1}行\n'

def t_error2(t):
    r'([0-9]+[a-wy-zA-WY-Z]+)'
    global error_list
    error_list += f'标识符（不能以数字开始）错误{t.value} 在第{t.lineno+1}行\n'

def t_error3(t):
    r'([0-9]+\.[0-9]+\.[0-9])'
    global error_list
    error_list += f'标识符（小数点）错误{t.value} 在 {t.lineno+1}行\n'
def t_error4(t):
    r'0 [xX][0-9][F-Zf-z]'
    global error_list
    error_list += f'无法识别的十六进制错误{t.value} 在 {t.lineno+1}行\n'


t_INTEGER = r'([1-9][0-9]*)|0'
t_DECIMAL = r'(([1-9][0-9]*)|0)\.\d+'
# t_SCM = r'('+t_DECIMAL +r'|' + t_INTEGER + r')e' + t_INTEGER
t_SCM = r'(' +t_INTEGER+r'|'+t_DECIMAL+r')'+r'([Ee][+-]?[\d]+)'
# t_ID = r'(' + letter + r'(' + digit + r'|' + letter + r')*)'
ID = r'(' + letter + r'(' + digit + r'|' + letter + r')*)'
t_STRING = r'(\".* \")|(\'.*\')'
t_HEX = r'0 [xX]([0-9]|[A-Fa-f])+' #16进制


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


def t_ID(t):
    r'([a-zA-Z]([0-9]|[a-zA-Z])*)'
    # 从保留字列表中查找保留字，并保存在标记类型中；如果不是保留字，类型就为标识符
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    # Look up symbol table information and return a tuple
    # t.value = (t.value, symbol_lookup(t.value))
    return t

def t_Line_comment(t):
    r'\/\/[^\n]*'

def t_block_coment(t):
    r'\/\*([^\*^\/]*|[\*^\/*]*|[^\**\/]*)*\*\/'
# Error handling rule
def t_error(t):
    # 输出不合法的字符，并且通过调用t.lexer.skip(1)跳r过一个字符
    global error_list
    error_list += f'不合法字符{t.value[0]} 在 {t.lineno+1}行\n'
    t.lexer.noError = False
    t.lexer.skip(1)


sss = '''
    "sfsdf"
    'asd'
    08
    123a
    0xa2
     .2
    15.
    /*sdfjhk
    15.
    asd*/
    a=3.4e23
    23.24e-21
    0
    
    a=8798
    a1=0.988e+3;
    float
    //dskjf;as
    //int a1 = +10;
    //int b2bb = 20;
   // int mmm = a1+b2bb;
    '''

# Build the lexer

class auto():
    def __init__(self):
        self.lexer = lex.lex()
        self.res = ''
    def rec(self,string):
        self.lexer.input(string)
        self.res = ''
        while True:
            tok = self.lexer.token()
            if not tok: break  # No more input
            if str(tok.type) == 'ID':
                self.res += str(code.get("标识符"))+' ' +str(tok.value) +' '+ str(tok.type) +'\n'
                continue
            elif str(tok.type) == 'INTEGER':
                self.res += str(code.get("整数"))+' ' +str(tok.value)+' '+ str(tok.type)+'\n'
                continue
            elif str(tok.type) == 'DECIMAL':
                self.res += str(code.get("小数")) +' '+ str(tok.value)+' '+ str(tok.type)+'\n'
                continue
            elif str(tok.type) == 'SCM':
                self.res += str(code.get("科学计数法")) +' '+ str(tok.value)+' '+ str(tok.type)+'\n'
                continue
            elif str(tok.type) == 'HEX':
                self.res += str(code.get("十六进制")) + ' ' + str(tok.value) +' '+ str(tok.type)+ '\n'
                continue
            elif str(tok.type) == 'STRING':
                self.res += str(code.get("字符串")) +' '+ str(tok.value)+' '+ str(tok.type)+'\n'
                continue
            elif tok.type in tokens:
                self.res += str(code.get(tok.value)) + ' ' + str(tok.value)+' '+ str(tok.type)+'\n'
                continue
        global error_list
        err = error_list
        error_list = ''
        return self.res,err
if __name__ == '__main__':
    aa = auto()
    aa.rec(sss)
