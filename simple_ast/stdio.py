from . import BaseBox


class Print(BaseBox):
    def __init__(self, value) -> None:
        self.value = value

    def eval(self, context):
        print(self.value.eval(context))


class Read(BaseBox):
    def __init__(self, value) -> None:
        self.value = value

    def eval(self, context):
        varname = self.value.eval(context)
        context.vars[varname] = int(input())
