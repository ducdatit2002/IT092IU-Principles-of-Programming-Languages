# Generated from Exercise1.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\5")
        buf.write("\f\4\2\t\2\3\2\3\2\7\2\7\n\2\f\2\16\2\n\13\2\3\2\2\2\3")
        buf.write("\2\2\3\3\2\3\4\2\13\2\4\3\2\2\2\4\b\7\3\2\2\5\7\t\2\2")
        buf.write("\2\6\5\3\2\2\2\7\n\3\2\2\2\b\6\3\2\2\2\b\t\3\2\2\2\t\3")
        buf.write("\3\2\2\2\n\b\3\2\2\2\3\b")
        return buf.getvalue()


class Exercise1Parser ( Parser ):

    grammarFileName = "Exercise1.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "LOWERCASE", "DIGIT", "WS" ]

    RULE_language = 0

    ruleNames =  [ "language" ]

    EOF = Token.EOF
    LOWERCASE=1
    DIGIT=2
    WS=3

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class LanguageContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOWERCASE(self, i:int=None):
            if i is None:
                return self.getTokens(Exercise1Parser.LOWERCASE)
            else:
                return self.getToken(Exercise1Parser.LOWERCASE, i)

        def DIGIT(self, i:int=None):
            if i is None:
                return self.getTokens(Exercise1Parser.DIGIT)
            else:
                return self.getToken(Exercise1Parser.DIGIT, i)

        def getRuleIndex(self):
            return Exercise1Parser.RULE_language

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLanguage" ):
                listener.enterLanguage(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLanguage" ):
                listener.exitLanguage(self)




    def language(self):

        localctx = Exercise1Parser.LanguageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_language)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(Exercise1Parser.LOWERCASE)
            self.state = 6
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Exercise1Parser.LOWERCASE or _la==Exercise1Parser.DIGIT:
                self.state = 3
                _la = self._input.LA(1)
                if not(_la==Exercise1Parser.LOWERCASE or _la==Exercise1Parser.DIGIT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 8
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





