from . import BaseBox


class BinaryOp(BaseBox):
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Add(BinaryOp):
    def eval(self, context):
        return self.left.eval(context) + self.right.eval(context)

class Sub(BinaryOp):
    def eval(self, context):
        return self.left.eval(context) - self.right.eval(context)

class Mul(BinaryOp):
    def eval(self, context):
        return self.left.eval(context) * self.right.eval(context)

class Div(BinaryOp):
    def eval(self, context):
        return self.left.eval(context) / self.right.eval(context)

class Mod(BinaryOp):
    def eval(self, context):
        return self.left.eval(context) % self.right.eval(context)

class Assign(BinaryOp):
    def eval(self, context):
        context.vars[self.left.eval(context)] = self.right.eval(context)