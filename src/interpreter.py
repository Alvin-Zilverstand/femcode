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

    def visit_BinOp(self, node):
        if node.op.type == 'PLUS':
            return self.visit(node.left) + self.visit(node.right)
        elif node.op.type == 'MINUS':
            return self.visit(node.left) - self.visit(node.right)
        elif node.op.type == 'MUL':
            return self.visit(node.left) * self.visit(node.right)
        elif node.op.type == 'DIV':
            return self.visit(node.left) / self.visit(node.right)

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
