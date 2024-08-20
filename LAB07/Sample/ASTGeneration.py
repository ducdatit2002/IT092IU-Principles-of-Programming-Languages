from CompiledFiles.SampleVisitor import SampleVisitor
from CompiledFiles.SampleParser import SampleParser
from ASTUtils import *

class ASTGeneration(SampleVisitor):
    def visitProgram(self, ctx: SampleParser.ProgramContext):
        return Prog([ctx.expression().accept(self)])

    def visitExpression(self, ctx: SampleParser.ExpressionContext):
        if ctx.expression():
            sign = ""
            if ctx.Add():
                sign = "+"
            elif ctx.Sub():
                sign = "-"
                            
            return BinOp(sign, ctx.expression().accept(self), ctx.term().accept(self))
        else:
            return ctx.term().accept(self)

    def visitTerm(self, ctx: SampleParser.TermContext):
        if ctx.term():
            sign = ""
            if ctx.Mul():
                sign = "*"
            elif ctx.Div():
                sign = "/"
            elif ctx.Mod():
                sign = "%"
            
            return BinOp(sign, ctx.term().accept(self), ctx.factor().accept(self))
        else:
            return ctx.factor().accept(self)

    def visitFactor(self, ctx: SampleParser.FactorContext):
        if ctx.factor():
            sign = "^"
            return BinOp(sign, ctx.factor().accept(self), ctx.atom().accept(self))
        else:
            return ctx.atom().accept(self)

    def visitAtom(self, ctx: SampleParser.AtomContext):
        if ctx.Integer():
            return self.visitInteger(ctx.Integer())

    def visitInteger(self, node: SampleParser.IntegerContext):
        return Int(int(node.getText()))
