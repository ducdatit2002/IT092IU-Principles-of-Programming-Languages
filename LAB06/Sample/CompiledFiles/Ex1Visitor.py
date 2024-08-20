# Generated from Ex1.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .Ex1Parser import Ex1Parser
else:
    from Ex1Parser import Ex1Parser

# This class defines a complete generic visitor for a parse tree produced by Ex1Parser.

class Ex1Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by Ex1Parser#program.
    def visitProgram(self, ctx:Ex1Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ex1Parser#expression.
    def visitExpression(self, ctx:Ex1Parser.ExpressionContext):
        return self.visitChildren(ctx)



del Ex1Parser