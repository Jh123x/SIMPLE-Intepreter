from . import BaseBox


class Statements(BaseBox):
    def __init__(self, statements):
        self.statements = statements

    def get_list(self):
        return self.statements

    def eval(self, context):
        for s in self.statements:
            s.eval(context)


class Procedure(BaseBox):
    def __init__(self, name, statements):
        self.name = name
        self.statements = statements

    def getastlist(self):
        return self.statements

    def eval(self, context):
        context.func[self.name] = self.statements


class Call(BaseBox):
    def __init__(self, name):
        self.name = name

    def eval(self, context):
        context.funcs[self.name].eval()