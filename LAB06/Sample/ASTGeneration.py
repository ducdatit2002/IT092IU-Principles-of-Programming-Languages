from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List
from CompiledFiles.Ex2Visitor import Ex2Visitor
from CompiledFiles.Ex2Parser import Ex2Parser
from CompiledFiles.Ex3Visitor import Ex3Visitor
from CompiledFiles.Ex3Parser import Ex3Parser
from ASTUtils import *

# AST Utilities
def printlist(lst, f=str, start="[", sepa=",", end="]"):
    return start + sepa.join(f(i) for i in lst) + end

class AST(ABC):
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    @abstractmethod
    def accept(self, v, param):
        return v.visit(self, param)

class Exp(AST):
    __metaclass__ = ABCMeta
    pass

@dataclass
class Int(Exp):
    value: str

    def __str__(self):
        return "INT(" + self.value + ")"

    def accept(self, v, param):
        return v.visitInteger(self, param)

@dataclass
class Id(Exp):
    value: str

    def __str__(self):
        return "ID(" + self.value + ")"

    def accept(self, v, param):
        return v.visitIdentifier(self, param)

@dataclass
class Prog(AST):
    expr: List[Exp]

    def __str__(self):
        return "Prog(" + printlist(self.expr, start="", end="") + ")"

    def accept(self, v, param):
        return v.visitProgram(self, param)

@dataclass
class BinOp(Exp):
    left: Exp
    op: str
    right: Exp

    def __str__(self):
        return "BinOp(" + str(self.left) + ", " + self.op + ", " + str(self.right) + ")"

    def accept(self, v, param):
        return v.visitBinOp(self, param)

# AST Generation Classes for Ex1, Ex2, Ex3

class ASTGenerationEx1:
    def visitProgram(self, ctx):
        expressions = [expression.accept(self) for expression in ctx.expression()]
        return Prog(expressions)

    def visitExpression(self, ctx):
        if ctx.Integer():
            return self.visitInteger(ctx.Integer())
        if ctx.Identifier():
            return self.visitIdentifier(ctx.Identifier())
        
    def visitInteger(self, node):
        return Int(node.getText())

    def visitIdentifier(self, node):
        return Id(node.getText())

class ASTGenerationEx2(Ex2Visitor):
    def visitProgram(self, ctx: Ex2Parser.ProgramContext):
        # Visit all expressions in the program
        expressions = [expression.accept(self) for expression in ctx.expression()]
        return Prog(expressions)

    def visitExpression(self, ctx: Ex2Parser.ExpressionContext):
        # If there is only a term, return it
        if ctx.term() and not ctx.expression():
            return self.visitTerm(ctx.term())
        # If there is an expression and a term, it means it's a binary operation
        elif ctx.expression() and ctx.term():
            left = ctx.expression().accept(self)
            right = self.visitTerm(ctx.term())
            return BinOp(left, '+', right)

    def visitTerm(self, ctx: Ex2Parser.TermContext):
        if ctx.Integer():
            return self.visitInteger(ctx.Integer())
        elif ctx.Identifier():
            return self.visitIdentifier(ctx.Identifier())

    def visitInteger(self, token):
        return Int(token.getText())

    def visitIdentifier(self, token):
        return Id(token.getText())
   
    


class ASTGenerationEx3(Ex3Visitor):
    def visitProgram(self, ctx: Ex3Parser.ProgramContext):
        expressions = [expression.accept(self) for expression in ctx.expression()]
        return Prog(expressions)

    def visitBinaryExpr(self, ctx: Ex3Parser.BinaryExprContext):
        left = ctx.expression(0).accept(self)  # Use list indexing to get the first expression
        right = ctx.expression(1).accept(self)  # Use list indexing to get the second expression
        op = ctx.op.text
        return BinOp(left, op, right)

    def visitFactorExpr(self, ctx: Ex3Parser.FactorExprContext):
        return self.visit(ctx.factor())

    def visitBinaryFactor(self, ctx: Ex3Parser.BinaryFactorContext):
        left = ctx.factor(0).accept(self)  # Use list indexing if there are multiple factors
        op = ctx.op.text
        right = ctx.factor(1).accept(self)
        return BinOp(left, op, right)

    def visitTermFactor(self, ctx: Ex3Parser.TermFactorContext):
        return self.visit(ctx.term())

    def visitTerm(self, ctx: Ex3Parser.TermContext):
        if ctx.Integer():
            return Int(ctx.getText())
        else:
            return Id(ctx.getText())

    def visit(self, ctx):
        return ctx.accept(self)
