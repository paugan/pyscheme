from abc import ABC
from typing import Any, override

OPEN_PARENTHESIS = 1
CLOSE_PARENTHESIS = 2
IDENTIFIER = 3
STRING_LITERAL = 4
NUMBER_LITERAL = 5
PIPE_SCOPED_IDENTIFIER = 6
DIRECTIVE = 7
LINE_COMMENT = 8
BLOCK_COMMENT = 9
APOSTROPHE = 10
BACKQUOTE = 11
COMMA = 12
SHELL = 13
OPEN_SQUARE_BRACE = 14
CLOSE_SQUARE_BRACE = 15
OPEN_CURLY_BRACE = 16
CLOSE_CURLY_BRACE = 17
BOOLEAN_LITERAL = 18
CHAR_CONST = 19

class Node(ABC):
    def __init__(self, ntype: int, value: Any):
        self._ntype: int = ntype
        self._value: Any = value

    def ntype(self) -> int:
        return self._ntype

    def value(self) -> Any:
        return self._value

    def __str__(self) -> str:
        pass

class OpenParenthesis(Node):
    def __init__(self):
        super().__init__(OPEN_PARENTHESIS, None)

    @override
    def __str__(self) -> str:
        return '(open parenthesis)'

class CloseParenthesis(Node):
    def __init__(self):
        super().__init__(CLOSE_PARENTHESIS, None)

    @override
    def __str__(self) -> str:
        return '(close parenthesis)'

class Identifier(Node):
    def __init__(self, value: str):
        super().__init__(IDENTIFIER, value)

    @override
    def __str__(self) -> str:
        return '(identifier)'

class StringLiteral(Node):
    def __init__(self, value: str):
        super().__init__(STRING_LITERAL, value)

    @override
    def __str__(self) -> str:
        return '(string literal)'

class NumberLiteral(Node):
    def __init__(self, value: str):
        super().__init__(NUMBER_LITERAL, value)

    @override
    def __str__(self) -> str:
        return '(number literal)'

class PipeScopedIdentifier(Node):
    def __init__(self, value: str):
        super().__init__(PIPE_SCOPED_IDENTIFIER, value)

    @override
    def __str__(self) -> str:
        return '(pipe-scoped identifier)'

class Directive(Node):
    def __init__(self, value: str):
        super().__init__(DIRECTIVE, value)

    @override
    def __str__(self) -> str:
        return '(directive)'

class LineComment(Node):
    def __init__(self, value: str):
        super().__init__(LINE_COMMENT, value)

    @override
    def __str__(self) -> str:
        return '(line comment)'

class BlockComment(Node):
    def __init__(self, value: str):
        super().__init__(BLOCK_COMMENT, value)

    @override
    def __str__(self) -> str:
        return '(block comment)'

class Apostrophe(Node):
    def __init__(self):
        super().__init__(APOSTROPHE, None)

    @override
    def __str__(self) -> str:
        return '(apostrophe)'

class Backquote(Node):
    def __init__(self):
        super().__init__(BACKQUOTE, None)

    @override
    def __str__(self) -> str:
        return '(backquote)'

class Comma(Node):
    def __init__(self):
        super().__init__(COMMA, None)

    @override
    def __str__(self) -> str:
        return '(comma)'

class Shell(Node):
    def __init__(self):
        super().__init__(SHELL, None)

    @override
    def __str__(self) -> str:
        return '(shell)'

class OpenSquareBrace(Node):
    def __init__(self):
        super().__init__(OPEN_SQUARE_BRACE, None)

    @override
    def __str__(self) -> str:
        return '(open-square-brace)'

class CloseSquareBrace(Node):
    def __init__(self):
        super().__init__(CLOSE_SQUARE_BRACE, None)

    @override
    def __str__(self) -> str:
        return '(close-square-brace)'

class OpenCurlyBrace(Node):
    def __init__(self):
        super().__init__(OPEN_CURLY_BRACE, None)

    @override
    def __str__(self) -> str:
        return '(open-curly-brace)'

class CloseCurlyBrace(Node):
    def __init__(self):
        super().__init__(CLOSE_CURLY_BRACE, None)

    @override
    def __str__(self) -> str:
        return '(close-curly-brace)'

class BooleanLiteral(Node):
    def __init__(self, value: bool):
        super().__init__(BOOLEAN_LITERAL, value)

    @override
    def __str__(self) -> str:
        return '(boolean literal)'

class CharConst(Node):
    def __init__(self, value: str):
        super().__init__(CHAR_CONST, value)

    @override
    def __str__(self) -> str:
        return '(char const)'
