class AST:
    pass

class Print(AST):
    def __init__(self, value):
        self.value = value

class Assign(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Variable(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def get_next_token(self):
        if self.pos < len(self.tokens):
            token = self.tokens[self.pos]
            self.pos += 1
            return token
        return Token('EOF', None)

    def peek_next_token(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return Token('EOF', None)

    def parse(self):
        statements = []
        while self.peek_next_token().type != 'EOF':
            statements.append(self.parse_statement())
        return statements

    def parse_statement(self):
        token = self.peek_next_token()

        if token.type == 'PRINT':
            return self.parse_print_statement()

        if token.type == 'ID' and self.pos + 1 < len(self.tokens) and self.tokens[self.pos + 1].type == 'ASSIGN':
            return self.parse_assignment_statement()
        elif token.type == 'ID':
            raise Exception(f"Unexpected identifier '{token.value}' without assignment.")

        raise Exception(f"Invalid statement starting with token {token.type}")

    def parse_print_statement(self):
        self.get_next_token()  # Consume PRINT token
        token = self.get_next_token()
        if token.type == 'STRING':
            return Print(token.value)
        elif token.type == 'ID':
            return Print(Variable(token))
        else:
            raise Exception("Expected a string or variable after 'UwU Boy'")

    def parse_assignment_statement(self):
        var_token = self.get_next_token()
        var_node = Variable(var_token)
        
        assign_token = self.get_next_token()

        value_token = self.get_next_token()
        if value_token.type == 'STRING':
            return Assign(left=var_node, op=assign_token, right=value_token.value)
        else:
            raise Exception("Expected a string value for assignment")
