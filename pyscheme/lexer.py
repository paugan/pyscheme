import string
from typing import List

from pyscheme.error import (
    MalformedFloatingPointError,
    UnterminatedStringLiteralError,
    UnterminatedPipeScopedIdentifier,
    MalformedHexadecimalEscape
)

from pyscheme.node import (
	Node,
    OpenParenthesis,
    CloseParenthesis,
    Identifier,
    StringLiteral,
    NumberLiteral,
    PipeScopedIdentifier
)

class Lexer:
    def __init__(self, buf: str):
        self._buf: str = buf
        self._pos: int = 0
        self._tokens: List[Node] = []

    def lex(self) -> None:
        while True:
            if self._is_eof():
                break

            if self._current() == '(':
                self._match_open_parenthesis()
                continue

            if self._current() == ')':
                self._match_close_parenthesis()
                continue

            if self._current() == '"':
                self._match_string_literal()
                continue

            if self._is_digit():
                self._match_number_literal()
                continue

            if self._current() == '|':
                self._match_pipe_scoped_identifier()
                continue

            if self._current() == '.':
                if self._peek() in string.digits:
                    self._match_number_literal()
                    continue

            if self._is_identifier():
                self._match_identifier()
                continue

            self._advance()

    def tokens(self) -> List[Node]:
        return self._tokens

    def _is_eof(self) -> bool:
        return self._pos >= len(self._buf)

    def _current(self) -> str | None:
        return None if self._is_eof() else self._buf[self._pos]

    def _peek(self, depth: int = 1) -> str | None:
        if self._pos + depth >= len(self._buf):
            return None

        return self._buf[self._pos + depth]

    def _is_digit(self) -> bool:
        return self._current() in string.digits

    def _is_hexdigit(self) -> bool:
        return self._current() in string.hexdigits

    def _is_identifier(self) -> bool:
        return self._current() in ''.join([
            string.digits,
            string.ascii_lowercase,
            string.ascii_uppercase,
            '!$%&*+-./:<=>?@^_~'
        ])

    def _advance(self) -> None:
        self._pos += 1

    def _match_open_parenthesis(self) -> None:
        self._tokens.append(OpenParenthesis())
        self._advance()

    def _match_close_parenthesis(self) -> None:
        self._tokens.append(CloseParenthesis())
        self._advance()

    def _match_string_literal(self) -> None:
        start = self._current()

        # if peeked next character is equal to dquote
        # then advance bufptr by 2 and give empty string
        # as a parameter for 'StringLiteral' constructor.
        if self._peek() == start:
            self._advance()
            self._advance()
            self._tokens.append(StringLiteral(''))
            return None

        self._advance()

        buf, end = '', ''

        while True:
            if self._is_eof():
                break

            if self._current() == start:
                end = self._current()
                self._advance()
                break

            buf += self._current()
            self._advance()

        if end != start:
            raise UnterminatedStringLiteralError('unterminated string literal')

        self._tokens.append(StringLiteral(buf))

    def _match_number_literal(self) -> None:
        buf = self._current()
        cdot = 0 if self._is_digit() else 1

        self._advance()

        while True:
            if self._is_eof() or \
                (not self._is_digit() and self._current() != '.'):
                break

            if self._current() == '.':
                cdot += 1

            buf += self._current()
            self._advance()

        if cdot > 1:
            raise MalformedFloatingPointError('malformed floating-point number')

        num = int(buf) if '.' not in buf else float(buf)

        self._tokens.append(NumberLiteral(num))

    def _match_identifier(self) -> None:
        buf = self._current()

        self._advance()

        while True:
            if self._is_eof() or not self._is_identifier():
                break

            buf += self._current()
            self._advance()

        self._tokens.append(Identifier(buf))

    def _match_pipe_scoped_identifier(self) -> None:
        start = self._current()

        if self._peek() == start:
            self._advance()
            self._advance()
            self._tokens.append(PipeScopedIdentifier(''))
            return None

        self._advance()

        buf, end, tmp = '', '', ''

        while True:
            if self._is_eof():
                break

            if self._current() == start:
                end = self._current()
                self._advance()
                break

            if self._current() == '\\' and self._peek() == 'x':
                self._advance()
                self._advance()

                while True:
                    if self._is_eof() or self._current() == ';':
                        if self._current() == ';':
                            self._advance()

                        break

                    tmp += self._current().lower()
                    self._advance()

                if self._peek(depth=-1) != ';':
                    raise MalformedHexadecimalEscape(
                        'every hex-escape must be terminated by \';\''
                    )

                try:
                    buf += chr(int('0x' + tmp, 16))
                except ValueError as e:
                    raise MalformedHexadecimalEscape('malformed hexadecimal escape') from e

                tmp = ''
                continue

            buf += self._current()
            self._advance()

        if end != start:
            raise UnterminatedPipeScopedIdentifier('malformed pipe-scoped identifier')

        self._tokens.append(PipeScopedIdentifier(buf))
