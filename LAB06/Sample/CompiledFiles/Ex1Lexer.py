# Generated from Ex1.g4 by ANTLR 4.9.2
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
        buf.write("\32\b\1\4\2\t\2\4\3\t\3\4\4\t\4\3\2\6\2\13\n\2\r\2\16")
        buf.write("\2\f\3\3\6\3\20\n\3\r\3\16\3\21\3\4\6\4\25\n\4\r\4\16")
        buf.write("\4\26\3\4\3\4\2\2\5\3\3\5\4\7\5\3\2\5\3\2\62;\3\2c|\5")
        buf.write("\2\13\f\17\17\"\"\2\34\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write("\2\2\3\n\3\2\2\2\5\17\3\2\2\2\7\24\3\2\2\2\t\13\t\2\2")
        buf.write("\2\n\t\3\2\2\2\13\f\3\2\2\2\f\n\3\2\2\2\f\r\3\2\2\2\r")
        buf.write("\4\3\2\2\2\16\20\t\3\2\2\17\16\3\2\2\2\20\21\3\2\2\2\21")
        buf.write("\17\3\2\2\2\21\22\3\2\2\2\22\6\3\2\2\2\23\25\t\4\2\2\24")
        buf.write("\23\3\2\2\2\25\26\3\2\2\2\26\24\3\2\2\2\26\27\3\2\2\2")
        buf.write("\27\30\3\2\2\2\30\31\b\4\2\2\31\b\3\2\2\2\6\2\f\21\26")
        buf.write("\3\b\2\2")
        return buf.getvalue()


class Ex1Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    Integer = 1
    Identifier = 2
    WS = 3

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "Integer", "Identifier", "WS" ]

    ruleNames = [ "Integer", "Identifier", "WS" ]

    grammarFileName = "Ex1.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


