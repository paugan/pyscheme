from pyscheme.lexer import Lexer

lexer = Lexer('(define (|\\x9;\\x9;abc| a b) (+ a b))')
lexer.lex()

tokens = list(map(lambda x: [str(x), x.value()], lexer.tokens()))

for el in tokens:
    print(el)
