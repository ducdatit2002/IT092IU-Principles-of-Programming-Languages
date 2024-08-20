from CompiledFiles.SampleVisitor import SampleVisitor
from CompiledFiles.SampleParser import SampleParser
from ASTUtils import *

class ASTGeneration(SampleVisitor):
    def visitProgram(self, ctx: SampleParser.ProgramContext):
        expressions = [expression.accept(self) for expression in ctx.expression()]
        return Prog(expressions)

    def visitExpression(self, ctx: SampleParser.ExpressionContext):
        if ctx.getChildCount() == 3:  # Handles the case "expression (Add | Sub) factor"
            left = ctx.getChild(0).accept(self)
            operator = ctx.getChild(1).getText()
            right = ctx.getChild(2).accept(self)
            return BinOp(left, operator, right)
        else:  # Handles the case "factor"
            return ctx.getChild(0).accept(self)

    def visitFactor(self, ctx: SampleParser.FactorContext):
        if ctx.getChildCount() == 3:  # Handles the case "factor (Mul | Div) term"
            left = ctx.getChild(0).accept(self)
            operator = ctx.getChild(1).getText()
            right = ctx.getChild(2).accept(self)
            return BinOp(left, operator, right)
        else:  # Handles the case "term"
            return ctx.getChild(0).accept(self)

    def visitTerm(self, ctx: SampleParser.TermContext):
        if ctx.Integer():
            return self.visitInteger(ctx.Integer())
        elif ctx.Identifier():
            return self.visitIdentifier(ctx.Identifier())

    def visitInteger(self, ctx):  # No need for SampleParser.IntegerContext
        return Int(int(ctx.getText()))

    def visitIdentifier(self, ctx):  # No need for SampleParser.IdentifierContext
        return Str(ctx.getText())