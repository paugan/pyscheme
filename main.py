from pyscheme.lexer import Lexer

lexer = Lexer('''
;this is a first comment.
;this is a second comment.

#|
  the FACT procedure computes the factorial
  of a non-negative integer.
|#

#!no-fold-case

(|two\\x20;words| 10 20 3.14159)''')

lexer.lex()

tokens = list(map(lambda x: [str(x), x.value()], lexer.tokens()))

for el in tokens:
    print(el)
