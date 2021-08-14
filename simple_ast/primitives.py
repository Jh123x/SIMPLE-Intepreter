from . import BaseBox


class Number(BaseBox):
    def __init__(self, value):
        self.value = value

    def eval(self, context):
        return self.value


class Name(BaseBox):
    def __init__(self, value) -> None:
        self.value = value
    
    def eval(self, context):
        return self.value


class NameEval(BaseBox):
    def __init__(self, value) -> None:
        self.value = value
    
    def eval(self, context):
        val = context.vars.get(self.value, None)
        if val is None:
            raise ValueError("Variable referenced before assignment")
        return val