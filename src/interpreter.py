class Interpreter:
    def __init__(self, ast):
        self.ast = ast
        self.variables = {}

    def interpret(self):
        for node in self.ast:
            self.visit(node)

    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name, self.no_visit_method)
        return method(node)

    def no_visit_method(self, node):
        raise Exception(f'No visit_{type(node).__name__} method defined')

    def visit_Number(self, node):
        return node.value

    def visit_String(self, node):
        return node.value

    def visit_BinOp(self, node):
        left_val = self.visit(node.left)
        right_val = self.visit(node.right)
        if node.op.type == 'PLUS':
            return left_val + right_val
        elif node.op.type == 'MINUS':
            return left_val - right_val
        elif node.op.type == 'MUL':
            return left_val * right_val
        elif node.op.type == 'DIV':
            return left_val / right_val

    def visit_Comparison(self, node):
        left_val = self.visit(node.left)
        right_val = self.visit(node.right)
        if node.op.type == 'EQ':
            return left_val == right_val
        elif node.op.type == 'NEQ':
            return left_val != right_val
        elif node.op.type == 'GT':
            return left_val > right_val
        elif node.op.type == 'GTE':
            return left_val >= right_val
        elif node.op.type == 'LT':
            return left_val < right_val
        elif node.op.type == 'LTE':
            return left_val <= right_val

    def visit_Print(self, node):
        value_to_print = self.visit(node.value)
        print(value_to_print)

    def visit_Assign(self, node):
        var_name = node.left.value
        value = self.visit(node.right)
        self.variables[var_name] = value

    def visit_Variable(self, node):
        var_name = node.value
        if var_name in self.variables:
            return self.variables[var_name]
        else:
            raise NameError(f"name '{var_name}' is not defined")

    def visit_Block(self, node):
        for statement in node.statements:
            self.visit(statement)

    def visit_IfStatement(self, node):
        condition_result = self.visit(node.condition)
        if condition_result:
            self.visit(node.if_block)
        elif node.else_block:
            self.visit(node.else_block)
