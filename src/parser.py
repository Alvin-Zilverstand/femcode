class AST:
    pass

class Number(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value

class String(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value

class BinOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right

class Comparison(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
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

class Block(AST):
    def __init__(self, statements):
        self.statements = statements

class IfStatement(AST):
    def __init__(self, condition, if_block, else_block=None):
        self.condition = condition
        self.if_block = if_block
        self.else_block = else_block

class WhileStatement(AST):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

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

        if token.type == 'FEMBOY_FEMININE':
            return self.parse_if_statement()

        if token.type == 'OTOKONOKO':
            return self.parse_while_statement()

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

    def parse_if_statement(self):
        self.get_next_token() # Consume FEMBOY_FEMININE

        condition = self.expression()

        # Expect Femboycore to start the if block
        if self.peek_next_token().type != 'FEMBOYCORE':
            raise Exception("Expected 'Femboycore' to start if block")
        self.get_next_token() # Consume FEMBOYCORE

        if_block_statements = []
        while self.peek_next_token().type != 'PERIODT':
            if self.peek_next_token().type == 'EOF':
                raise Exception("Unterminated if block: Expected 'Periodt'")
            if_block_statements.append(self.parse_statement())
        self.get_next_token() # Consume PERIODT
        if_block = Block(if_block_statements)

        else_block = None
        if self.peek_next_token().type == 'ANDROGYNY':
            self.get_next_token() # Consume ANDROGYNY
            # Expect Femboycore to start the else block
            if self.peek_next_token().type != 'FEMBOYCORE':
                raise Exception("Expected 'Femboycore' to start else block")
            self.get_next_token() # Consume FEMBOYCORE

            else_block_statements = []
            while self.peek_next_token().type != 'PERIODT':
                if self.peek_next_token().type == 'EOF':
                    raise Exception("Unterminated else block: Expected 'Periodt'")
                else_block_statements.append(self.parse_statement())
            self.get_next_token() # Consume PERIODT
            else_block = Block(else_block_statements)

        return IfStatement(condition, if_block, else_block)

    def parse_while_statement(self):
        self.get_next_token() # Consume OTOKONOKO

        condition = self.expression()

        if self.peek_next_token().type != 'FEMBOYCORE':
            raise Exception("Expected 'Femboycore' to start while loop body")
        self.get_next_token() # Consume FEMBOYCORE

        body_statements = []
        while self.peek_next_token().type != 'PERIODT':
            if self.peek_next_token().type == 'EOF':
                raise Exception("Unterminated while loop: Expected 'Periodt'")
            body_statements.append(self.parse_statement())
        self.get_next_token() # Consume PERIODT
        body = Block(body_statements)

        return WhileStatement(condition, body)

    def factor(self):
        token = self.get_next_token()
        if token.type == 'INTEGER':
            return Number(token)
        elif token.type == 'STRING':
            return String(token) # Now returns a String AST node
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

        # Handle addition/subtraction
        while self.peek_next_token().type in ('PLUS', 'MINUS'):
            token = self.get_next_token()
            node = BinOp(left=node, op=token, right=self.term())

        # Handle comparisons
        if self.peek_next_token().type in ('EQ', 'NEQ', 'GT', 'GTE', 'LT', 'LTE'):
            op_token = self.get_next_token()
            right_node = self.expression() # Recursively parse right side of comparison
            node = Comparison(left=node, op=op_token, right=right_node)

        return node