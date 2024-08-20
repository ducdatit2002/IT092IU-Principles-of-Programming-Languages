import sys, os
import subprocess
import unittest
from antlr4 import *

# Define your variables
DIR = os.path.dirname(__file__)
ANTLR_JAR = '/Users/macbook/Documents/Library_PPL/antlr4-4.9.2-complete.jar'
CPL_Dest = 'CompiledFiles'
SRC = 'Sample.g4'
TESTS = os.path.join(DIR, './tests')

def printUsage():
    print('python run.py gen')
    print('python run.py test')

def printBreak():
    print('-----------------------------------------------')

def generateAntlr2Python():
    print('Antlr4 is running...')
    subprocess.run(['java', '-jar', ANTLR_JAR, '-o', CPL_Dest, '-no-listener', '-visitor', '-Dlanguage=Python3', SRC])    
    print('Generate successfully')

def runTest():
    print('Running testcases...')
    # Include Lexer and Parser from Compiled files
    from CompiledFiles.SampleLexer import SampleLexer
    from CompiledFiles.SampleParser import SampleParser
    
    inputFile = 'testcase.txt'
    outputFile = "result.txt"   
    dest = open(outputFile,"w")

    # Read input from a file or a string
    input_stream = FileStream(inputFile)    
    lexer = SampleLexer(input_stream)
  
    stream = CommonTokenStream(lexer)
    parser = SampleParser(stream)
      
    tree = parser.program()
    print(tree.toStringTree(recog=parser))
    #(program (expression 17) (expression 23) (expression 4) (expression 86))
   
    from ASTGeneration import ASTGeneration
    ast_generator = ASTGeneration()

    asttree = tree.accept(ast_generator)
    
    dest.write(str(asttree))
    print('This is ast string: ', asttree)
    dest = open(outputFile,"r")
    line = dest.read()
    print(line)
  
    print('Run tests completely')

def main(argv):
    print('Complete jar file ANTLR  :  ' + str(ANTLR_JAR))
    print('Length of arguments      :  ' + str(len(argv)))
    print(DIR, SRC, TESTS)
    printBreak()

    if len(argv) < 1:
        printUsage()
    elif argv[0] == 'gen':
        generateAntlr2Python()   
    elif argv[0] == 'test':        
        runTest()        
    else:
        printUsage()


if __name__ == '__main__':
    main(sys.argv[1:])     
    
    