import sys, os
import subprocess
import unittest
from antlr4 import *

# Define your variables
DIR = os.path.dirname(__file__)
ANTLR_JAR = 'C:/antlr/antlr4-4.9.2-complete.jar'
CPL_Dest = 'CompiledFiles'
SRC = 'Example.g4'
DIST = os.path.join(DIR, './dist')
TESTS = os.path.join(DIR, './tests')

# Run the command
#subprocess.run(['java', '-jar', ANTLR_JAR, '-o', DIST, '-Dlanguage=Python3', SRC])


def printUsage():
    print('python3 Hello.py gen')
    print('python3 Hello.py clean')
    print('python3 Hello.py test')

def printBreak():
    print('-----------------------------------------------')


def generateAntlr2Python():
    print('Antlr4 is running...')
    subprocess.run(['java', '-jar', ANTLR_JAR, '-o', CPL_Dest, '-no-listener', '-Dlanguage=Python3', SRC])
    print('Generate successfully')


def removeDist():
    print('Cleaning dist...')
    subprocess.run(['rm', '-rf', DIST, '/*'])
    print('Clean successfully')


def runTest():
    print('Running testcases...')
    
    # Import HelloLexer
    if not DIST in sys.path:
        sys.path.append(DIST)

    from CompiledFiles.ExampleLexer import ExampleLexer

    # Read all test files
    #testfiles = sorted(os.listdir(TESTS))

    #for filename in testfiles:
    filename ='004.txt'
    print('Running test : ' + filename)
    filepath = os.path.join(DIR, './tests', filename)      
    lexer = ExampleLexer(FileStream(filepath))        
    tokens = []
    token = lexer.nextToken()
    while token.type != Token.EOF:
        tokens.append(token.text)
        token = lexer.nextToken()
    tokens.append('<EOF>')
    print(','.join(tokens))

    printBreak()
    print('Run tests completely')


def main(argv):
    print('Complete jar file ANTLR  :  ' + str(ANTLR_JAR))
    print('Length of arguments      :  ' + str(len(argv)))
    print(DIR, SRC, DIST, TESTS)
    printBreak()

    if len(argv) < 1:
        printUsage()
    elif argv[0] == 'gen':
        generateAntlr2Python()
    elif argv[0] == 'clean':
        removeDist()
    elif argv[0] == 'test':
        if not os.path.isdir(DIST):
            generateAntlr2Python()
        runTest()
    else:
        printUsage()



if __name__ == '__main__':
    main(sys.argv[1:])     
    