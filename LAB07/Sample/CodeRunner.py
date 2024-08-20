from ASTUtils import *

class CodeRunner():
    def visitProgram(self, ctx: Prog):
        return "\n".join([str(expr.accept(self)) for expr in ctx.expr])

    def visitBinaryOp(self, ctx: BinOp):
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
        elif ctx.op == "^":
            return left ** right  # Exponentiation

    def visitInteger(self, node: Int):
        return node.value
