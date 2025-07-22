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

class Boolean(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value

class LogicalOp(AST):
    def __init__(self, left, op, right=None):
        self.left = left
        self.op = op
        self.right = right

class UnaryOp(AST):
    def __init__(self, op, right):
        self.op = op
        self.right = right

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

class ForStatement(AST):
    def __init__(self, var_name, iterable, body):
        self.var_name = var_name
        self.iterable = iterable
        self.body = body

class BreakStatement(AST):
    pass

class ContinueStatement(AST):
    pass

class TryExceptStatement(AST):
    def __init__(self, try_block, except_block):
        self.try_block = try_block
        self.except_block = except_block

class FunctionDefinition(AST):
    def __init__(self, name, parameters, body):
        self.name = name
        self.parameters = parameters
        self.body = body

class FunctionCall(AST):
    def __init__(self, name, arguments):
        self.name = name
        self.arguments = arguments

class ReturnStatement(AST):
    def __init__(self, value):
        self.value = value

class List(AST):
    def __init__(self, elements):
        self.elements = elements

class IndexAccess(AST):
    def __init__(self, target, index):
        self.target = target
        self.index = index

class Dictionary(AST):
    def __init__(self, pairs):
        self.pairs = pairs # List of (key_expr, value_expr) tuples

class PropertyAccess(AST):
    def __init__(self, target, property_name):
        self.target = target
        self.property_name = property_name

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def get_current_token(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return Token('EOF', None)

    def consume(self, token_type):
        if self.get_current_token().type == token_type:
            self.pos += 1
        else:
            raise Exception(f"Expected {token_type}, got {self.get_current_token().type}")

    def parse(self):
        statements = []
        while self.get_current_token().type != 'EOF':
            statements.append(self.parse_statement())
        return statements

    def parse_statement(self):
        token = self.get_current_token()

        if token.type == 'PRINT':
            return self.parse_print_statement()

        if token.type == 'ID':
            # Check for assignment
            if self.pos + 1 < len(self.tokens) and self.tokens[self.pos + 1].type == 'ASSIGN':
                return self.parse_assignment_statement()
            # Check for function call as a statement
            if self.pos + 1 < len(self.tokens) and self.tokens[self.pos + 1].type == 'LPAREN':
                # Consume the ID token first, then parse the function call
                name_token = self.get_current_token()
                self.consume('ID') # Consume the ID token
                return self.parse_function_call(name_token)

        if token.type == 'FEMBOY_FEMININE':
            return self.parse_if_statement()

        if token.type == 'OTOKONOKO':
            return self.parse_while_statement()

        if token.type == 'FOR':
            return self.parse_for_statement()

        if token.type == 'FUNCTION_DEF':
            return self.parse_function_definition()

        if token.type == 'RETURN':
            return self.parse_return_statement()

        if token.type == 'PASS':
            self.consume('PASS')
            return Block([]) # A pass statement is an empty block

        if token.type == 'BREAK':
            self.consume('BREAK')
            return BreakStatement()

        if token.type == 'CONTINUE':
            self.consume('CONTINUE')
            return ContinueStatement()

        if token.type == 'TRY':
            return self.parse_try_except_statement()

        raise Exception(f"Invalid statement starting with token {token.type}")

    def parse_print_statement(self):
        self.consume('PRINT')
        expr = self.expression()
        return Print(expr)

    def parse_assignment_statement(self):
        var_token = self.get_current_token()
        self.consume('ID')
        var_node = Variable(var_token)
        
        self.consume('ASSIGN')

        right_expr = self.expression()
        assign_token = self.tokens[self.pos - 1] # Get the consumed ASSIGN token
        return Assign(left=var_node, op=assign_token, right=right_expr)

    def parse_if_statement(self):
        self.consume('FEMBOY_FEMININE')

        condition = self.expression()

        self.consume('FEMBOYCORE')

        if_block_statements = []
        while self.get_current_token().type != 'PERIODT':
            if self.get_current_token().type == 'EOF':
                raise Exception("Unterminated if block: Expected 'Periodt'")
            if_block_statements.append(self.parse_statement())
        self.consume('PERIODT')
        if_block = Block(if_block_statements)

        else_block = None
        if self.get_current_token().type == 'ANDROGYNY':
            self.consume('ANDROGYNY')
            self.consume('FEMBOYCORE')

            else_block_statements = []
            while self.get_current_token().type != 'PERIODT':
                if self.get_current_token().type == 'EOF':
                    raise Exception("Unterminated else block: Expected 'Periodt'")
                else_block_statements.append(self.parse_statement())
            self.consume('PERIODT')
            else_block = Block(else_block_statements)

        return IfStatement(condition, if_block, else_block)

    def parse_while_statement(self):
        self.consume('OTOKONOKO')

        condition = self.expression()

        self.consume('FEMBOYCORE')

        body_statements = []
        while self.get_current_token().type != 'PERIODT':
            if self.get_current_token().type == 'EOF':
                raise Exception("Unterminated while loop: Expected 'Periodt'")
            body_statements.append(self.parse_statement())
        self.consume('PERIODT')
        body = Block(body_statements)

        return WhileStatement(condition, body)

    def parse_for_statement(self):
        self.consume('FOR')
        var_name_token = self.get_current_token()
        self.consume('ID')
        self.consume('ASSIGN') # Using ASSIGN for 'in' for now, will refine later
        iterable_expr = self.expression()

        self.consume('FEMBOYCORE')

        body_statements = []
        while self.get_current_token().type != 'PERIODT':
            if self.get_current_token().type == 'EOF':
                raise Exception("Unterminated for loop: Expected 'Periodt'")
            body_statements.append(self.parse_statement())
        self.consume('PERIODT')
        body = Block(body_statements)

        return ForStatement(var_name_token.value, iterable_expr, body)

    def parse_function_definition(self):
        self.consume('FUNCTION_DEF')
        name_token = self.get_current_token()
        self.consume('ID')
        
        # Parse parameters
        parameters = []
        if self.get_current_token().type == 'LPAREN':
            self.consume('LPAREN')
            while self.get_current_token().type != 'RPAREN':
                param_token = self.get_current_token()
                self.consume('ID')
                parameters.append(param_token.value)
                if self.get_current_token().type == 'COMMA':
                    self.consume('COMMA')
            self.consume('RPAREN')
            

        self.consume('FEMBOYCORE')

        body_statements = []
        while self.get_current_token().type != 'PERIODT':
            if self.get_current_token().type == 'EOF':
                raise Exception("Unterminated function definition: Expected 'Periodt'")
            body_statements.append(self.parse_statement())
        self.consume('PERIODT')
        body = Block(body_statements)

        return FunctionDefinition(name_token.value, parameters, body)

    def parse_return_statement(self):
        self.consume('RETURN')
        value = self.expression()
        return ReturnStatement(value)

    def factor(self):
        token = self.get_current_token()
        if token.type == 'INTEGER':
            self.consume('INTEGER')
            return Number(token)
        elif token.type == 'FLOAT':
            self.consume('FLOAT')
            return Number(token) # Using Number AST for both int and float for now
        elif token.type == 'STRING':
            self.consume('STRING')
            return String(token)
        elif token.type == 'KAWAII' or token.type == 'CRINGE':
            self.consume(token.type)
            return Boolean(token)
        elif token.type == 'NULL':
            self.consume('NULL')
            return Null()
        elif token.type == 'ID':
            # Consume the ID token first
            self.consume('ID')
            # Now check what follows the ID
            next_token = self.get_current_token()
            if next_token.type == 'LPAREN':
                # It's a function call
                return self.parse_function_call(token)
            elif next_token.type == 'DOT':
                # It's a property access
                return self.parse_property_access(Variable(token)) # Pass Variable node as target
            elif next_token.type == 'LBRACKET':
                # It's an index access
                return self.parse_index_access(Variable(token))
            else:
                # It's a simple variable
                return Variable(token)
        elif token.type == 'LPAREN': # Handle parenthesized expressions
            self.consume('LPAREN')
            node = self.expression()
            self.consume('RPAREN')
            return node
        elif token.type == 'LBRACKET': # Handle list literals
            return self.parse_list_literal()
        elif token.type == 'LBRACE': # Handle dictionary literals
            return self.parse_dictionary_literal()
        else:
            raise Exception(f"Expected integer, string, boolean, identifier, or literal, got {token.type}")

    def unary_expression(self):
        token = self.get_current_token()
        if token.type == 'NOT':
            self.consume('NOT')
            right_node = self.unary_expression() # NOT applies to the next unary_expression
            return UnaryOp(token, right_node)
        return self.factor()

    def term(self):
        node = self.unary_expression()
        while self.get_current_token().type in ('MUL', 'DIV'):
            token = self.get_current_token()
            self.consume(token.type)
            node = BinOp(left=node, op=token, right=self.unary_expression())
        return node

    def comparison_expression(self):
        node = self.term()

        # Handle addition/subtraction
        while self.get_current_token().type in ('PLUS', 'MINUS'):
            token = self.get_current_token()
            self.consume(token.type)
            node = BinOp(left=node, op=token, right=self.term())

        # Handle comparisons
        if self.get_current_token().type in ('EQ', 'NEQ', 'GT', 'GTE', 'LT', 'LTE'):
            op_token = self.get_current_token()
            self.consume(op_token.type)
            right_node = self.comparison_expression() # Recursively parse right side of comparison
            node = Comparison(left=node, op=op_token, right=right_node)

        return node

    def expression(self):
        node = self.comparison_expression()
        while self.get_current_token().type in ('AND', 'OR'):
            op_token = self.get_current_token()
            self.consume(op_token.type)
            right_node = self.comparison_expression()
            node = LogicalOp(left=node, op=op_token, right=right_node)
        return node

    def parse_function_call(self, name_token):
        self.consume('LPAREN')
        arguments = []
        if self.get_current_token().type != 'RPAREN':
            while True:
                arguments.append(self.expression())
                if self.get_current_token().type == 'COMMA':
                    self.consume('COMMA')
                else:
                    break
        self.consume('RPAREN')
        return FunctionCall(name_token.value, arguments)

    def parse_list_literal(self):
        self.consume('LBRACKET')
        elements = []
        # Check if the list is empty
        if self.get_current_token().type == 'RBRACKET':
            self.consume('RBRACKET')
            return List(elements)

        # Parse first element
        elements.append(self.expression())

        # Parse subsequent elements
        while self.get_current_token().type == 'COMMA':
            self.consume('COMMA')
            elements.append(self.expression())

        # Expect closing bracket
        self.consume('RBRACKET')

        return List(elements)

    def parse_dictionary_literal(self):
        self.consume('LBRACE')
        pairs = []
        # Check if the dictionary is empty
        if self.get_current_token().type == 'RBRACE':
            self.consume('RBRACE')
            return Dictionary(pairs)

        # Parse first key-value pair
        key = self.expression()
        self.consume('COLON')
        value = self.expression()
        pairs.append((key, value))

        # Parse subsequent key-value pairs
        while self.get_current_token().type == 'COMMA':
            self.consume('COMMA')
            key = self.expression()
            self.consume('COLON')
            value = self.expression()
            pairs.append((key, value))

        # Expect closing brace
        self.consume('RBRACE')
        return Dictionary(pairs)

    def parse_index_access(self, target_node):
        self.consume('LBRACKET')
        index_node = self.expression()
        self.consume('RBRACKET')
        return IndexAccess(target_node, index_node)

    def parse_property_access(self, target_node):
        self.consume('DOT') # Assuming DOT token for property access
        property_name_token = self.get_current_token()
        self.consume('ID')
        return PropertyAccess(target_node, property_name_token.value)

    def parse_try_except_statement(self):
        self.consume('TRY')
        self.consume('FEMBOYCORE')
        try_block_statements = []
        while self.get_current_token().type != 'PERIODT':
            if self.get_current_token().type == 'EOF':
                raise Exception("Unterminated try block: Expected 'Periodt'")
            try_block_statements.append(self.parse_statement())
        self.consume('PERIODT')
        try_block = Block(try_block_statements)

        self.consume('EXCEPT')
        self.consume('FEMBOYCORE')
        except_block_statements = []
        while self.get_current_token().type != 'PERIODT':
            if self.get_current_token().type == 'EOF':
                raise Exception("Unterminated except block: Expected 'Periodt'")
            except_block_statements.append(self.parse_statement())
        self.consume('PERIODT')
        except_block = Block(except_block_statements)

        return TryExceptStatement(try_block, except_block)