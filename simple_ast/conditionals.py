from . import BaseBox


class NotConditional(BaseBox):
    def __init__(self, left):
        self.left = left

    def eval(self, context):
        return not self.left.eval(context)


class Conditional(BaseBox):
    ops_table = {
        ">": lambda x, y: x > y,
        "<": lambda x, y: x < y,
        ">=": lambda x, y: x >= y,
        "<=": lambda x, y: x <= y,
        "==": lambda x, y: x == y,
        "!=": lambda x, y: x != y,
        "&&": lambda x, y: x and y,
        "||": lambda x, y: x or y,
    }

    def __init__(self, left, operator, right):
        self.left = left
        self.right = right
        self.operator = operator

    def eval(self, context):
        func = self.ops_table.get(self.operator, None)
        if func is None:
            raise ValueError("Operator is not found")
        return func(self.left.eval(context), self.right.eval(context))


class If(BaseBox):
    def __init__(self, condition, if_statements, else_statements):
        self.condition = condition
        self.if_statements = if_statements
        self.else_statements = else_statements

    def eval(self, context):
        if self.condition.eval(context):
            self.if_statements.eval(context)
        else:
            self.else_statements.eval(context)


class While(BaseBox):
    def __init__(self, condition, statements):
        self.condition = condition
        self.statements = statements

    def eval(self, context):
        while (self.condition.eval(context)):
            self.statements.eval(context)