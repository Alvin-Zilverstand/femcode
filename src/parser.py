class AST:
    pass

class Number(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value

class BinOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right

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
            # This case should be handled by expression parsing if it's part of an expression
            # For now, raise an error if it's a standalone ID not part of assignment or print
            raise Exception(f"Unexpected identifier '{token.value}' without assignment or print.")

        # Handle expressions as statements (e.g., just a number or an arithmetic operation)
        # This might need refinement depending on what we consider a valid standalone statement
        # For now, let's assume expressions are only part of print or assignment
        raise Exception(f"Invalid statement starting with token {token.type}")

    def parse_print_statement(self):
        self.get_next_token()  # Consume PRINT token
        expr = self.expression()
        return Print(expr)

    def parse_assignment_statement(self):
        var_token = self.get_next_token()
        var_node = Variable(var_token)
        
        assign_token = self.get_next_token()

        right_expr = self.expression()
        return Assign(left=var_node, op=assign_token, right=right_expr)

    def factor(self):
        token = self.get_next_token()
        if token.type == 'INTEGER':
            return Number(token)
        elif token.type == 'STRING':
            return token.value # Strings are literals, not AST nodes for now
        elif token.type == 'ID':
            return Variable(token)
        else:
            raise Exception(f"Expected integer, string or identifier, got {token.type}")

    def term(self):
        node = self.factor()
        while self.peek_next_token().type in ('MUL', 'DIV'):
            token = self.get_next_token()
            node = BinOp(left=node, op=token, right=self.factor())
        return node

    def expression(self):
        node = self.term()
        while self.peek_next_token().type in ('PLUS', 'MINUS'):
            token = self.get_next_token()
            node = BinOp(left=node, op=token, right=self.term())
        return node
