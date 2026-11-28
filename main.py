from pyscheme.lexer import Lexer

lexer = Lexer('''
;this is a first comment.
;this is a second comment.

#|
  the FACT procedure computes the factorial
  of a non-negative integer.
|#

#!no-fold-case

(display 30)
(display +30)
(display -30)
(display 3.14)
(display +3.14)
(display -3.14)
(display .11)
(display +.11)
(display -.11)
(display '(10 20 30))
(display `('(10 20 30)))
(display ,@(list 10 20 30))
(display #t)
(display #f)
(display #\\C)
(display #\\ )
(display #\\alarm)
(display #\\newline)
(display #\\tab)
''')

lexer.lex()

tokens = list(map(lambda x: [str(x), x.value()], lexer.tokens()))

for el in tokens:
    print(el)
