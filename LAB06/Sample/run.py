import sys, os
import subprocess
from antlr4 import *

# Define your variables
DIR = os.path.dirname(__file__)
ANTLR_JAR = 'antlr4-4.9.2-complete.jar'  # Update this with the correct path
CPL_Dest = 'CompiledFiles'
TESTS = os.path.join(DIR, './tests')

GRAMMARS = {
    "ex1": "Ex1.g4",
    "ex2": "Ex2.g4",
    "ex3": "Ex3.g4",
}

def printUsage():
    print('python run.py gen [exercise]')
    print('python run.py test [exercise]')

def printBreak():
    print('-----------------------------------------------')

def generateAntlr2Python(grammar):
    print(f'Antlr4 is running for {grammar}...')
    subprocess.run(['java', '-jar', ANTLR_JAR, '-o', CPL_Dest, '-no-listener', '-visitor', '-Dlanguage=Python3', GRAMMARS[grammar]])
    print('Generate successfully')

def runTest(grammar):
    print(f'Running testcases for {grammar}...')
    
    if grammar == 'ex1':
        from CompiledFiles.Ex1Lexer import Ex1Lexer as LexerClass
        from CompiledFiles.Ex1Parser import Ex1Parser as ParserClass
    elif grammar == 'ex2':
        from CompiledFiles.Ex2Lexer import Ex2Lexer as LexerClass
        from CompiledFiles.Ex2Parser import Ex2Parser as ParserClass
    elif grammar == 'ex3':
        from CompiledFiles.Ex3Lexer import Ex3Lexer as LexerClass
        from CompiledFiles.Ex3Parser import Ex3Parser as ParserClass
    
    inputFile = os.path.join(TESTS, f'{grammar}_test.txt')
    outputFile = os.path.join(TESTS, f'{grammar}_result.txt')
    dest = open(outputFile, "w")

    # Read input from a file or a string
    input_stream = FileStream(inputFile)
    lexer = LexerClass(input_stream)

    stream = CommonTokenStream(lexer)
    parser = ParserClass(stream)

    tree = parser.program()
    print(tree.toStringTree(recog=parser))

    if grammar == 'ex1':
        from ASTGeneration import ASTGenerationEx1 as ASTGenClass
    elif grammar == 'ex2':
        from ASTGeneration import ASTGenerationEx2 as ASTGenClass
    elif grammar == 'ex3':
        from ASTGeneration import ASTGenerationEx3 as ASTGenClass
        
    ast_generator = ASTGenClass()

    asttree = tree.accept(ast_generator)
    
    dest.write(str(asttree))
    print('This is ast string: ', asttree)
    dest = open(outputFile, "r")
    line = dest.read()
    print(line)
  
    print('Run tests completely')

def main(argv):
    print('Complete jar file ANTLR  :  ' + str(ANTLR_JAR))
    print('Length of arguments      :  ' + str(len(argv)))
    print(DIR, GRAMMARS, TESTS)
    printBreak()

    if len(argv) < 2:
        printUsage()
    elif argv[0] == 'gen':
        generateAntlr2Python(argv[1])   
    elif argv[0] == 'test':        
        runTest(argv[1])
    else:
        printUsage()

if __name__ == '__main__':
    main(sys.argv[1:])
