import sys
from antlr4 import *
from Ex5Lexer import Ex5Lexer
from Ex5Parser import Ex5Parser
from antlr4.tree.Trees import Trees

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = Ex5Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Ex5Parser(stream)
    tree = parser.start()
    print(Trees.toStringTree(tree, None, parser))

if __name__ == '__main__':
    main(sys.argv)
