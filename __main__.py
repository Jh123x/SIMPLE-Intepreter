import argparse
from lexer import lexer
from simp_parser import parser as simpleparser
from interpreter import Interpreter

def tokenizer(filename):
    with open(filename) as file:
        data = file.read()
    tokens = lexer.lex(data)
    return [i for i in tokens]


def run(filename: str):
    with open(filename) as file:
        data = file.read()
    tokens = lexer.lex(data)
    results = simpleparser.parse(tokens)
    intepreter = Interpreter(results)
    intepreter.interpret()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=str)

    args = parser.parse_args()
    source = args.source
    run(source)

    