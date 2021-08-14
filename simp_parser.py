from rply import ParserGenerator
import simple_ast as ast
from lexer import lexer

pg = ParserGenerator(
    list(map(lambda x: x.name, lexer.rules)),
    precedence=[ 
        ('left', ['PROCEDURE',]), 
        ('left', ['=']), 
        ('left', ['[',']',',']), 
        ('left', ['IF', 'COLON', 'ELSE', 'END', 'NEWLINE','WHILE',]), 
        ('left', ['AND', 'OR',]), 
        ('left', ['NOT',]), 
        ('left', ['==', '!=', '>=','>', '<', '<=',]), 
        ('left', ['PLUS', 'MINUS',]), 
        ('left', ['MUL', 'DIV',]),
    ])


@pg.production('statements : statement')
@pg.production('statement : expression SEMICOLON')
def statement(p):
    return p[0]

@pg.production('expression : NUMBER')
def expression_number(p):
    return ast.Number(int(p[0].getstr()))

@pg.production('expression : NAME')
def expression_name(p):
    return ast.Name(p[0].getstr())

@pg.production('expression : LPAREN expression RPAREN')
def expression_parens(p):
    return p[1]

@pg.production('expression : expression PLUS expression')
@pg.production('expression : expression MINUS expression')
@pg.production('expression : expression MUL expression')
@pg.production('expression : expression DIV expression')
@pg.production('expression : expression MOD expression')
def expression_binop(p):
    left = p[0]
    right = p[2]
    d = {
        "PLUS": ast.Add,
        "MINUS": ast.Sub,
        "DIV": ast.Div,
        "MUL": ast.Mul,
        "MOD": ast.Mod,
    }

    op = p[1].name
    res =  d.get(op, None)
    if res is None:
        raise AssertionError(f"Invalid binary operator {op}")
    return res(left, right)

@pg.production("statement : PRINT expression SEMICOLON")
def printing(p):
    return ast.Print(p[1])

@pg.production("statement : NAME EQUAL expression SEMICOLON")
def assign(p):
    return ast.Assign(p[0], p[2])

@pg.error
def error(token):
    raise ValueError(f"Token {token} is unexpected")

parser = pg.build()