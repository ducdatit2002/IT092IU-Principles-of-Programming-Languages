# Generated from Ex3.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\t")
        buf.write("*\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\6\2\f\n\2\r\2\16")
        buf.write("\2\r\3\3\3\3\3\3\3\3\3\3\3\3\7\3\26\n\3\f\3\16\3\31\13")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\7\4!\n\4\f\4\16\4$\13\4\3\5")
        buf.write("\3\5\5\5(\n\5\3\5\2\4\4\6\6\2\4\6\b\2\4\3\2\3\4\3\2\5")
        buf.write("\6\2)\2\13\3\2\2\2\4\17\3\2\2\2\6\32\3\2\2\2\b\'\3\2\2")
        buf.write("\2\n\f\5\4\3\2\13\n\3\2\2\2\f\r\3\2\2\2\r\13\3\2\2\2\r")
        buf.write("\16\3\2\2\2\16\3\3\2\2\2\17\20\b\3\1\2\20\21\5\6\4\2\21")
        buf.write("\27\3\2\2\2\22\23\f\4\2\2\23\24\t\2\2\2\24\26\5\6\4\2")
        buf.write("\25\22\3\2\2\2\26\31\3\2\2\2\27\25\3\2\2\2\27\30\3\2\2")
        buf.write("\2\30\5\3\2\2\2\31\27\3\2\2\2\32\33\b\4\1\2\33\34\5\b")
        buf.write("\5\2\34\"\3\2\2\2\35\36\f\4\2\2\36\37\t\3\2\2\37!\5\b")
        buf.write("\5\2 \35\3\2\2\2!$\3\2\2\2\" \3\2\2\2\"#\3\2\2\2#\7\3")
        buf.write("\2\2\2$\"\3\2\2\2%(\7\7\2\2&(\7\b\2\2\'%\3\2\2\2\'&\3")
        buf.write("\2\2\2(\t\3\2\2\2\6\r\27\"\'")
        return buf.getvalue()


class Ex3Parser ( Parser ):

    grammarFileName = "Ex3.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "Integer", "Identifier", "WS" ]

    RULE_program = 0
    RULE_expression = 1
    RULE_factor = 2
    RULE_term = 3

    ruleNames =  [ "program", "expression", "factor", "term" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    Integer=5
    Identifier=6
    WS=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Ex3Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(Ex3Parser.ExpressionContext,i)


        def getRuleIndex(self):
            return Ex3Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = Ex3Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.expression(0)
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==Ex3Parser.Integer or _la==Ex3Parser.Identifier):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Ex3Parser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class BinaryExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Ex3Parser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(Ex3Parser.ExpressionContext,0)

        def factor(self):
            return self.getTypedRuleContext(Ex3Parser.FactorContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinaryExpr" ):
                return visitor.visitBinaryExpr(self)
            else:
                return visitor.visitChildren(self)


    class FactorExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Ex3Parser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self):
            return self.getTypedRuleContext(Ex3Parser.FactorContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactorExpr" ):
                return visitor.visitFactorExpr(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Ex3Parser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = Ex3Parser.FactorExprContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 14
            self.factor(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 21
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = Ex3Parser.BinaryExprContext(self, Ex3Parser.ExpressionContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 16
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 17
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==Ex3Parser.T__0 or _la==Ex3Parser.T__1):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 18
                    self.factor(0) 
                self.state = 23
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Ex3Parser.RULE_factor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class TermFactorContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Ex3Parser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(Ex3Parser.TermContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermFactor" ):
                return visitor.visitTermFactor(self)
            else:
                return visitor.visitChildren(self)


    class BinaryFactorContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Ex3Parser.FactorContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def factor(self):
            return self.getTypedRuleContext(Ex3Parser.FactorContext,0)

        def term(self):
            return self.getTypedRuleContext(Ex3Parser.TermContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinaryFactor" ):
                return visitor.visitBinaryFactor(self)
            else:
                return visitor.visitChildren(self)



    def factor(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Ex3Parser.FactorContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_factor, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = Ex3Parser.TermFactorContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 25
            self.term()
            self._ctx.stop = self._input.LT(-1)
            self.state = 32
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = Ex3Parser.BinaryFactorContext(self, Ex3Parser.FactorContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_factor)
                    self.state = 27
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 28
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==Ex3Parser.T__2 or _la==Ex3Parser.T__3):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 29
                    self.term() 
                self.state = 34
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Ex3Parser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IntegerTermContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Ex3Parser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Integer(self):
            return self.getToken(Ex3Parser.Integer, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntegerTerm" ):
                return visitor.visitIntegerTerm(self)
            else:
                return visitor.visitChildren(self)


    class IdentifierTermContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Ex3Parser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(Ex3Parser.Identifier, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifierTerm" ):
                return visitor.visitIdentifierTerm(self)
            else:
                return visitor.visitChildren(self)



    def term(self):

        localctx = Ex3Parser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_term)
        try:
            self.state = 37
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Ex3Parser.Integer]:
                localctx = Ex3Parser.IntegerTermContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.match(Ex3Parser.Integer)
                pass
            elif token in [Ex3Parser.Identifier]:
                localctx = Ex3Parser.IdentifierTermContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.match(Ex3Parser.Identifier)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expression_sempred
        self._predicates[2] = self.factor_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def factor_sempred(self, localctx:FactorContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




