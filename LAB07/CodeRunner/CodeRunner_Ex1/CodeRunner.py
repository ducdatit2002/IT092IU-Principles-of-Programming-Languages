from ASTUtils import *
from functools import reduce

class CodeRunner():
    def visitProgram(self, ctx:Prog):
        return "\n".join([str(expr.accept(self)) for expr in ctx.expr])

    def visitBinaryOp(self, ctx:BinOp):
        left = ctx.left.accept(self)
        right = ctx.right.accept(self)
        if ctx.op == "+":
            return left + right
        elif ctx.op == "-":
            return left - right
        elif ctx.op == "*":
            return left * right
        elif ctx.op == "/":
            return left / right
        elif ctx.op == "%":
            return left % right
        
        
            # if (left < right):
            #     return left
            # s1 = left / right
            # s2 = right * s1
            # if (s1 == s2):
            #     return s1
            # return left - s1
        

    def visitInteger(self, node:Int):
        return node.value