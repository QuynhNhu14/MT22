# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3?")
        buf.write("\u0168\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\3\2\3\2\3\2\3\3\6\3U\n\3\r\3\16\3V\3\4")
        buf.write("\3\4\5\4[\n\4\3\5\3\5\5\5_\n\5\3\5\3\5\3\6\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7s")
        buf.write("\n\7\3\b\3\b\3\b\6\bx\n\b\r\b\16\by\3\b\3\b\5\b~\n\b\3")
        buf.write("\t\3\t\3\t\7\t\u0083\n\t\f\t\16\t\u0086\13\t\3\n\3\n\3")
        buf.write("\n\3\n\5\n\u008c\n\n\3\13\3\13\3\f\3\f\3\f\3\f\3\f\7\f")
        buf.write("\u0095\n\f\f\f\16\f\u0098\13\f\3\f\3\f\3\f\3\f\3\r\5\r")
        buf.write("\u009f\n\r\3\r\5\r\u00a2\n\r\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17")
        buf.write("\u00b4\n\17\3\20\7\20\u00b7\n\20\f\20\16\20\u00ba\13\20")
        buf.write("\3\21\3\21\3\21\7\21\u00bf\n\21\f\21\16\21\u00c2\13\21")
        buf.write("\3\21\3\21\3\22\6\22\u00c7\n\22\r\22\16\22\u00c8\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u00d5")
        buf.write("\n\23\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\5\25\u00e1\n\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3")
        buf.write("\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\33\3\33\5\33\u00fc\n\33\3")
        buf.write("\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\7\35\u0106\n\35")
        buf.write("\f\35\16\35\u0109\13\35\3\36\3\36\3\36\3\36\3\36\5\36")
        buf.write("\u0110\n\36\3\37\3\37\3\37\3\37\3\37\5\37\u0117\n\37\3")
        buf.write(" \3 \3 \3 \3 \5 \u011e\n \3!\3!\3!\3!\3!\3!\7!\u0126\n")
        buf.write("!\f!\16!\u0129\13!\3\"\3\"\3\"\3\"\3\"\3\"\7\"\u0131\n")
        buf.write("\"\f\"\16\"\u0134\13\"\3#\3#\3#\3#\3#\3#\7#\u013c\n#\f")
        buf.write("#\16#\u013f\13#\3$\3$\3$\5$\u0144\n$\3%\3%\3%\5%\u0149")
        buf.write("\n%\3&\3&\3&\3&\3&\3&\3&\3&\7&\u0153\n&\f&\16&\u0156\13")
        buf.write("&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\5\'\u015f\n\'\3(\3(\3(\5")
        buf.write("(\u0164\n(\3(\3(\3(\2\6@BDJ)\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLN\2\7\6\2")
        buf.write("\7\7\13\13\21\21;;\3\2\"\'\3\2 !\3\2\32\33\3\2\34\36\2")
        buf.write("\u016b\2P\3\2\2\2\4T\3\2\2\2\6Z\3\2\2\2\b^\3\2\2\2\nb")
        buf.write("\3\2\2\2\fr\3\2\2\2\16}\3\2\2\2\20\177\3\2\2\2\22\u008b")
        buf.write("\3\2\2\2\24\u008d\3\2\2\2\26\u008f\3\2\2\2\30\u009e\3")
        buf.write("\2\2\2\32\u00a7\3\2\2\2\34\u00aa\3\2\2\2\36\u00b8\3\2")
        buf.write("\2\2 \u00bb\3\2\2\2\"\u00c6\3\2\2\2$\u00d4\3\2\2\2&\u00d6")
        buf.write("\3\2\2\2(\u00d9\3\2\2\2*\u00e2\3\2\2\2,\u00e7\3\2\2\2")
        buf.write(".\u00ec\3\2\2\2\60\u00f3\3\2\2\2\62\u00f6\3\2\2\2\64\u00f9")
        buf.write("\3\2\2\2\66\u00ff\3\2\2\28\u0102\3\2\2\2:\u010f\3\2\2")
        buf.write("\2<\u0116\3\2\2\2>\u011d\3\2\2\2@\u011f\3\2\2\2B\u012a")
        buf.write("\3\2\2\2D\u0135\3\2\2\2F\u0143\3\2\2\2H\u0148\3\2\2\2")
        buf.write("J\u014a\3\2\2\2L\u015e\3\2\2\2N\u0160\3\2\2\2PQ\5\4\3")
        buf.write("\2QR\7\2\2\3R\3\3\2\2\2SU\5\6\4\2TS\3\2\2\2UV\3\2\2\2")
        buf.write("VT\3\2\2\2VW\3\2\2\2W\5\3\2\2\2X[\5\b\5\2Y[\5\32\16\2")
        buf.write("ZX\3\2\2\2ZY\3\2\2\2[\7\3\2\2\2\\_\5\n\6\2]_\5\f\7\2^")
        buf.write("\\\3\2\2\2^]\3\2\2\2_`\3\2\2\2`a\7\61\2\2a\t\3\2\2\2b")
        buf.write("c\5\20\t\2cd\7\62\2\2de\5\22\n\2e\13\3\2\2\2fg\7\65\2")
        buf.write("\2gh\7\62\2\2hi\5\22\n\2ij\7\63\2\2jk\5\16\b\2ks\3\2\2")
        buf.write("\2lm\7\65\2\2mn\7\60\2\2no\5\f\7\2op\7\60\2\2pq\5\16\b")
        buf.write("\2qs\3\2\2\2rf\3\2\2\2rl\3\2\2\2s\r\3\2\2\2t~\5:\36\2")
        buf.write("uw\7-\2\2vx\5\16\b\2wv\3\2\2\2xy\3\2\2\2yw\3\2\2\2yz\3")
        buf.write("\2\2\2z{\3\2\2\2{|\7.\2\2|~\3\2\2\2}t\3\2\2\2}u\3\2\2")
        buf.write("\2~\17\3\2\2\2\177\u0084\7\65\2\2\u0080\u0081\7\60\2\2")
        buf.write("\u0081\u0083\7\65\2\2\u0082\u0080\3\2\2\2\u0083\u0086")
        buf.write("\3\2\2\2\u0084\u0082\3\2\2\2\u0084\u0085\3\2\2\2\u0085")
        buf.write("\21\3\2\2\2\u0086\u0084\3\2\2\2\u0087\u008c\5\24\13\2")
        buf.write("\u0088\u008c\7\r\2\2\u0089\u008c\7\5\2\2\u008a\u008c\5")
        buf.write("\26\f\2\u008b\u0087\3\2\2\2\u008b\u0088\3\2\2\2\u008b")
        buf.write("\u0089\3\2\2\2\u008b\u008a\3\2\2\2\u008c\23\3\2\2\2\u008d")
        buf.write("\u008e\t\2\2\2\u008e\25\3\2\2\2\u008f\u0090\7\31\2\2\u0090")
        buf.write("\u0091\7+\2\2\u0091\u0096\7\67\2\2\u0092\u0093\7\60\2")
        buf.write("\2\u0093\u0095\7\67\2\2\u0094\u0092\3\2\2\2\u0095\u0098")
        buf.write("\3\2\2\2\u0096\u0094\3\2\2\2\u0096\u0097\3\2\2\2\u0097")
        buf.write("\u0099\3\2\2\2\u0098\u0096\3\2\2\2\u0099\u009a\7,\2\2")
        buf.write("\u009a\u009b\7\t\2\2\u009b\u009c\5\24\13\2\u009c\27\3")
        buf.write("\2\2\2\u009d\u009f\7\16\2\2\u009e\u009d\3\2\2\2\u009e")
        buf.write("\u009f\3\2\2\2\u009f\u00a1\3\2\2\2\u00a0\u00a2\7\25\2")
        buf.write("\2\u00a1\u00a0\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a3")
        buf.write("\3\2\2\2\u00a3\u00a4\7\65\2\2\u00a4\u00a5\7\62\2\2\u00a5")
        buf.write("\u00a6\5\22\n\2\u00a6\31\3\2\2\2\u00a7\u00a8\5\34\17\2")
        buf.write("\u00a8\u00a9\5 \21\2\u00a9\33\3\2\2\2\u00aa\u00ab\7\65")
        buf.write("\2\2\u00ab\u00ac\7\62\2\2\u00ac\u00ad\7\22\2\2\u00ad\u00ae")
        buf.write("\5\22\n\2\u00ae\u00af\7)\2\2\u00af\u00b0\5\36\20\2\u00b0")
        buf.write("\u00b3\7*\2\2\u00b1\u00b2\7\16\2\2\u00b2\u00b4\7\65\2")
        buf.write("\2\u00b3\u00b1\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\35\3")
        buf.write("\2\2\2\u00b5\u00b7\5\30\r\2\u00b6\u00b5\3\2\2\2\u00b7")
        buf.write("\u00ba\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b8\u00b9\3\2\2\2")
        buf.write("\u00b9\37\3\2\2\2\u00ba\u00b8\3\2\2\2\u00bb\u00c0\7+\2")
        buf.write("\2\u00bc\u00bf\5\"\22\2\u00bd\u00bf\5\b\5\2\u00be\u00bc")
        buf.write("\3\2\2\2\u00be\u00bd\3\2\2\2\u00bf\u00c2\3\2\2\2\u00c0")
        buf.write("\u00be\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\u00c3\3\2\2\2")
        buf.write("\u00c2\u00c0\3\2\2\2\u00c3\u00c4\7,\2\2\u00c4!\3\2\2\2")
        buf.write("\u00c5\u00c7\5$\23\2\u00c6\u00c5\3\2\2\2\u00c7\u00c8\3")
        buf.write("\2\2\2\u00c8\u00c6\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9#")
        buf.write("\3\2\2\2\u00ca\u00d5\5&\24\2\u00cb\u00d5\5(\25\2\u00cc")
        buf.write("\u00d5\5*\26\2\u00cd\u00d5\5,\27\2\u00ce\u00d5\5.\30\2")
        buf.write("\u00cf\u00d5\5\60\31\2\u00d0\u00d5\5\62\32\2\u00d1\u00d5")
        buf.write("\5\64\33\2\u00d2\u00d5\5\66\34\2\u00d3\u00d5\5 \21\2\u00d4")
        buf.write("\u00ca\3\2\2\2\u00d4\u00cb\3\2\2\2\u00d4\u00cc\3\2\2\2")
        buf.write("\u00d4\u00cd\3\2\2\2\u00d4\u00ce\3\2\2\2\u00d4\u00cf\3")
        buf.write("\2\2\2\u00d4\u00d0\3\2\2\2\u00d4\u00d1\3\2\2\2\u00d4\u00d2")
        buf.write("\3\2\2\2\u00d4\u00d3\3\2\2\2\u00d5%\3\2\2\2\u00d6\u00d7")
        buf.write("\58\35\2\u00d7\u00d8\7\61\2\2\u00d8\'\3\2\2\2\u00d9\u00da")
        buf.write("\7\27\2\2\u00da\u00db\7)\2\2\u00db\u00dc\58\35\2\u00dc")
        buf.write("\u00dd\7*\2\2\u00dd\u00e0\5\"\22\2\u00de\u00df\7\26\2")
        buf.write("\2\u00df\u00e1\5\"\22\2\u00e0\u00de\3\2\2\2\u00e0\u00e1")
        buf.write("\3\2\2\2\u00e1)\3\2\2\2\u00e2\u00e3\7\20\2\2\u00e3\u00e4")
        buf.write("\7)\2\2\u00e4\u00e5\5\20\t\2\u00e5\u00e6\7*\2\2\u00e6")
        buf.write("+\3\2\2\2\u00e7\u00e8\7\b\2\2\u00e8\u00e9\7)\2\2\u00e9")
        buf.write("\u00ea\58\35\2\u00ea\u00eb\7*\2\2\u00eb-\3\2\2\2\u00ec")
        buf.write("\u00ed\7\23\2\2\u00ed\u00ee\5 \21\2\u00ee\u00ef\7\b\2")
        buf.write("\2\u00ef\u00f0\7)\2\2\u00f0\u00f1\58\35\2\u00f1\u00f2")
        buf.write("\7*\2\2\u00f2/\3\2\2\2\u00f3\u00f4\7\n\2\2\u00f4\u00f5")
        buf.write("\7\61\2\2\u00f5\61\3\2\2\2\u00f6\u00f7\7\30\2\2\u00f7")
        buf.write("\u00f8\7\61\2\2\u00f8\63\3\2\2\2\u00f9\u00fb\7\f\2\2\u00fa")
        buf.write("\u00fc\58\35\2\u00fb\u00fa\3\2\2\2\u00fb\u00fc\3\2\2\2")
        buf.write("\u00fc\u00fd\3\2\2\2\u00fd\u00fe\7\61\2\2\u00fe\65\3\2")
        buf.write("\2\2\u00ff\u0100\5N(\2\u0100\u0101\7\61\2\2\u0101\67\3")
        buf.write("\2\2\2\u0102\u0107\5:\36\2\u0103\u0104\7\60\2\2\u0104")
        buf.write("\u0106\5:\36\2\u0105\u0103\3\2\2\2\u0106\u0109\3\2\2\2")
        buf.write("\u0107\u0105\3\2\2\2\u0107\u0108\3\2\2\2\u01089\3\2\2")
        buf.write("\2\u0109\u0107\3\2\2\2\u010a\u010b\5F$\2\u010b\u010c\7")
        buf.write("\63\2\2\u010c\u010d\5:\36\2\u010d\u0110\3\2\2\2\u010e")
        buf.write("\u0110\5<\37\2\u010f\u010a\3\2\2\2\u010f\u010e\3\2\2\2")
        buf.write("\u0110;\3\2\2\2\u0111\u0112\5> \2\u0112\u0113\7(\2\2\u0113")
        buf.write("\u0114\5> \2\u0114\u0117\3\2\2\2\u0115\u0117\5> \2\u0116")
        buf.write("\u0111\3\2\2\2\u0116\u0115\3\2\2\2\u0117=\3\2\2\2\u0118")
        buf.write("\u0119\5@!\2\u0119\u011a\t\3\2\2\u011a\u011b\5@!\2\u011b")
        buf.write("\u011e\3\2\2\2\u011c\u011e\5@!\2\u011d\u0118\3\2\2\2\u011d")
        buf.write("\u011c\3\2\2\2\u011e?\3\2\2\2\u011f\u0120\b!\1\2\u0120")
        buf.write("\u0121\5B\"\2\u0121\u0127\3\2\2\2\u0122\u0123\f\4\2\2")
        buf.write("\u0123\u0124\t\4\2\2\u0124\u0126\5B\"\2\u0125\u0122\3")
        buf.write("\2\2\2\u0126\u0129\3\2\2\2\u0127\u0125\3\2\2\2\u0127\u0128")
        buf.write("\3\2\2\2\u0128A\3\2\2\2\u0129\u0127\3\2\2\2\u012a\u012b")
        buf.write("\b\"\1\2\u012b\u012c\5D#\2\u012c\u0132\3\2\2\2\u012d\u012e")
        buf.write("\f\4\2\2\u012e\u012f\t\5\2\2\u012f\u0131\5D#\2\u0130\u012d")
        buf.write("\3\2\2\2\u0131\u0134\3\2\2\2\u0132\u0130\3\2\2\2\u0132")
        buf.write("\u0133\3\2\2\2\u0133C\3\2\2\2\u0134\u0132\3\2\2\2\u0135")
        buf.write("\u0136\b#\1\2\u0136\u0137\5F$\2\u0137\u013d\3\2\2\2\u0138")
        buf.write("\u0139\f\4\2\2\u0139\u013a\t\6\2\2\u013a\u013c\5F$\2\u013b")
        buf.write("\u0138\3\2\2\2\u013c\u013f\3\2\2\2\u013d\u013b\3\2\2\2")
        buf.write("\u013d\u013e\3\2\2\2\u013eE\3\2\2\2\u013f\u013d\3\2\2")
        buf.write("\2\u0140\u0141\7\37\2\2\u0141\u0144\5F$\2\u0142\u0144")
        buf.write("\5H%\2\u0143\u0140\3\2\2\2\u0143\u0142\3\2\2\2\u0144G")
        buf.write("\3\2\2\2\u0145\u0146\7\33\2\2\u0146\u0149\5H%\2\u0147")
        buf.write("\u0149\5J&\2\u0148\u0145\3\2\2\2\u0148\u0147\3\2\2\2\u0149")
        buf.write("I\3\2\2\2\u014a\u014b\b&\1\2\u014b\u014c\5L\'\2\u014c")
        buf.write("\u0154\3\2\2\2\u014d\u014e\f\4\2\2\u014e\u014f\7+\2\2")
        buf.write("\u014f\u0150\58\35\2\u0150\u0151\7,\2\2\u0151\u0153\3")
        buf.write("\2\2\2\u0152\u014d\3\2\2\2\u0153\u0156\3\2\2\2\u0154\u0152")
        buf.write("\3\2\2\2\u0154\u0155\3\2\2\2\u0155K\3\2\2\2\u0156\u0154")
        buf.write("\3\2\2\2\u0157\u015f\7\66\2\2\u0158\u015f\7\65\2\2\u0159")
        buf.write("\u015f\5N(\2\u015a\u015b\7)\2\2\u015b\u015c\58\35\2\u015c")
        buf.write("\u015d\7*\2\2\u015d\u015f\3\2\2\2\u015e\u0157\3\2\2\2")
        buf.write("\u015e\u0158\3\2\2\2\u015e\u0159\3\2\2\2\u015e\u015a\3")
        buf.write("\2\2\2\u015fM\3\2\2\2\u0160\u0161\7\65\2\2\u0161\u0163")
        buf.write("\7)\2\2\u0162\u0164\58\35\2\u0163\u0162\3\2\2\2\u0163")
        buf.write("\u0164\3\2\2\2\u0164\u0165\3\2\2\2\u0165\u0166\7*\2\2")
        buf.write("\u0166O\3\2\2\2!VZ^ry}\u0084\u008b\u0096\u009e\u00a1\u00b3")
        buf.write("\u00b8\u00be\u00c0\u00c8\u00d4\u00e0\u00fb\u0107\u010f")
        buf.write("\u0116\u011d\u0127\u0132\u013d\u0143\u0148\u0154\u015e")
        buf.write("\u0163")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'auto'", "'false'", 
                     "'integer'", "'while'", "'of'", "'break'", "'float'", 
                     "'return'", "'void'", "'inherit'", "'boolean'", "'for'", 
                     "'string'", "'function'", "'do'", "'true'", "'out'", 
                     "'else'", "'if'", "'continue'", "'array'", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
                     "'!='", "'<'", "'<='", "'>'", "'>='", "'::'", "'('", 
                     "')'", "'['", "']'", "'{'", "'}'", "'.'", "','", "';'", 
                     "':'", "'='", "'_'" ]

    symbolicNames = [ "<INVALID>", "BlockComment", "LineComment", "Auto", 
                      "False_", "Integer", "While", "Of", "Break", "Float", 
                      "Return", "Void", "Inherit", "Boolean_", "For", "String", 
                      "Function", "Do", "True_", "Out", "Else", "If", "Continue", 
                      "Array", "Plus", "Minus", "Star", "Div", "Mod", "Not", 
                      "AndAnd", "OrOr", "Equal", "NotEqual", "Less", "LessEqual", 
                      "Greater", "GreaterEqual", "ColonColon", "LeftParen", 
                      "RightParen", "LeftBracket", "RightBracket", "LeftBrace", 
                      "RightBrace", "Dot", "Comma", "Semi", "Colon", "Assign", 
                      "Under", "Identifier", "Literal", "IntegerConstant", 
                      "FloatingConstant", "DigitSequence", "StringLiteral", 
                      "Boolean", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_declarations = 1
    RULE_declaration = 2
    RULE_variableDeclaration = 3
    RULE_shortDeclaration = 4
    RULE_longDeclaration = 5
    RULE_initializer = 6
    RULE_identifiers = 7
    RULE_typeName = 8
    RULE_atomicType = 9
    RULE_arrayType = 10
    RULE_parameter = 11
    RULE_functionDeclaration = 12
    RULE_functionPrototype = 13
    RULE_parameters = 14
    RULE_blockStatement = 15
    RULE_statements = 16
    RULE_statement = 17
    RULE_assignmentStatement = 18
    RULE_ifStatement = 19
    RULE_forStatement = 20
    RULE_whileStatement = 21
    RULE_do_whileStatement = 22
    RULE_breakStatement = 23
    RULE_continueStatement = 24
    RULE_returnStatement = 25
    RULE_callStatement = 26
    RULE_expressions = 27
    RULE_expression = 28
    RULE_stringExpression = 29
    RULE_relationalExpression = 30
    RULE_logicalExpression = 31
    RULE_additiveExpression = 32
    RULE_multiplicativeExpression = 33
    RULE_unaryExpression = 34
    RULE_signExpression = 35
    RULE_postfixExpression = 36
    RULE_primaryExpression = 37
    RULE_functionCall = 38

    ruleNames =  [ "program", "declarations", "declaration", "variableDeclaration", 
                   "shortDeclaration", "longDeclaration", "initializer", 
                   "identifiers", "typeName", "atomicType", "arrayType", 
                   "parameter", "functionDeclaration", "functionPrototype", 
                   "parameters", "blockStatement", "statements", "statement", 
                   "assignmentStatement", "ifStatement", "forStatement", 
                   "whileStatement", "do_whileStatement", "breakStatement", 
                   "continueStatement", "returnStatement", "callStatement", 
                   "expressions", "expression", "stringExpression", "relationalExpression", 
                   "logicalExpression", "additiveExpression", "multiplicativeExpression", 
                   "unaryExpression", "signExpression", "postfixExpression", 
                   "primaryExpression", "functionCall" ]

    EOF = Token.EOF
    BlockComment=1
    LineComment=2
    Auto=3
    False_=4
    Integer=5
    While=6
    Of=7
    Break=8
    Float=9
    Return=10
    Void=11
    Inherit=12
    Boolean_=13
    For=14
    String=15
    Function=16
    Do=17
    True_=18
    Out=19
    Else=20
    If=21
    Continue=22
    Array=23
    Plus=24
    Minus=25
    Star=26
    Div=27
    Mod=28
    Not=29
    AndAnd=30
    OrOr=31
    Equal=32
    NotEqual=33
    Less=34
    LessEqual=35
    Greater=36
    GreaterEqual=37
    ColonColon=38
    LeftParen=39
    RightParen=40
    LeftBracket=41
    RightBracket=42
    LeftBrace=43
    RightBrace=44
    Dot=45
    Comma=46
    Semi=47
    Colon=48
    Assign=49
    Under=50
    Identifier=51
    Literal=52
    IntegerConstant=53
    FloatingConstant=54
    DigitSequence=55
    StringLiteral=56
    Boolean=57
    WS=58
    ERROR_CHAR=59
    UNCLOSE_STRING=60
    ILLEGAL_ESCAPE=61

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

        def declarations(self):
            return self.getTypedRuleContext(MT22Parser.DeclarationsContext,0)


        def EOF(self):
            return self.getToken(MT22Parser.EOF, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MT22Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.declarations()
            self.state = 79
            self.match(MT22Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.DeclarationContext)
            else:
                return self.getTypedRuleContext(MT22Parser.DeclarationContext,i)


        def getRuleIndex(self):
            return MT22Parser.RULE_declarations

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclarations" ):
                return visitor.visitDeclarations(self)
            else:
                return visitor.visitChildren(self)




    def declarations(self):

        localctx = MT22Parser.DeclarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declarations)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 81
                self.declaration()
                self.state = 84 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MT22Parser.Identifier):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self):
            return self.getTypedRuleContext(MT22Parser.VariableDeclarationContext,0)


        def functionDeclaration(self):
            return self.getTypedRuleContext(MT22Parser.FunctionDeclarationContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = MT22Parser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaration)
        try:
            self.state = 88
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.variableDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.functionDeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Semi(self):
            return self.getToken(MT22Parser.Semi, 0)

        def shortDeclaration(self):
            return self.getTypedRuleContext(MT22Parser.ShortDeclarationContext,0)


        def longDeclaration(self):
            return self.getTypedRuleContext(MT22Parser.LongDeclarationContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_variableDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclaration" ):
                return visitor.visitVariableDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclaration(self):

        localctx = MT22Parser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variableDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 90
                self.shortDeclaration()
                pass

            elif la_ == 2:
                self.state = 91
                self.longDeclaration()
                pass


            self.state = 94
            self.match(MT22Parser.Semi)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShortDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifiers(self):
            return self.getTypedRuleContext(MT22Parser.IdentifiersContext,0)


        def Colon(self):
            return self.getToken(MT22Parser.Colon, 0)

        def typeName(self):
            return self.getTypedRuleContext(MT22Parser.TypeNameContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_shortDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShortDeclaration" ):
                return visitor.visitShortDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def shortDeclaration(self):

        localctx = MT22Parser.ShortDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_shortDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.identifiers()
            self.state = 97
            self.match(MT22Parser.Colon)
            self.state = 98
            self.typeName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LongDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(MT22Parser.Identifier, 0)

        def Colon(self):
            return self.getToken(MT22Parser.Colon, 0)

        def typeName(self):
            return self.getTypedRuleContext(MT22Parser.TypeNameContext,0)


        def Assign(self):
            return self.getToken(MT22Parser.Assign, 0)

        def initializer(self):
            return self.getTypedRuleContext(MT22Parser.InitializerContext,0)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.Comma)
            else:
                return self.getToken(MT22Parser.Comma, i)

        def longDeclaration(self):
            return self.getTypedRuleContext(MT22Parser.LongDeclarationContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_longDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLongDeclaration" ):
                return visitor.visitLongDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def longDeclaration(self):

        localctx = MT22Parser.LongDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_longDeclaration)
        try:
            self.state = 112
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 100
                self.match(MT22Parser.Identifier)
                self.state = 101
                self.match(MT22Parser.Colon)
                self.state = 102
                self.typeName()
                self.state = 103
                self.match(MT22Parser.Assign)
                self.state = 104
                self.initializer()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 106
                self.match(MT22Parser.Identifier)
                self.state = 107
                self.match(MT22Parser.Comma)
                self.state = 108
                self.longDeclaration()
                self.state = 109
                self.match(MT22Parser.Comma)
                self.state = 110
                self.initializer()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitializerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def LeftBrace(self):
            return self.getToken(MT22Parser.LeftBrace, 0)

        def RightBrace(self):
            return self.getToken(MT22Parser.RightBrace, 0)

        def initializer(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.InitializerContext)
            else:
                return self.getTypedRuleContext(MT22Parser.InitializerContext,i)


        def getRuleIndex(self):
            return MT22Parser.RULE_initializer

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitializer" ):
                return visitor.visitInitializer(self)
            else:
                return visitor.visitChildren(self)




    def initializer(self):

        localctx = MT22Parser.InitializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_initializer)
        self._la = 0 # Token type
        try:
            self.state = 123
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.Minus, MT22Parser.Not, MT22Parser.LeftParen, MT22Parser.Identifier, MT22Parser.Literal]:
                self.enterOuterAlt(localctx, 1)
                self.state = 114
                self.expression()
                pass
            elif token in [MT22Parser.LeftBrace]:
                self.enterOuterAlt(localctx, 2)
                self.state = 115
                self.match(MT22Parser.LeftBrace)
                self.state = 117 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 116
                    self.initializer()
                    self.state = 119 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.Minus) | (1 << MT22Parser.Not) | (1 << MT22Parser.LeftParen) | (1 << MT22Parser.LeftBrace) | (1 << MT22Parser.Identifier) | (1 << MT22Parser.Literal))) != 0)):
                        break

                self.state = 121
                self.match(MT22Parser.RightBrace)
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


    class IdentifiersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.Identifier)
            else:
                return self.getToken(MT22Parser.Identifier, i)

        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.Comma)
            else:
                return self.getToken(MT22Parser.Comma, i)

        def getRuleIndex(self):
            return MT22Parser.RULE_identifiers

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifiers" ):
                return visitor.visitIdentifiers(self)
            else:
                return visitor.visitChildren(self)




    def identifiers(self):

        localctx = MT22Parser.IdentifiersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_identifiers)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(MT22Parser.Identifier)
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MT22Parser.Comma:
                self.state = 126
                self.match(MT22Parser.Comma)
                self.state = 127
                self.match(MT22Parser.Identifier)
                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atomicType(self):
            return self.getTypedRuleContext(MT22Parser.AtomicTypeContext,0)


        def Void(self):
            return self.getToken(MT22Parser.Void, 0)

        def Auto(self):
            return self.getToken(MT22Parser.Auto, 0)

        def arrayType(self):
            return self.getTypedRuleContext(MT22Parser.ArrayTypeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_typeName

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeName" ):
                return visitor.visitTypeName(self)
            else:
                return visitor.visitChildren(self)




    def typeName(self):

        localctx = MT22Parser.TypeNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_typeName)
        try:
            self.state = 137
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.Integer, MT22Parser.Float, MT22Parser.String, MT22Parser.Boolean]:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.atomicType()
                pass
            elif token in [MT22Parser.Void]:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.match(MT22Parser.Void)
                pass
            elif token in [MT22Parser.Auto]:
                self.enterOuterAlt(localctx, 3)
                self.state = 135
                self.match(MT22Parser.Auto)
                pass
            elif token in [MT22Parser.Array]:
                self.enterOuterAlt(localctx, 4)
                self.state = 136
                self.arrayType()
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


    class AtomicTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Boolean(self):
            return self.getToken(MT22Parser.Boolean, 0)

        def Integer(self):
            return self.getToken(MT22Parser.Integer, 0)

        def Float(self):
            return self.getToken(MT22Parser.Float, 0)

        def String(self):
            return self.getToken(MT22Parser.String, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_atomicType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomicType" ):
                return visitor.visitAtomicType(self)
            else:
                return visitor.visitChildren(self)




    def atomicType(self):

        localctx = MT22Parser.AtomicTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_atomicType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.Integer) | (1 << MT22Parser.Float) | (1 << MT22Parser.String) | (1 << MT22Parser.Boolean))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Array(self):
            return self.getToken(MT22Parser.Array, 0)

        def LeftBracket(self):
            return self.getToken(MT22Parser.LeftBracket, 0)

        def IntegerConstant(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.IntegerConstant)
            else:
                return self.getToken(MT22Parser.IntegerConstant, i)

        def RightBracket(self):
            return self.getToken(MT22Parser.RightBracket, 0)

        def Of(self):
            return self.getToken(MT22Parser.Of, 0)

        def atomicType(self):
            return self.getTypedRuleContext(MT22Parser.AtomicTypeContext,0)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.Comma)
            else:
                return self.getToken(MT22Parser.Comma, i)

        def getRuleIndex(self):
            return MT22Parser.RULE_arrayType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayType" ):
                return visitor.visitArrayType(self)
            else:
                return visitor.visitChildren(self)




    def arrayType(self):

        localctx = MT22Parser.ArrayTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_arrayType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(MT22Parser.Array)
            self.state = 142
            self.match(MT22Parser.LeftBracket)
            self.state = 143
            self.match(MT22Parser.IntegerConstant)
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MT22Parser.Comma:
                self.state = 144
                self.match(MT22Parser.Comma)
                self.state = 145
                self.match(MT22Parser.IntegerConstant)
                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 151
            self.match(MT22Parser.RightBracket)
            self.state = 152
            self.match(MT22Parser.Of)
            self.state = 153
            self.atomicType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(MT22Parser.Identifier, 0)

        def Colon(self):
            return self.getToken(MT22Parser.Colon, 0)

        def typeName(self):
            return self.getTypedRuleContext(MT22Parser.TypeNameContext,0)


        def Inherit(self):
            return self.getToken(MT22Parser.Inherit, 0)

        def Out(self):
            return self.getToken(MT22Parser.Out, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = MT22Parser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.Inherit:
                self.state = 155
                self.match(MT22Parser.Inherit)


            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.Out:
                self.state = 158
                self.match(MT22Parser.Out)


            self.state = 161
            self.match(MT22Parser.Identifier)
            self.state = 162
            self.match(MT22Parser.Colon)
            self.state = 163
            self.typeName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionPrototype(self):
            return self.getTypedRuleContext(MT22Parser.FunctionPrototypeContext,0)


        def blockStatement(self):
            return self.getTypedRuleContext(MT22Parser.BlockStatementContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_functionDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDeclaration" ):
                return visitor.visitFunctionDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def functionDeclaration(self):

        localctx = MT22Parser.FunctionDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_functionDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.functionPrototype()
            self.state = 166
            self.blockStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionPrototypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.Identifier)
            else:
                return self.getToken(MT22Parser.Identifier, i)

        def Colon(self):
            return self.getToken(MT22Parser.Colon, 0)

        def Function(self):
            return self.getToken(MT22Parser.Function, 0)

        def typeName(self):
            return self.getTypedRuleContext(MT22Parser.TypeNameContext,0)


        def LeftParen(self):
            return self.getToken(MT22Parser.LeftParen, 0)

        def parameters(self):
            return self.getTypedRuleContext(MT22Parser.ParametersContext,0)


        def RightParen(self):
            return self.getToken(MT22Parser.RightParen, 0)

        def Inherit(self):
            return self.getToken(MT22Parser.Inherit, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_functionPrototype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionPrototype" ):
                return visitor.visitFunctionPrototype(self)
            else:
                return visitor.visitChildren(self)




    def functionPrototype(self):

        localctx = MT22Parser.FunctionPrototypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_functionPrototype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(MT22Parser.Identifier)
            self.state = 169
            self.match(MT22Parser.Colon)
            self.state = 170
            self.match(MT22Parser.Function)
            self.state = 171
            self.typeName()
            self.state = 172
            self.match(MT22Parser.LeftParen)
            self.state = 173
            self.parameters()
            self.state = 174
            self.match(MT22Parser.RightParen)
            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.Inherit:
                self.state = 175
                self.match(MT22Parser.Inherit)
                self.state = 176
                self.match(MT22Parser.Identifier)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.ParameterContext)
            else:
                return self.getTypedRuleContext(MT22Parser.ParameterContext,i)


        def getRuleIndex(self):
            return MT22Parser.RULE_parameters

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameters" ):
                return visitor.visitParameters(self)
            else:
                return visitor.visitChildren(self)




    def parameters(self):

        localctx = MT22Parser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.Inherit) | (1 << MT22Parser.Out) | (1 << MT22Parser.Identifier))) != 0):
                self.state = 179
                self.parameter()
                self.state = 184
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LeftBracket(self):
            return self.getToken(MT22Parser.LeftBracket, 0)

        def RightBracket(self):
            return self.getToken(MT22Parser.RightBracket, 0)

        def statements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.StatementsContext)
            else:
                return self.getTypedRuleContext(MT22Parser.StatementsContext,i)


        def variableDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.VariableDeclarationContext)
            else:
                return self.getTypedRuleContext(MT22Parser.VariableDeclarationContext,i)


        def getRuleIndex(self):
            return MT22Parser.RULE_blockStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockStatement" ):
                return visitor.visitBlockStatement(self)
            else:
                return visitor.visitChildren(self)




    def blockStatement(self):

        localctx = MT22Parser.BlockStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_blockStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.match(MT22Parser.LeftBracket)
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.While) | (1 << MT22Parser.Break) | (1 << MT22Parser.Return) | (1 << MT22Parser.For) | (1 << MT22Parser.Do) | (1 << MT22Parser.If) | (1 << MT22Parser.Continue) | (1 << MT22Parser.Minus) | (1 << MT22Parser.Not) | (1 << MT22Parser.LeftParen) | (1 << MT22Parser.LeftBracket) | (1 << MT22Parser.Identifier) | (1 << MT22Parser.Literal))) != 0):
                self.state = 188
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                if la_ == 1:
                    self.state = 186
                    self.statements()
                    pass

                elif la_ == 2:
                    self.state = 187
                    self.variableDeclaration()
                    pass


                self.state = 192
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 193
            self.match(MT22Parser.RightBracket)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.StatementContext)
            else:
                return self.getTypedRuleContext(MT22Parser.StatementContext,i)


        def getRuleIndex(self):
            return MT22Parser.RULE_statements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatements" ):
                return visitor.visitStatements(self)
            else:
                return visitor.visitChildren(self)




    def statements(self):

        localctx = MT22Parser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 195
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 198 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignmentStatement(self):
            return self.getTypedRuleContext(MT22Parser.AssignmentStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(MT22Parser.IfStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(MT22Parser.ForStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(MT22Parser.WhileStatementContext,0)


        def do_whileStatement(self):
            return self.getTypedRuleContext(MT22Parser.Do_whileStatementContext,0)


        def breakStatement(self):
            return self.getTypedRuleContext(MT22Parser.BreakStatementContext,0)


        def continueStatement(self):
            return self.getTypedRuleContext(MT22Parser.ContinueStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(MT22Parser.ReturnStatementContext,0)


        def callStatement(self):
            return self.getTypedRuleContext(MT22Parser.CallStatementContext,0)


        def blockStatement(self):
            return self.getTypedRuleContext(MT22Parser.BlockStatementContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MT22Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_statement)
        try:
            self.state = 210
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.assignmentStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
                self.ifStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 202
                self.forStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 203
                self.whileStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 204
                self.do_whileStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 205
                self.breakStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 206
                self.continueStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 207
                self.returnStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 208
                self.callStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 209
                self.blockStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressions(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionsContext,0)


        def Semi(self):
            return self.getToken(MT22Parser.Semi, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_assignmentStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentStatement" ):
                return visitor.visitAssignmentStatement(self)
            else:
                return visitor.visitChildren(self)




    def assignmentStatement(self):

        localctx = MT22Parser.AssignmentStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_assignmentStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.expressions()
            self.state = 213
            self.match(MT22Parser.Semi)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def If(self):
            return self.getToken(MT22Parser.If, 0)

        def LeftParen(self):
            return self.getToken(MT22Parser.LeftParen, 0)

        def expressions(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionsContext,0)


        def RightParen(self):
            return self.getToken(MT22Parser.RightParen, 0)

        def statements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.StatementsContext)
            else:
                return self.getTypedRuleContext(MT22Parser.StatementsContext,i)


        def Else(self):
            return self.getToken(MT22Parser.Else, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_ifStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = MT22Parser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(MT22Parser.If)
            self.state = 216
            self.match(MT22Parser.LeftParen)
            self.state = 217
            self.expressions()
            self.state = 218
            self.match(MT22Parser.RightParen)
            self.state = 219
            self.statements()
            self.state = 222
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 220
                self.match(MT22Parser.Else)
                self.state = 221
                self.statements()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def For(self):
            return self.getToken(MT22Parser.For, 0)

        def LeftParen(self):
            return self.getToken(MT22Parser.LeftParen, 0)

        def identifiers(self):
            return self.getTypedRuleContext(MT22Parser.IdentifiersContext,0)


        def RightParen(self):
            return self.getToken(MT22Parser.RightParen, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_forStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = MT22Parser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(MT22Parser.For)
            self.state = 225
            self.match(MT22Parser.LeftParen)
            self.state = 226
            self.identifiers()
            self.state = 227
            self.match(MT22Parser.RightParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def While(self):
            return self.getToken(MT22Parser.While, 0)

        def LeftParen(self):
            return self.getToken(MT22Parser.LeftParen, 0)

        def expressions(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionsContext,0)


        def RightParen(self):
            return self.getToken(MT22Parser.RightParen, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_whileStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = MT22Parser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(MT22Parser.While)
            self.state = 230
            self.match(MT22Parser.LeftParen)
            self.state = 231
            self.expressions()
            self.state = 232
            self.match(MT22Parser.RightParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Do_whileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Do(self):
            return self.getToken(MT22Parser.Do, 0)

        def blockStatement(self):
            return self.getTypedRuleContext(MT22Parser.BlockStatementContext,0)


        def While(self):
            return self.getToken(MT22Parser.While, 0)

        def LeftParen(self):
            return self.getToken(MT22Parser.LeftParen, 0)

        def expressions(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionsContext,0)


        def RightParen(self):
            return self.getToken(MT22Parser.RightParen, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_do_whileStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDo_whileStatement" ):
                return visitor.visitDo_whileStatement(self)
            else:
                return visitor.visitChildren(self)




    def do_whileStatement(self):

        localctx = MT22Parser.Do_whileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_do_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(MT22Parser.Do)
            self.state = 235
            self.blockStatement()
            self.state = 236
            self.match(MT22Parser.While)
            self.state = 237
            self.match(MT22Parser.LeftParen)
            self.state = 238
            self.expressions()
            self.state = 239
            self.match(MT22Parser.RightParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Break(self):
            return self.getToken(MT22Parser.Break, 0)

        def Semi(self):
            return self.getToken(MT22Parser.Semi, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_breakStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStatement" ):
                return visitor.visitBreakStatement(self)
            else:
                return visitor.visitChildren(self)




    def breakStatement(self):

        localctx = MT22Parser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(MT22Parser.Break)
            self.state = 242
            self.match(MT22Parser.Semi)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Continue(self):
            return self.getToken(MT22Parser.Continue, 0)

        def Semi(self):
            return self.getToken(MT22Parser.Semi, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_continueStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStatement" ):
                return visitor.visitContinueStatement(self)
            else:
                return visitor.visitChildren(self)




    def continueStatement(self):

        localctx = MT22Parser.ContinueStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(MT22Parser.Continue)
            self.state = 245
            self.match(MT22Parser.Semi)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Return(self):
            return self.getToken(MT22Parser.Return, 0)

        def Semi(self):
            return self.getToken(MT22Parser.Semi, 0)

        def expressions(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionsContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_returnStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = MT22Parser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(MT22Parser.Return)
            self.state = 249
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.Minus) | (1 << MT22Parser.Not) | (1 << MT22Parser.LeftParen) | (1 << MT22Parser.Identifier) | (1 << MT22Parser.Literal))) != 0):
                self.state = 248
                self.expressions()


            self.state = 251
            self.match(MT22Parser.Semi)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionCall(self):
            return self.getTypedRuleContext(MT22Parser.FunctionCallContext,0)


        def Semi(self):
            return self.getToken(MT22Parser.Semi, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_callStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallStatement" ):
                return visitor.visitCallStatement(self)
            else:
                return visitor.visitChildren(self)




    def callStatement(self):

        localctx = MT22Parser.CallStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_callStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.functionCall()
            self.state = 254
            self.match(MT22Parser.Semi)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MT22Parser.ExpressionContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.Comma)
            else:
                return self.getToken(MT22Parser.Comma, i)

        def getRuleIndex(self):
            return MT22Parser.RULE_expressions

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressions" ):
                return visitor.visitExpressions(self)
            else:
                return visitor.visitChildren(self)




    def expressions(self):

        localctx = MT22Parser.ExpressionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_expressions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.expression()
            self.state = 261
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MT22Parser.Comma:
                self.state = 257
                self.match(MT22Parser.Comma)
                self.state = 258
                self.expression()
                self.state = 263
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def unaryExpression(self):
            return self.getTypedRuleContext(MT22Parser.UnaryExpressionContext,0)


        def Assign(self):
            return self.getToken(MT22Parser.Assign, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def stringExpression(self):
            return self.getTypedRuleContext(MT22Parser.StringExpressionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = MT22Parser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_expression)
        try:
            self.state = 269
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 264
                self.unaryExpression()
                self.state = 265
                self.match(MT22Parser.Assign)
                self.state = 266
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 268
                self.stringExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relationalExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.RelationalExpressionContext)
            else:
                return self.getTypedRuleContext(MT22Parser.RelationalExpressionContext,i)


        def ColonColon(self):
            return self.getToken(MT22Parser.ColonColon, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_stringExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringExpression" ):
                return visitor.visitStringExpression(self)
            else:
                return visitor.visitChildren(self)




    def stringExpression(self):

        localctx = MT22Parser.StringExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_stringExpression)
        try:
            self.state = 276
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 271
                self.relationalExpression()
                self.state = 272
                self.match(MT22Parser.ColonColon)
                self.state = 273
                self.relationalExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 275
                self.relationalExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.LogicalExpressionContext)
            else:
                return self.getTypedRuleContext(MT22Parser.LogicalExpressionContext,i)


        def Equal(self):
            return self.getToken(MT22Parser.Equal, 0)

        def NotEqual(self):
            return self.getToken(MT22Parser.NotEqual, 0)

        def Less(self):
            return self.getToken(MT22Parser.Less, 0)

        def Greater(self):
            return self.getToken(MT22Parser.Greater, 0)

        def LessEqual(self):
            return self.getToken(MT22Parser.LessEqual, 0)

        def GreaterEqual(self):
            return self.getToken(MT22Parser.GreaterEqual, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_relationalExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalExpression" ):
                return visitor.visitRelationalExpression(self)
            else:
                return visitor.visitChildren(self)




    def relationalExpression(self):

        localctx = MT22Parser.RelationalExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_relationalExpression)
        self._la = 0 # Token type
        try:
            self.state = 283
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 278
                self.logicalExpression(0)
                self.state = 279
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.Equal) | (1 << MT22Parser.NotEqual) | (1 << MT22Parser.Less) | (1 << MT22Parser.LessEqual) | (1 << MT22Parser.Greater) | (1 << MT22Parser.GreaterEqual))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 280
                self.logicalExpression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 282
                self.logicalExpression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpression(self):
            return self.getTypedRuleContext(MT22Parser.AdditiveExpressionContext,0)


        def logicalExpression(self):
            return self.getTypedRuleContext(MT22Parser.LogicalExpressionContext,0)


        def AndAnd(self):
            return self.getToken(MT22Parser.AndAnd, 0)

        def OrOr(self):
            return self.getToken(MT22Parser.OrOr, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_logicalExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalExpression" ):
                return visitor.visitLogicalExpression(self)
            else:
                return visitor.visitChildren(self)



    def logicalExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.LogicalExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_logicalExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.additiveExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 293
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.LogicalExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalExpression)
                    self.state = 288
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 289
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.AndAnd or _la==MT22Parser.OrOr):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 290
                    self.additiveExpression(0) 
                self.state = 295
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AdditiveExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpression(self):
            return self.getTypedRuleContext(MT22Parser.MultiplicativeExpressionContext,0)


        def additiveExpression(self):
            return self.getTypedRuleContext(MT22Parser.AdditiveExpressionContext,0)


        def Plus(self):
            return self.getToken(MT22Parser.Plus, 0)

        def Minus(self):
            return self.getToken(MT22Parser.Minus, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_additiveExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpression" ):
                return visitor.visitAdditiveExpression(self)
            else:
                return visitor.visitChildren(self)



    def additiveExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.AdditiveExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_additiveExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.multiplicativeExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 304
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.AdditiveExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_additiveExpression)
                    self.state = 299
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 300
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.Plus or _la==MT22Parser.Minus):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 301
                    self.multiplicativeExpression(0) 
                self.state = 306
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MultiplicativeExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpression(self):
            return self.getTypedRuleContext(MT22Parser.UnaryExpressionContext,0)


        def multiplicativeExpression(self):
            return self.getTypedRuleContext(MT22Parser.MultiplicativeExpressionContext,0)


        def Star(self):
            return self.getToken(MT22Parser.Star, 0)

        def Div(self):
            return self.getToken(MT22Parser.Div, 0)

        def Mod(self):
            return self.getToken(MT22Parser.Mod, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_multiplicativeExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExpression" ):
                return visitor.visitMultiplicativeExpression(self)
            else:
                return visitor.visitChildren(self)



    def multiplicativeExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.MultiplicativeExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_multiplicativeExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.unaryExpression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 315
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.MultiplicativeExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicativeExpression)
                    self.state = 310
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 311
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.Star) | (1 << MT22Parser.Div) | (1 << MT22Parser.Mod))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 312
                    self.unaryExpression() 
                self.state = 317
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class UnaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Not(self):
            return self.getToken(MT22Parser.Not, 0)

        def unaryExpression(self):
            return self.getTypedRuleContext(MT22Parser.UnaryExpressionContext,0)


        def signExpression(self):
            return self.getTypedRuleContext(MT22Parser.SignExpressionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_unaryExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpression" ):
                return visitor.visitUnaryExpression(self)
            else:
                return visitor.visitChildren(self)




    def unaryExpression(self):

        localctx = MT22Parser.UnaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_unaryExpression)
        try:
            self.state = 321
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.Not]:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self.match(MT22Parser.Not)
                self.state = 319
                self.unaryExpression()
                pass
            elif token in [MT22Parser.Minus, MT22Parser.LeftParen, MT22Parser.Identifier, MT22Parser.Literal]:
                self.enterOuterAlt(localctx, 2)
                self.state = 320
                self.signExpression()
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


    class SignExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Minus(self):
            return self.getToken(MT22Parser.Minus, 0)

        def signExpression(self):
            return self.getTypedRuleContext(MT22Parser.SignExpressionContext,0)


        def postfixExpression(self):
            return self.getTypedRuleContext(MT22Parser.PostfixExpressionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_signExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSignExpression" ):
                return visitor.visitSignExpression(self)
            else:
                return visitor.visitChildren(self)




    def signExpression(self):

        localctx = MT22Parser.SignExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_signExpression)
        try:
            self.state = 326
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.Minus]:
                self.enterOuterAlt(localctx, 1)
                self.state = 323
                self.match(MT22Parser.Minus)
                self.state = 324
                self.signExpression()
                pass
            elif token in [MT22Parser.LeftParen, MT22Parser.Identifier, MT22Parser.Literal]:
                self.enterOuterAlt(localctx, 2)
                self.state = 325
                self.postfixExpression(0)
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


    class PostfixExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primaryExpression(self):
            return self.getTypedRuleContext(MT22Parser.PrimaryExpressionContext,0)


        def postfixExpression(self):
            return self.getTypedRuleContext(MT22Parser.PostfixExpressionContext,0)


        def LeftBracket(self):
            return self.getToken(MT22Parser.LeftBracket, 0)

        def expressions(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionsContext,0)


        def RightBracket(self):
            return self.getToken(MT22Parser.RightBracket, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_postfixExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostfixExpression" ):
                return visitor.visitPostfixExpression(self)
            else:
                return visitor.visitChildren(self)



    def postfixExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.PostfixExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_postfixExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.primaryExpression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 338
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.PostfixExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_postfixExpression)
                    self.state = 331
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 332
                    self.match(MT22Parser.LeftBracket)
                    self.state = 333
                    self.expressions()
                    self.state = 334
                    self.match(MT22Parser.RightBracket) 
                self.state = 340
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PrimaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Literal(self):
            return self.getToken(MT22Parser.Literal, 0)

        def Identifier(self):
            return self.getToken(MT22Parser.Identifier, 0)

        def functionCall(self):
            return self.getTypedRuleContext(MT22Parser.FunctionCallContext,0)


        def LeftParen(self):
            return self.getToken(MT22Parser.LeftParen, 0)

        def expressions(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionsContext,0)


        def RightParen(self):
            return self.getToken(MT22Parser.RightParen, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_primaryExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpression" ):
                return visitor.visitPrimaryExpression(self)
            else:
                return visitor.visitChildren(self)




    def primaryExpression(self):

        localctx = MT22Parser.PrimaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_primaryExpression)
        try:
            self.state = 348
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 341
                self.match(MT22Parser.Literal)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 342
                self.match(MT22Parser.Identifier)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 343
                self.functionCall()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 344
                self.match(MT22Parser.LeftParen)
                self.state = 345
                self.expressions()
                self.state = 346
                self.match(MT22Parser.RightParen)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(MT22Parser.Identifier, 0)

        def LeftParen(self):
            return self.getToken(MT22Parser.LeftParen, 0)

        def RightParen(self):
            return self.getToken(MT22Parser.RightParen, 0)

        def expressions(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionsContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_functionCall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = MT22Parser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.match(MT22Parser.Identifier)
            self.state = 351
            self.match(MT22Parser.LeftParen)
            self.state = 353
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.Minus) | (1 << MT22Parser.Not) | (1 << MT22Parser.LeftParen) | (1 << MT22Parser.Identifier) | (1 << MT22Parser.Literal))) != 0):
                self.state = 352
                self.expressions()


            self.state = 355
            self.match(MT22Parser.RightParen)
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
        self._predicates[31] = self.logicalExpression_sempred
        self._predicates[32] = self.additiveExpression_sempred
        self._predicates[33] = self.multiplicativeExpression_sempred
        self._predicates[36] = self.postfixExpression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def logicalExpression_sempred(self, localctx:LogicalExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def additiveExpression_sempred(self, localctx:AdditiveExpressionContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def multiplicativeExpression_sempred(self, localctx:MultiplicativeExpressionContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def postfixExpression_sempred(self, localctx:PostfixExpressionContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




