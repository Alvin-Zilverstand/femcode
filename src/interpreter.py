class Interpreter:
    def __init__(self, ast):
        self.ast = ast
        self.scope_stack = [{}]
        self.functions = {}

    @property
    def current_scope(self):
        return self.scope_stack[-1]

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
        self.current_scope[var_name] = value

    def visit_Variable(self, node):
        var_name = node.value
        # Search up the scope stack for the variable
        for scope in reversed(self.scope_stack):
            if var_name in scope:
                return scope[var_name]
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

    def visit_WhileStatement(self, node):
        while self.visit(node.condition):
            self.visit(node.body)

    def visit_FunctionDefinition(self, node):
        self.functions[node.name] = {
            'parameters': node.parameters,
            'body': node.body
        }

    def visit_FunctionCall(self, node):
        func_name = node.name
        if func_name not in self.functions:
            raise NameError(f"Function '{func_name}' is not defined")

        func_info = self.functions[func_name]

        # Evaluate arguments
        evaluated_arguments = [self.visit(arg) for arg in node.arguments]

        # Create a new scope for the function call
        new_scope = {}
        for i, param_name in enumerate(func_info['parameters']):
            new_scope[param_name] = evaluated_arguments[i]

        self.scope_stack.append(new_scope)

        # Execute function body
        try:
            self.visit(func_info['body'])
        except ReturnValue as e:
            self.scope_stack.pop() # Pop the function scope
            return e.value
        finally:
            # Ensure scope is popped even if no return or an error occurs
            if len(self.scope_stack) > 1: # Don't pop global scope
                self.scope_stack.pop()

    def visit_ReturnStatement(self, node):
        raise ReturnValue(self.visit(node.value))

class ReturnValue(Exception):
    def __init__(self, value):
        self.value = value
