from rply import LexerGenerator

lg = LexerGenerator()
lg.ignore(r"\t+")
lg.ignore(r"\n+")


# Symbols
lg.add("LPAREN", r"\(")
lg.add("RPAREN", r"\)")
lg.add("LBRACE", r"\{")
lg.add("RBRACE", r"\}")

# Bools
lg.add("GREATER_EQUAL", r">=")
lg.add("LESS_EQUAL", r"<=")
lg.add("EQUALS", r"==")
lg.add("NOT_EQUALS", r"!=")
lg.add("GREATER", r">")
lg.add("LESS", r"<")
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
keywords = {
    "READ": r'read',
    "PROCEDURE": r"procedure",
    "CALL": r"call",
    "WHILE": r"while",
    "IF": r'if',
    'THEN': r'then',
    'ELSE': r'else',
    'PRINT': r"print",
}

for k, v in keywords.items():
    lg.add(k, f"{v}(?![a-zA-Z0-9_])")

lg.ignore(r"\s+")
lg.add("NAME", r"[A-Za-z][A-Za-z0-9]*")
lg.add("NUMBER", r"\d+")

lexer = lg.build()
