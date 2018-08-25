WORD, EOF = 'WORD', 'EOF'
QUOTE_OPEN, QUOTE_CLOSE, SPACE = 'QUOTE_OPEN', 'QUOTE_CLOSE', 'SPACE'


class Token:

    def __init__(self, token_type, value):
        self.type = token_type
        self.value = value

    def __str__(self):
        return "Token({type}, {value})".format(
            type=self.type,
            value=self.value
        )

    def __repr__(self):
        return self.__str__()


class Lexer:

    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception('Invalid character')

    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def word(self):
        s = []
        while self.current_char is not None \
                and not self.current_char.isspace() \
                and self.current_char != '”':
            s.append(self.current_char)
            self.advance()
        # TODO: Process the word, because it could have trailing punctuation
        return ''.join(s)

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                return Token(SPACE, ' ')
            if self.current_char == '“':
                self.advance()
                return Token(QUOTE_OPEN, '“')
            if self.current_char == "”":
                self.advance()
                return Token(QUOTE_CLOSE, "”")
            if self.current_char.isalpha():
                return Token(WORD, self.word())
            self.error()
        return Token(EOF, None)


class Interpreter:

    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception('Invalid syntax')

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def term(self):
        token = self.current_token
        if token.type == WORD:
            self.eat(WORD)
            return token.value
        elif token.type == QUOTE_OPEN:
            self.eat(QUOTE_OPEN)
            result = self.expr()
            self.eat(QUOTE_CLOSE)
            return result

    def expr(self):
        s = [self.term()]

        while self.current_token.type == SPACE:
            self.eat(SPACE)
            s += [self.term()]

        return s


if __name__ == '__main__':
    h1 = 'Tesla ends flirtation with going private as Elon Musk cites belief that company is “better off”'
    lexer = Lexer(h1)
    interpreter = Interpreter(lexer)
    result = interpreter.expr()
    print(result)
