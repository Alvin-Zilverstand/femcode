import re

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f'Token({self.type}, {self.value!r})'

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0

    def error(self):
        raise Exception('Invalid character')

    def get_next_token(self):
        if self.pos > len(self.text) - 1:
            return Token('EOF', None)

        current_char = self.text[self.pos]

        if current_char.isspace():
            self.pos += 1
            return self.get_next_token()

        if current_char == '"':
            self.pos += 1
            string_end = self.text.find('"', self.pos)
            if string_end == -1:
                self.error()
            string = self.text[self.pos:string_end]
            self.pos = string_end + 1
            return Token('STRING', string)

        if re.match(r'\bUwU Boy\b', self.text[self.pos:]):
            self.pos += 7
            return Token('PRINT', 'UwU Boy')

        self.error()

    def tokenize(self):
        tokens = []
        while True:
            token = self.get_next_token()
            tokens.append(token)
            if token.type == 'EOF':
                break
        return tokens
