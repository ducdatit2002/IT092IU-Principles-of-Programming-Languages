# ASTUtils.py
from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple

def printlist(lst,f=str,start="[",sepa=",",end="]"):
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
    value: int

    def __str__(self):
        return f"INT({self.value})"

    def accept(self, v, param=None):
        return v.visitInteger(self, param)

@dataclass
class Str(Exp):
    name: str

    def __str__(self):
        return f"IDF({self.name})"

    def accept(self, v, param=None):
        return v.visitIdentifier(self, param)

@dataclass
class BinOp(Exp):
    left: Exp
    op: str
    right: Exp

    def __str__(self):
        return f"BinOp({str(self.left)}, {self.op}, {str(self.right)})"

    def accept(self, v, param=None):
        return v.visitBinOp(self, param)

@dataclass
class Prog(AST):
    expr: List[Exp]

    def __str__(self):
        return "Prog(" + printlist(self.expr, start="", end="") + ")"

    def accept(self, v, param=None):
        return v.visitProgram(self, param)