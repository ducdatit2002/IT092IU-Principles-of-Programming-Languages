# Generated from Exercise1.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\5")
        buf.write("\24\b\1\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\3\3\3\3\4\6")
        buf.write("\4\17\n\4\r\4\16\4\20\3\4\3\4\2\2\5\3\3\5\4\7\5\3\2\5")
        buf.write("\3\2c|\3\2\62;\5\2\13\f\17\17\"\"\2\24\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\3\t\3\2\2\2\5\13\3\2\2\2\7\16\3\2")
        buf.write("\2\2\t\n\t\2\2\2\n\4\3\2\2\2\13\f\t\3\2\2\f\6\3\2\2\2")
        buf.write("\r\17\t\4\2\2\16\r\3\2\2\2\17\20\3\2\2\2\20\16\3\2\2\2")
        buf.write("\20\21\3\2\2\2\21\22\3\2\2\2\22\23\b\4\2\2\23\b\3\2\2")
        buf.write("\2\4\2\20\3\b\2\2")
        return buf.getvalue()


class Exercise1Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    LOWERCASE = 1
    DIGIT = 2
    WS = 3

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "LOWERCASE", "DIGIT", "WS" ]

    ruleNames = [ "LOWERCASE", "DIGIT", "WS" ]

    grammarFileName = "Exercise1.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


