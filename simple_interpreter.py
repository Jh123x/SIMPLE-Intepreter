class Context(object):
    def __init__(self):
        self.vars = {}
        self.funcs = {}


class Interpreter(object):
    def __init__(self, parse_result):
        self.parse_result = parse_result
        self.context = Context()

    def interpret(self):
        self.parse_result.eval(self.context)
            


