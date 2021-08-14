from rply import ParserGenerator
import simple_ast as ast
from lexer import lexer

pg = ParserGenerator(
    list(map(lambda x: x.name, lexer.rules)),
    precedence=[ 
        ('left', ['PROCEDURE']), 
        ('left', ['EQUAL']),  
        ('left', ['IF', 'COLON', 'ELSE', 'END', 'NEWLINE','WHILE',]), 
        ('left', ['AND', 'OR',]), 
        ('left', ['NOT']), 
        ('left', ['EQUALS', 'NOT_EQUALS', 'GREATER_EQUAL','GREATER', 'LESS', 'LESS_EQUAL',]), 
        ('left', ['PLUS', 'MINUS',]), 
        ('left', ['MUL', 'DIV',]),
        ('left', ['PRINT']),
        ('left', ['NAME']),
        
    ])

@pg.production('statements : statement statements')
def statements(p):
    return ast.Statements([p[0]]) + p[1]

@pg.production('statements : statement')
@pg.production('statement : expression')
def statement(p):
    return ast.Statements([p[0]])

@pg.production('expression : NUMBER')
def expression_number(p):
    return ast.Number(int(p[0].getstr()))

# Conditionals
@pg.production("conditional : expression GREATER expression")
@pg.production("conditional : expression LESS expression")
@pg.production("conditional : expression GREATER_EQUAL expression")
@pg.production("conditional : expression LESS_EQUAL expression")
@pg.production("conditional : expression EQUALS expression")
@pg.production("conditional : expression NOT_EQUALS expression")
@pg.production("conditional : conditional AND conditional")
@pg.production("conditional : conditional OR conditional")
def conditional(p):
    return ast.Conditional(p[0], p[1].getstr(), p[2])

@pg.production("conditional : NOT conditional")
def not_conditional(p):
    return ast.NotConditional(p[1])

@pg.production("statement : IF LPAREN conditional RPAREN THEN LBRACE statements RBRACE ELSE LBRACE statements RBRACE")
def if_condition(p):
    return ast.If(p[2], p[6], p[10])

@pg.production("statement : WHILE LPAREN conditional RPAREN LBRACE statements RBRACE")
def while_condition(p):
    return ast.While(p[2], p[5])

@pg.production('expression : LPAREN expression RPAREN')
@pg.production('conditional : LPAREN conditional RPAREN')
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

@pg.production("expression : NAME")
def name(p):
    return ast.NameEval(p[0].getstr())

@pg.production("statement : PRINT expression SEMICOLON")
def printing(p):
    return ast.Print(p[1])

@pg.production("statement : READ NAME SEMICOLON")
def reading(p):
    return ast.Read(ast.Name(p[1].getstr()))


@pg.production("statement : NAME EQUAL expression SEMICOLON")
def assign(p):
    return ast.Assign(ast.Name(p[0].getstr()), p[2])


# Functions
@pg.production("statement : PROCEDURE NAME LBRACE statements RBRACE")
def procedure(p):
    return ast.Procedure(ast.Name(p[1].getstr()), p[3])

@pg.production("statement : CALL NAME SEMICOLON")
def reading(p):
    return ast.Call(ast.Name(p[1].getstr()))


# Error handling
@pg.error
def error(token):
    raise ValueError(f"Token `{token.value}` is unexpected on line {token.source_pos.lineno} column {token.source_pos.colno}")

parser = pg.build()