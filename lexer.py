from rply import LexerGenerator

lg = LexerGenerator()
lg.ignore(r"\s")

# Symbols
lg.add("LPAREN", r"\(")
lg.add("RPAREN", r"\)")
lg.add("LBRACE", r"\{")
lg.add("RBRACE", r"\}")

# Bools
lg.add("GREATER", r">")
lg.add("LESS", r"<")
lg.add("GREATER_EQUAL", r">=")
lg.add("LESS_EQUAL", r"<=")
lg.add("EQUALS", r"==")
lg.add("NOT_EQUALS", r"!=")
lg.add("OR", "\|\|")
lg.add("AND", r"&&")
lg.add("NOT", r"!")
lg.add("EQUAL", r"=")
lg.add("SEMICOLON", r";")
lg.add("PLUS", r"\+")
lg.add("MINUS", r"-")
lg.add("DIV", r"/")
lg.add("MUL", r"\*")
lg.add("MOD", r"%")

# Words

lg.add("READ", r"read")
lg.add("PROCEDURE", r"procedure")
lg.add("CALL", r"call")
lg.add("WHILE", r"while")
lg.add("IF", r"if")
lg.add("THEN", r"then")
lg.add("ELSE", r"else")
lg.add("PRINT", r"print")
lg.add("NUMBER", r"\d+")
lg.add("NAME", r"[A-Za-z][A-Za-z0-9]*")

lexer = lg.build()
