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

        # Skip whitespace
        while self.pos < len(self.text) and self.text[self.pos].isspace():
            self.pos += 1

        if self.pos > len(self.text) - 1:
            return Token('EOF', None)

        current_char = self.text[self.pos]

        if current_char == '"':
            self.pos += 1
            string_end = self.text.find('"', self.pos)
            if string_end == -1:
                self.error()
            string = self.text[self.pos:string_end]
            self.pos = string_end + 1
            return Token('STRING', string)

        if current_char.isdigit():
            start_pos = self.pos
            while self.pos < len(self.text) and self.text[self.pos].isdigit():
                self.pos += 1
            return Token('INTEGER', int(self.text[start_pos:self.pos]))

        if current_char == '+':
            self.pos += 1
            return Token('PLUS', '+')
        if current_char == '-':
            self.pos += 1
            return Token('MINUS', '-')
        if current_char == '*':
            self.pos += 1
            return Token('MUL', '*')
        if current_char == '/':
            self.pos += 1
            return Token('DIV', '/')

        # Match keywords
        if re.match(r'\bUwU Boy\b', self.text[self.pos:]):
            self.pos += 7
            return Token('PRINT', 'UwU Boy')
        if re.match(r'\bis\b', self.text[self.pos:]):
            self.pos += 2
            return Token('ASSIGN', 'is')

        # Match identifiers
        match = re.match(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', self.text[self.pos:])
        if match:
            value = match.group(0)
            self.pos += len(value)
            return Token('ID', value)

        self.error()

    def tokenize(self):
        tokens = []
        while True:
            token = self.get_next_token()
            tokens.append(token)
            if token.type == 'EOF':
                break
        return tokens
