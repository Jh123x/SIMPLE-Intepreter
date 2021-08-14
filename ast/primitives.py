from . import BaseBox


class Number(BaseBox):
    def __init__(self, value):
        self.value = value

    def eval(self, context):
        return self.value


class Name():
    def __init__(self, value) -> None:
        self.value = value
    
    def eval(self, context):
        return self.value