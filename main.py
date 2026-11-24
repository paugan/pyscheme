from pyscheme.lexer import Lexer

lexer = Lexer('(display "foobarbaz")')
lexer.lex()

tokens = list(map(lambda x: [str(x), x.value()], lexer.tokens()))

for el in tokens:
    print(el)
