import sys, os
import subprocess
import unittest
from antlr4 import *

# Define your variables
DIR = os.path.dirname(__file__)
ANTLR_JAR = 'C:/antlr/antlr4-4.9.2-complete.jar' # your location is going here
CPL_Dest = 'CompiledFiles'
SRC = 'Sample.g4'
TESTS = os.path.join(DIR, './tests')


def printUsage():
    print('python3 run.py gen')
    print('python3 run.py test')

def printBreak():
    print('-----------------------------------------------')


def generateAntlr2Python():
    print('Antlr4 is running...')
    subprocess.run(['java', '-jar', ANTLR_JAR, '-o', CPL_Dest, '-no-listener', '-Dlanguage=Python3', SRC])
    print('Generate successfully')


def checkParser(lexerAgent, parserAgent, inputFile, outputFile):
    dest = open(outputFile,"w")
    lexer = lexerAgent(FileStream(inputFile))

    tokens = CommonTokenStream(lexer)
    parser = parserAgent(tokens)

    dest = open(outputFile,"r")
    line = dest.read()
    print(line)

def runTest():
    print('Running testcases...')
    from CompiledFiles.SampleLexer import SampleLexer
    from CompiledFiles.SampleParser import SampleParser

    filename = '001.txt'
    inputFile = os.path.join(DIR, './tests', filename)    

 
    input_stream = FileStream(inputFile)
    lexer = SampleLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SampleParser(stream)
    tree = parser.start()

    # Print the parse tree
    print(tree.toStringTree(recog=parser))

    printBreak()
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

# run cmd: python run.py test



if __name__ == '__main__':
    main(sys.argv[1:])     
    
    