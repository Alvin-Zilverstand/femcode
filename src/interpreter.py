class Interpreter:
    def __init__(self, ast):
        self.ast = ast

    def interpret(self):
        for node in self.ast:
            self.visit(node)

    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name, self.no_visit_method)
        return method(node)

    def no_visit_method(self, node):
        raise Exception(f'No visit_{type(node).__name__} method defined')

    def visit_Print(self, node):
        print(node.value)
