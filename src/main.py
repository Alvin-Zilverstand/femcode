from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

def main():
    with open('../examples/variables.fem', 'r') as f:
        text = f.read()

    lexer = Lexer(text)
    tokens = lexer.tokenize()

    parser = Parser(tokens)
    ast = parser.parse()

    interpreter = Interpreter(ast)
    interpreter.interpret()

if __name__ == '__main__':
    main()
