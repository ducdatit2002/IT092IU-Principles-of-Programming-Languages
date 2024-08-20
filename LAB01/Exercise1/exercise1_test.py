import sys
from antlr4 import *
from Exercise1Lexer import Exercise1Lexer
from Exercise1Parser import Exercise1Parser

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = Exercise1Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Exercise1Parser(stream)
    tree = parser.language()
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main(sys.argv)
