class AST:
    pass

class Print(AST):
    def __init__(self, value):
        self.value = value

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def get_next_token(self):
        if self.pos < len(self.tokens):
            token = self.tokens[self.pos]
            self.pos += 1
            return token
        return None

    def parse(self):
        statements = []
        while True:
            token = self.get_next_token()
            if token is None or token.type == 'EOF':
                break

            if token.type == 'PRINT':
                next_token = self.get_next_token()
                if next_token.type == 'STRING':
                    statements.append(Print(next_token.value))
                else:
                    raise Exception("Expected a string after 'UwU Boy'")
            else:
                raise Exception(f"Unexpected token: {token.type}")

        return statements
