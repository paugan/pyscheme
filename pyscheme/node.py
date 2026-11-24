from abc import ABC
from typing import Any, override

OPEN_PARENTHESIS = 1
CLOSE_PARENTHESIS = 2
IDENTIFIER = 3
STRING_LITERAL = 4
NUMBER_LITERAL = 5

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
