WORD, EOF = 'WORD', 'EOF'
QUOTE = '"'


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

    PUNCTUATION = {':', '-', ';', '!', '?'}

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

    def skip_punctuation(self):
        while self.current_char is not None and self.current_char in self.PUNCTUATION:
            self.advance()

    def word(self):
        s = ''
        while self.current_char is not None and not self.current_char.isspace():
            s += self.current_char
            self.advance()
        # TODO: Process the word, because it could have trailing punctuation
        return s

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            if self.current_char in self.PUNCTUATION:
                self.skip_punctuation()
                continue
            if self.current_char == QUOTE:
                return Token(QUOTE, '"')
            if self.current_char.isalpha():
                return Token(WORD, self.word())
            self.error()
        return Token(EOF, None)


class Interpreter:

    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = None

    def error(self):
        raise Exception('Invalid syntax')

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def term(self):
        pass

    def expr(self):
        pass

