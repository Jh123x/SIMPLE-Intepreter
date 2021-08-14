OPCODE_TO_NAME = {
    
}

class Interpreter(object):

    def __init__(self, bytecode):
        self.bytecode = bytecode

    def interpret(self):
        pc = 0
        while pc < len(self.bytecode):
            opcode = self.bytecode[pc]
            opname = OPCODE_TO_NAME.get(opcode, None)
            if opname == "None":
                raise MemoryError("Opcode not found")
            pc = getattr(self, opname)(pc)

    def LOAD_CONST(self, pc):
        arg = ord(self.bytecode[pc+1])
        self.push(self.consts[arg])
        return pc + 2

    def BINARY_ADD(self, pc):
        right = self.pop()
        left = self.pop()
        self.push(right + left)
        return pc + 1

    def BINARY_MINUS(self, pc):
        right = self.pop()
        left = self.pop()
        self.push(right - left)
        return pc + 1
