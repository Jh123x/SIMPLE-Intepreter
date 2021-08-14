from lexer import lexer
from simp_parser import parser
from interpreter import Interpreter


source = "./test.simp"

with open(source) as file:
    data = file.read()
tokens = lexer.lex(data)
results = parser.parse(tokens)
intepreter = Interpreter(results)
intepreter.interpret()