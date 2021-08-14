from rply import LexerGenerator

lg = LexerGenerator()
lg.ignore(r"\s+")
lg.add("IF", r"if")
lg.add("WHILE", r"while")
lg.add("ELSE", r"else")
lg.add("PRINT", r'print')
lg.add("LPAREN", r"\(")
lg.add("RPAREN", r"\)")
lg.add("LBRACE", r"\{")
lg.add("RBRACE", r"\}")
lg.add("EQUAL", r"=")

# Bools
lg.add("GREATER", r">")
lg.add("LESS", r"<")
lg.add("GREATER_EQUAL", r">=")
lg.add("LESS_EQUAL", r">=")
lg.add("EQUALS", r"==")
lg.add("NOT_EQUALS", r"!=")
lg.add("OR", r"\|\|")
lg.add("AND", r"&&")
lg.add("NOT", "!")


lg.add("SEMICOLON", r';')
lg.add("NUMBER", r"\d+")
lg.add("PROCEDURE", r"procedure")
lg.add("CALL", r"call")
lg.add("READ", r"read")
lg.add("PLUS", r"\+")
lg.add("MINUS", r"-")
lg.add("DIV", r"/")
lg.add("MUL", r"\*")
lg.add("MOD", r"%")
lg.add("THEN", r'then')
lg.add("NAME", r"[A-Za-z_][a-zA-Z0-9_]*")


lexer = lg.build()
