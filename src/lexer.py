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
        self.token_patterns = [
            (r'"[^"]*"', 'STRING'), # Double-quoted string literals
            (r"'[^']*'", 'STRING'), # Single-quoted string literals
            (r'\d+\.\d+', 'FLOAT'), # Floating-point numbers
            (r'\d+', 'INTEGER'), # Integer numbers

            (r'\+\+', 'INCREMENT'),
            (r'--', 'DECREMENT'),
            (r'\+=', 'PLUS_ASSIGN'),
            (r'-=', 'MINUS_ASSIGN'),
            (r'\*=', 'MUL_ASSIGN'),
            (r'/=', 'DIV_ASSIGN'),
            (r'==', 'EQ'),
            (r'!=', 'NEQ'),
            (r'>=', 'GTE'),
            (r'<=', 'LTE'),

            (r'\(', 'LPAREN'),
            (r'\)', 'RPAREN'),
            (r'\[', 'LBRACKET'),
            (r'\]', 'RBRACKET'),
            (r'{', 'LBRACE'),
            (r'}', 'RBRACE'),
            (r':', 'COLON'),
            (r'\.', 'DOT'),
            (r'\+', 'PLUS'),
            (r'-', 'MINUS'),
            (r'\*', 'MUL'),
            (r'/', 'DIV'),
            (r',', 'COMMA'),
            (r'=', 'ASSIGN'),
            (r'!', 'NOT'),
            (r'>', 'GT'),
            (r'<', 'LT'),

            (r'\bFemboy Feminine\b', 'FEMBOY_FEMININE'),
            (r'\bUwU Boy\b', 'PRINT'),
            (r'\bAndrogyny\b', 'ANDROGYNY'),
            (r'\bOtokonoko\b', 'OTOKONOKO'),
            (r'\bFemboy\b', 'FUNCTION_DEF'),
            (r'\bFemme\b', 'RETURN'),
            (r'\bFemboycore\b', 'FEMBOYCORE'),
            (r'\bPeriodt\b', 'PERIODT'),
            (r'\bKawaii\b', 'KAWAII'),
            (r'\bCringe\b', 'CRINGE'),
            (r'\bGhosted\b', 'NULL'),
            (r'\bTomgirl\b', 'FOR'),
            (r'\bSlay\b', 'PASS'),
            (r'\bBreak\b', 'BREAK'),
            (r'\bContinue\b', 'CONTINUE'),
            (r'\bTwink\b', 'TRY'),
            (r'\bBimboy\b', 'EXCEPT'),
            (r'\band\b', 'AND'),
            (r'\bor\b', 'OR'),
            (r'\bnot\b', 'NOT'),
            (r'\bis\b', 'ASSIGN'), # 'is' is now a keyword for assignment
            (r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', 'ID'), # Identifiers
        ]

    def error(self, message="Invalid character"):
        raise Exception(f"{message} at position {self.pos}: '{self.text[self.pos]}'")

    def get_next_token(self):
        while self.pos < len(self.text):
            # 1. Consume whitespace and comments
            self.skip_whitespace_and_comments()

            # If we've reached the end after skipping, return EOF
            if self.pos >= len(self.text):
                return Token('EOF', None)

            longest_match = None
            matched_type = None

            # 2. Match tokens
            for pattern, token_type in self.token_patterns:
                match = re.match(pattern, self.text[self.pos:], re.IGNORECASE if token_type == 'ID' else 0)
                if match:
                    if longest_match is None or len(match.group(0)) > len(longest_match.group(0)):
                        longest_match = match
                        matched_type = token_type
            
            if longest_match:
                value = longest_match.group(0)
                self.pos += len(value)
                if matched_type == 'INTEGER':
                    return Token(matched_type, int(value))
                elif matched_type == 'FLOAT':
                    return Token(matched_type, float(value))
                elif matched_type == 'KAWAII':
                    return Token(matched_type, True)
                elif matched_type == 'CRINGE':
                    return Token(matched_type, False)
                elif matched_type == 'NULL':
                    return Token(matched_type, None)
                else:
                    return Token(matched_type, value)
            else:
                self.error()

        return Token('EOF', None)

    def skip_whitespace_and_comments(self):
        while self.pos < len(self.text):
            # Try to match whitespace
            whitespace_match = re.match(r'\s+', self.text[self.pos:])
            if whitespace_match:
                self.pos += len(whitespace_match.group(0))
                continue

            # Try to match comments
            comment_match = re.match(r'#.*(?:\n|$)', self.text[self.pos:])
            if comment_match:
                self.pos += len(comment_match.group(0))
                continue
            
            # If neither whitespace nor comment, break the loop
            break

    def tokenize(self):
        tokens = []
        while True:
            token = self.get_next_token()
            tokens.append(token)
            if token.type == 'EOF':
                break
        return tokens