# Generated from Ex2.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .Ex2Parser import Ex2Parser
else:
    from Ex2Parser import Ex2Parser

# This class defines a complete generic visitor for a parse tree produced by Ex2Parser.

class Ex2Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by Ex2Parser#program.
    def visitProgram(self, ctx:Ex2Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ex2Parser#expression.
    def visitExpression(self, ctx:Ex2Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ex2Parser#term.
    def visitTerm(self, ctx:Ex2Parser.TermContext):
        return self.visitChildren(ctx)



del Ex2Parser