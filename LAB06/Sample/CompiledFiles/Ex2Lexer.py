# Generated from Ex2.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\6")
        buf.write("\36\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\3\6")
        buf.write("\3\17\n\3\r\3\16\3\20\3\4\6\4\24\n\4\r\4\16\4\25\3\5\6")
        buf.write("\5\31\n\5\r\5\16\5\32\3\5\3\5\2\2\6\3\3\5\4\7\5\t\6\3")
        buf.write("\2\5\3\2\62;\3\2c|\5\2\13\f\17\17\"\"\2 \2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\3\13\3\2\2\2\5\16\3")
        buf.write("\2\2\2\7\23\3\2\2\2\t\30\3\2\2\2\13\f\7-\2\2\f\4\3\2\2")
        buf.write("\2\r\17\t\2\2\2\16\r\3\2\2\2\17\20\3\2\2\2\20\16\3\2\2")
        buf.write("\2\20\21\3\2\2\2\21\6\3\2\2\2\22\24\t\3\2\2\23\22\3\2")
        buf.write("\2\2\24\25\3\2\2\2\25\23\3\2\2\2\25\26\3\2\2\2\26\b\3")
        buf.write("\2\2\2\27\31\t\4\2\2\30\27\3\2\2\2\31\32\3\2\2\2\32\30")
        buf.write("\3\2\2\2\32\33\3\2\2\2\33\34\3\2\2\2\34\35\b\5\2\2\35")
        buf.write("\n\3\2\2\2\6\2\20\25\32\3\b\2\2")
        return buf.getvalue()


class Ex2Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    Integer = 2
    Identifier = 3
    WS = 4

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'" ]

    symbolicNames = [ "<INVALID>",
            "Integer", "Identifier", "WS" ]

    ruleNames = [ "T__0", "Integer", "Identifier", "WS" ]

    grammarFileName = "Ex2.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


