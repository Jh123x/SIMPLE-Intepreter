import argparse
from simple_lexer import lexer
from simple_parser import parser as simpleparser
from simple_interpreter import Interpreter

def readFile(filename):
    with open(filename) as file:
        return file.read()

def tokenizer(filename):
    """Only tokenise the simple file"""
    data = readFile(filename)
    tokens = lexer.lex(data)
    return [i for i in tokens]


def run(filename: str):
    """Run the simple file"""
    data = readFile(filename)

    tokens = lexer.lex(data)
    results = simpleparser.parse(tokens)
    intepreter = Interpreter(results)
    intepreter.interpret()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=str, help="Path to source file")

    args = parser.parse_args()
    source = args.source
    run(source)

    