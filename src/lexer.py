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
            string_start = self.pos
            while self.pos < len(self.text) and self.text[self.pos] != '"':
                self.pos += 1
            string_value = self.text[string_start:self.pos]
            self.pos += 1 # Consume closing quote
            return Token('STRING', string_value)

        if current_char.isdigit():
            start_pos = self.pos
            while self.pos < len(self.text) and self.text[self.pos].isdigit():
                self.pos += 1
            return Token('INTEGER', int(self.text[start_pos:self.pos]))

        # Parentheses
        if current_char == '(':
            self.pos += 1
            return Token('LPAREN', '(')
        if current_char == ')':
            self.pos += 1
            return Token('RPAREN', ')')

        # Operators
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
        if current_char == ',':
            self.pos += 1
            return Token('COMMA', ',')
        if current_char == '=':
            if self.pos + 1 < len(self.text) and self.text[self.pos + 1] == '=':
                self.pos += 2
                return Token('EQ', '==')
        if current_char == '!':
            if self.pos + 1 < len(self.text) and self.text[self.pos + 1] == '=':
                self.pos += 2
                return Token('NEQ', '!=')
        if current_char == '>':
            if self.pos + 1 < len(self.text) and self.text[self.pos + 1] == '=':
                self.pos += 2
                return Token('GTE', '>=')
            else:
                self.pos += 1
                return Token('GT', '>')
        if current_char == '<':
            if self.pos + 1 < len(self.text) and self.text[self.pos + 1] == '=':
                self.pos += 2
                return Token('LTE', '<=')
            else:
                self.pos += 1
                return Token('LT', '<')

        # Match keywords (longer ones first)
        if re.match(r'\bFemboy Feminine\b', self.text[self.pos:]):
            self.pos += len('Femboy Feminine')
            return Token('FEMBOY_FEMININE', 'Femboy Feminine')
        if re.match(r'\bUwU Boy\b', self.text[self.pos:]):
            self.pos += 7
            return Token('PRINT', 'UwU Boy')
        if re.match(r'\bAndrogyny\b', self.text[self.pos:]):
            self.pos += len('Androgyny')
            return Token('ANDROGYNY', 'Androgyny')
        if re.match(r'\bOtokonoko\b', self.text[self.pos:]):
            self.pos += len('Otokonoko')
            return Token('OTOKONOKO', 'Otokonoko')
        if re.match(r'\bFemboy\b', self.text[self.pos:]):
            self.pos += len('Femboy')
            return Token('FUNCTION_DEF', 'Femboy')
        if re.match(r'\bFemme\b', self.text[self.pos:]):
            self.pos += len('Femme')
            return Token('RETURN', 'Femme')
        if re.match(r'\bis\b', self.text[self.pos:]):
            self.pos += 2
            return Token('ASSIGN', 'is')
        if re.match(r'\bFemboycore\b', self.text[self.pos:]):
            self.pos += len('Femboycore')
            return Token('FEMBOYCORE', 'Femboycore')
        if re.match(r'\bPeriodt\b', self.text[self.pos:]):
            self.pos += len('Periodt')
            return Token('PERIODT', 'Periodt')
        if re.match(r'\bKawaii\b', self.text[self.pos:]):
            self.pos += len('Kawaii')
            return Token('KAWAII', True)
        if re.match(r'\bCringe\b', self.text[self.pos:]):
            self.pos += len('Cringe')
            return Token('CRINGE', False)

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