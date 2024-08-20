# Generated from Ex3.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .Ex3Parser import Ex3Parser
else:
    from Ex3Parser import Ex3Parser

# This class defines a complete generic visitor for a parse tree produced by Ex3Parser.

class Ex3Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by Ex3Parser#program.
    def visitProgram(self, ctx:Ex3Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ex3Parser#BinaryExpr.
    def visitBinaryExpr(self, ctx:Ex3Parser.BinaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ex3Parser#FactorExpr.
    def visitFactorExpr(self, ctx:Ex3Parser.FactorExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ex3Parser#TermFactor.
    def visitTermFactor(self, ctx:Ex3Parser.TermFactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ex3Parser#BinaryFactor.
    def visitBinaryFactor(self, ctx:Ex3Parser.BinaryFactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ex3Parser#IntegerTerm.
    def visitIntegerTerm(self, ctx:Ex3Parser.IntegerTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ex3Parser#IdentifierTerm.
    def visitIdentifierTerm(self, ctx:Ex3Parser.IdentifierTermContext):
        return self.visitChildren(ctx)



del Ex3Parser