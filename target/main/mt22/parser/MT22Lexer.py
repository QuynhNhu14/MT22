# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2=")
        buf.write("\u01e7\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\3\2\3\2\3\2\3\2")
        buf.write("\7\2\u0098\n\2\f\2\16\2\u009b\13\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\3\7\3\u00a6\n\3\f\3\16\3\u00a9\13\3\3\3")
        buf.write("\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\5\6\u00b6\n\6")
        buf.write("\3\6\7\6\u00b9\n\6\f\6\16\6\u00bc\13\6\5\6\u00be\n\6\3")
        buf.write("\7\3\7\5\7\u00c2\n\7\3\7\3\7\3\7\5\7\u00c7\n\7\3\b\3\b")
        buf.write("\3\b\7\b\u00cc\n\b\f\b\16\b\u00cf\13\b\3\t\3\t\5\t\u00d3")
        buf.write("\n\t\3\t\6\t\u00d6\n\t\r\t\16\t\u00d7\3\n\3\n\5\n\u00dc")
        buf.write("\n\n\3\13\3\13\3\13\3\f\3\f\5\f\u00e3\n\f\3\f\3\f\3\f")
        buf.write("\3\r\6\r\u00e9\n\r\r\r\16\r\u00ea\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\5\16\u00f4\n\16\3\17\3\17\5\17\u00f8\n")
        buf.write("\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3 \3!\3!\3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3")
        buf.write("#\3#\3$\3$\3$\3$\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3")
        buf.write(")\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3.\3/\3/\3\60")
        buf.write("\3\60\3\60\3\61\3\61\3\62\3\62\3\62\3\63\3\63\3\63\3\64")
        buf.write("\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:")
        buf.write("\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3@\7@\u01b5\n@\f")
        buf.write("@\16@\u01b8\13@\3A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3F\6F\u01c5")
        buf.write("\nF\rF\16F\u01c6\3F\3F\3G\3G\3G\3H\3H\7H\u01d0\nH\fH\16")
        buf.write("H\u01d3\13H\3H\5H\u01d6\nH\3H\5H\u01d9\nH\3H\3H\3I\3I")
        buf.write("\7I\u01df\nI\fI\16I\u01e2\13I\3I\3I\3I\3I\3\u0099\2J\3")
        buf.write("\3\5\4\7\5\t\6\13\2\r\2\17\2\21\2\23\2\25\2\27\7\31\2")
        buf.write("\33\2\35\b\37\t!\n#\13%\f\'\r)\16+\17-\20/\21\61\22\63")
        buf.write("\23\65\24\67\259\26;\27=\30?\31A\32C\33E\34G\35I\36K\37")
        buf.write("M O!Q\"S#U$W%Y&[\'](_)a*c+e,g-i.k/m\60o\61q\62s\63u\64")
        buf.write("w\65y\66{\67}8\1779\u0081\2\u0083\2\u0085\2\u0087\2\u0089")
        buf.write("\2\u008b:\u008d;\u008f<\u0091=\3\2\16\4\2\f\f\17\17\4")
        buf.write("\2GGgg\6\2\f\f\17\17))^^\n\2$$))^^ddhhppttvv\6\2\f\f\17")
        buf.write("\17$$^^\5\2C\\aac|\3\2\62;\3\2\63;\4\2--//\5\2\n\f\16")
        buf.write("\17\"\"\3\2$$\t\2$$^^ddhhppttvv\2\u01f1\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\27\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2")
        buf.write("\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2")
        buf.write("9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2")
        buf.write("\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2")
        buf.write("\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2")
        buf.write("\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3")
        buf.write("\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i")
        buf.write("\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2")
        buf.write("s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2")
        buf.write("\2}\3\2\2\2\2\177\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2")
        buf.write("\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\3\u0093\3\2\2\2\5")
        buf.write("\u00a1\3\2\2\2\7\u00ac\3\2\2\2\t\u00af\3\2\2\2\13\u00bd")
        buf.write("\3\2\2\2\r\u00c6\3\2\2\2\17\u00c8\3\2\2\2\21\u00d0\3\2")
        buf.write("\2\2\23\u00db\3\2\2\2\25\u00dd\3\2\2\2\27\u00e0\3\2\2")
        buf.write("\2\31\u00e8\3\2\2\2\33\u00f3\3\2\2\2\35\u00f7\3\2\2\2")
        buf.write("\37\u00f9\3\2\2\2!\u00fe\3\2\2\2#\u0104\3\2\2\2%\u010c")
        buf.write("\3\2\2\2\'\u0112\3\2\2\2)\u0115\3\2\2\2+\u011b\3\2\2\2")
        buf.write("-\u0121\3\2\2\2/\u0128\3\2\2\2\61\u012d\3\2\2\2\63\u0135")
        buf.write("\3\2\2\2\65\u013d\3\2\2\2\67\u0141\3\2\2\29\u0148\3\2")
        buf.write("\2\2;\u0151\3\2\2\2=\u0154\3\2\2\2?\u0159\3\2\2\2A\u015d")
        buf.write("\3\2\2\2C\u0162\3\2\2\2E\u0165\3\2\2\2G\u016e\3\2\2\2")
        buf.write("I\u0174\3\2\2\2K\u0176\3\2\2\2M\u0178\3\2\2\2O\u017a\3")
        buf.write("\2\2\2Q\u017c\3\2\2\2S\u017e\3\2\2\2U\u0180\3\2\2\2W\u0183")
        buf.write("\3\2\2\2Y\u0186\3\2\2\2[\u0189\3\2\2\2]\u018c\3\2\2\2")
        buf.write("_\u018e\3\2\2\2a\u0191\3\2\2\2c\u0193\3\2\2\2e\u0196\3")
        buf.write("\2\2\2g\u0199\3\2\2\2i\u019b\3\2\2\2k\u019d\3\2\2\2m\u019f")
        buf.write("\3\2\2\2o\u01a1\3\2\2\2q\u01a3\3\2\2\2s\u01a5\3\2\2\2")
        buf.write("u\u01a7\3\2\2\2w\u01a9\3\2\2\2y\u01ab\3\2\2\2{\u01ad\3")
        buf.write("\2\2\2}\u01af\3\2\2\2\177\u01b1\3\2\2\2\u0081\u01b9\3")
        buf.write("\2\2\2\u0083\u01bb\3\2\2\2\u0085\u01bd\3\2\2\2\u0087\u01bf")
        buf.write("\3\2\2\2\u0089\u01c1\3\2\2\2\u008b\u01c4\3\2\2\2\u008d")
        buf.write("\u01ca\3\2\2\2\u008f\u01cd\3\2\2\2\u0091\u01dc\3\2\2\2")
        buf.write("\u0093\u0094\7\61\2\2\u0094\u0095\7,\2\2\u0095\u0099\3")
        buf.write("\2\2\2\u0096\u0098\13\2\2\2\u0097\u0096\3\2\2\2\u0098")
        buf.write("\u009b\3\2\2\2\u0099\u009a\3\2\2\2\u0099\u0097\3\2\2\2")
        buf.write("\u009a\u009c\3\2\2\2\u009b\u0099\3\2\2\2\u009c\u009d\7")
        buf.write(",\2\2\u009d\u009e\7\61\2\2\u009e\u009f\3\2\2\2\u009f\u00a0")
        buf.write("\b\2\2\2\u00a0\4\3\2\2\2\u00a1\u00a2\7\61\2\2\u00a2\u00a3")
        buf.write("\7\61\2\2\u00a3\u00a7\3\2\2\2\u00a4\u00a6\n\2\2\2\u00a5")
        buf.write("\u00a4\3\2\2\2\u00a6\u00a9\3\2\2\2\u00a7\u00a5\3\2\2\2")
        buf.write("\u00a7\u00a8\3\2\2\2\u00a8\u00aa\3\2\2\2\u00a9\u00a7\3")
        buf.write("\2\2\2\u00aa\u00ab\b\3\2\2\u00ab\6\3\2\2\2\u00ac\u00ad")
        buf.write("\5\13\6\2\u00ad\u00ae\b\4\3\2\u00ae\b\3\2\2\2\u00af\u00b0")
        buf.write("\5\r\7\2\u00b0\u00b1\b\5\4\2\u00b1\n\3\2\2\2\u00b2\u00be")
        buf.write("\7\62\2\2\u00b3\u00ba\5\u0087D\2\u00b4\u00b6\5}?\2\u00b5")
        buf.write("\u00b4\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00b7\3\2\2\2")
        buf.write("\u00b7\u00b9\5\u0085C\2\u00b8\u00b5\3\2\2\2\u00b9\u00bc")
        buf.write("\3\2\2\2\u00ba\u00b8\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb")
        buf.write("\u00be\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bd\u00b2\3\2\2\2")
        buf.write("\u00bd\u00b3\3\2\2\2\u00be\f\3\2\2\2\u00bf\u00c1\5\17")
        buf.write("\b\2\u00c0\u00c2\5\21\t\2\u00c1\u00c0\3\2\2\2\u00c1\u00c2")
        buf.write("\3\2\2\2\u00c2\u00c7\3\2\2\2\u00c3\u00c4\5\13\6\2\u00c4")
        buf.write("\u00c5\5\21\t\2\u00c5\u00c7\3\2\2\2\u00c6\u00bf\3\2\2")
        buf.write("\2\u00c6\u00c3\3\2\2\2\u00c7\16\3\2\2\2\u00c8\u00c9\5")
        buf.write("\13\6\2\u00c9\u00cd\7\60\2\2\u00ca\u00cc\5\u0085C\2\u00cb")
        buf.write("\u00ca\3\2\2\2\u00cc\u00cf\3\2\2\2\u00cd\u00cb\3\2\2\2")
        buf.write("\u00cd\u00ce\3\2\2\2\u00ce\20\3\2\2\2\u00cf\u00cd\3\2")
        buf.write("\2\2\u00d0\u00d2\t\3\2\2\u00d1\u00d3\5\u0089E\2\u00d2")
        buf.write("\u00d1\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d5\3\2\2\2")
        buf.write("\u00d4\u00d6\5\u0085C\2\u00d5\u00d4\3\2\2\2\u00d6\u00d7")
        buf.write("\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8")
        buf.write("\22\3\2\2\2\u00d9\u00dc\n\4\2\2\u00da\u00dc\5\25\13\2")
        buf.write("\u00db\u00d9\3\2\2\2\u00db\u00da\3\2\2\2\u00dc\24\3\2")
        buf.write("\2\2\u00dd\u00de\7^\2\2\u00de\u00df\t\5\2\2\u00df\26\3")
        buf.write("\2\2\2\u00e0\u00e2\7$\2\2\u00e1\u00e3\5\31\r\2\u00e2\u00e1")
        buf.write("\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4")
        buf.write("\u00e5\7$\2\2\u00e5\u00e6\b\f\5\2\u00e6\30\3\2\2\2\u00e7")
        buf.write("\u00e9\5\33\16\2\u00e8\u00e7\3\2\2\2\u00e9\u00ea\3\2\2")
        buf.write("\2\u00ea\u00e8\3\2\2\2\u00ea\u00eb\3\2\2\2\u00eb\32\3")
        buf.write("\2\2\2\u00ec\u00f4\n\6\2\2\u00ed\u00f4\5\25\13\2\u00ee")
        buf.write("\u00ef\7^\2\2\u00ef\u00f4\7\f\2\2\u00f0\u00f1\7^\2\2\u00f1")
        buf.write("\u00f2\7\17\2\2\u00f2\u00f4\7\f\2\2\u00f3\u00ec\3\2\2")
        buf.write("\2\u00f3\u00ed\3\2\2\2\u00f3\u00ee\3\2\2\2\u00f3\u00f0")
        buf.write("\3\2\2\2\u00f4\34\3\2\2\2\u00f5\u00f8\5=\37\2\u00f6\u00f8")
        buf.write("\5!\21\2\u00f7\u00f5\3\2\2\2\u00f7\u00f6\3\2\2\2\u00f8")
        buf.write("\36\3\2\2\2\u00f9\u00fa\7c\2\2\u00fa\u00fb\7w\2\2\u00fb")
        buf.write("\u00fc\7v\2\2\u00fc\u00fd\7q\2\2\u00fd \3\2\2\2\u00fe")
        buf.write("\u00ff\7h\2\2\u00ff\u0100\7c\2\2\u0100\u0101\7n\2\2\u0101")
        buf.write("\u0102\7u\2\2\u0102\u0103\7g\2\2\u0103\"\3\2\2\2\u0104")
        buf.write("\u0105\7k\2\2\u0105\u0106\7p\2\2\u0106\u0107\7v\2\2\u0107")
        buf.write("\u0108\7g\2\2\u0108\u0109\7i\2\2\u0109\u010a\7g\2\2\u010a")
        buf.write("\u010b\7t\2\2\u010b$\3\2\2\2\u010c\u010d\7y\2\2\u010d")
        buf.write("\u010e\7j\2\2\u010e\u010f\7k\2\2\u010f\u0110\7n\2\2\u0110")
        buf.write("\u0111\7g\2\2\u0111&\3\2\2\2\u0112\u0113\7q\2\2\u0113")
        buf.write("\u0114\7h\2\2\u0114(\3\2\2\2\u0115\u0116\7d\2\2\u0116")
        buf.write("\u0117\7t\2\2\u0117\u0118\7g\2\2\u0118\u0119\7c\2\2\u0119")
        buf.write("\u011a\7m\2\2\u011a*\3\2\2\2\u011b\u011c\7h\2\2\u011c")
        buf.write("\u011d\7n\2\2\u011d\u011e\7q\2\2\u011e\u011f\7c\2\2\u011f")
        buf.write("\u0120\7v\2\2\u0120,\3\2\2\2\u0121\u0122\7t\2\2\u0122")
        buf.write("\u0123\7g\2\2\u0123\u0124\7v\2\2\u0124\u0125\7w\2\2\u0125")
        buf.write("\u0126\7t\2\2\u0126\u0127\7p\2\2\u0127.\3\2\2\2\u0128")
        buf.write("\u0129\7x\2\2\u0129\u012a\7q\2\2\u012a\u012b\7k\2\2\u012b")
        buf.write("\u012c\7f\2\2\u012c\60\3\2\2\2\u012d\u012e\7k\2\2\u012e")
        buf.write("\u012f\7p\2\2\u012f\u0130\7j\2\2\u0130\u0131\7g\2\2\u0131")
        buf.write("\u0132\7t\2\2\u0132\u0133\7k\2\2\u0133\u0134\7v\2\2\u0134")
        buf.write("\62\3\2\2\2\u0135\u0136\7d\2\2\u0136\u0137\7q\2\2\u0137")
        buf.write("\u0138\7q\2\2\u0138\u0139\7n\2\2\u0139\u013a\7g\2\2\u013a")
        buf.write("\u013b\7c\2\2\u013b\u013c\7p\2\2\u013c\64\3\2\2\2\u013d")
        buf.write("\u013e\7h\2\2\u013e\u013f\7q\2\2\u013f\u0140\7t\2\2\u0140")
        buf.write("\66\3\2\2\2\u0141\u0142\7u\2\2\u0142\u0143\7v\2\2\u0143")
        buf.write("\u0144\7t\2\2\u0144\u0145\7k\2\2\u0145\u0146\7p\2\2\u0146")
        buf.write("\u0147\7i\2\2\u01478\3\2\2\2\u0148\u0149\7h\2\2\u0149")
        buf.write("\u014a\7w\2\2\u014a\u014b\7p\2\2\u014b\u014c\7e\2\2\u014c")
        buf.write("\u014d\7v\2\2\u014d\u014e\7k\2\2\u014e\u014f\7q\2\2\u014f")
        buf.write("\u0150\7p\2\2\u0150:\3\2\2\2\u0151\u0152\7f\2\2\u0152")
        buf.write("\u0153\7q\2\2\u0153<\3\2\2\2\u0154\u0155\7v\2\2\u0155")
        buf.write("\u0156\7t\2\2\u0156\u0157\7w\2\2\u0157\u0158\7g\2\2\u0158")
        buf.write(">\3\2\2\2\u0159\u015a\7q\2\2\u015a\u015b\7w\2\2\u015b")
        buf.write("\u015c\7v\2\2\u015c@\3\2\2\2\u015d\u015e\7g\2\2\u015e")
        buf.write("\u015f\7n\2\2\u015f\u0160\7u\2\2\u0160\u0161\7g\2\2\u0161")
        buf.write("B\3\2\2\2\u0162\u0163\7k\2\2\u0163\u0164\7h\2\2\u0164")
        buf.write("D\3\2\2\2\u0165\u0166\7e\2\2\u0166\u0167\7q\2\2\u0167")
        buf.write("\u0168\7p\2\2\u0168\u0169\7v\2\2\u0169\u016a\7k\2\2\u016a")
        buf.write("\u016b\7p\2\2\u016b\u016c\7w\2\2\u016c\u016d\7g\2\2\u016d")
        buf.write("F\3\2\2\2\u016e\u016f\7c\2\2\u016f\u0170\7t\2\2\u0170")
        buf.write("\u0171\7t\2\2\u0171\u0172\7c\2\2\u0172\u0173\7{\2\2\u0173")
        buf.write("H\3\2\2\2\u0174\u0175\7-\2\2\u0175J\3\2\2\2\u0176\u0177")
        buf.write("\7/\2\2\u0177L\3\2\2\2\u0178\u0179\7,\2\2\u0179N\3\2\2")
        buf.write("\2\u017a\u017b\7\61\2\2\u017bP\3\2\2\2\u017c\u017d\7\'")
        buf.write("\2\2\u017dR\3\2\2\2\u017e\u017f\7#\2\2\u017fT\3\2\2\2")
        buf.write("\u0180\u0181\7(\2\2\u0181\u0182\7(\2\2\u0182V\3\2\2\2")
        buf.write("\u0183\u0184\7~\2\2\u0184\u0185\7~\2\2\u0185X\3\2\2\2")
        buf.write("\u0186\u0187\7?\2\2\u0187\u0188\7?\2\2\u0188Z\3\2\2\2")
        buf.write("\u0189\u018a\7#\2\2\u018a\u018b\7?\2\2\u018b\\\3\2\2\2")
        buf.write("\u018c\u018d\7>\2\2\u018d^\3\2\2\2\u018e\u018f\7>\2\2")
        buf.write("\u018f\u0190\7?\2\2\u0190`\3\2\2\2\u0191\u0192\7@\2\2")
        buf.write("\u0192b\3\2\2\2\u0193\u0194\7@\2\2\u0194\u0195\7?\2\2")
        buf.write("\u0195d\3\2\2\2\u0196\u0197\7<\2\2\u0197\u0198\7<\2\2")
        buf.write("\u0198f\3\2\2\2\u0199\u019a\7*\2\2\u019ah\3\2\2\2\u019b")
        buf.write("\u019c\7+\2\2\u019cj\3\2\2\2\u019d\u019e\7]\2\2\u019e")
        buf.write("l\3\2\2\2\u019f\u01a0\7_\2\2\u01a0n\3\2\2\2\u01a1\u01a2")
        buf.write("\7}\2\2\u01a2p\3\2\2\2\u01a3\u01a4\7\177\2\2\u01a4r\3")
        buf.write("\2\2\2\u01a5\u01a6\7\60\2\2\u01a6t\3\2\2\2\u01a7\u01a8")
        buf.write("\7.\2\2\u01a8v\3\2\2\2\u01a9\u01aa\7=\2\2\u01aax\3\2\2")
        buf.write("\2\u01ab\u01ac\7<\2\2\u01acz\3\2\2\2\u01ad\u01ae\7?\2")
        buf.write("\2\u01ae|\3\2\2\2\u01af\u01b0\7a\2\2\u01b0~\3\2\2\2\u01b1")
        buf.write("\u01b6\5\u0081A\2\u01b2\u01b5\5\u0081A\2\u01b3\u01b5\5")
        buf.write("\u0085C\2\u01b4\u01b2\3\2\2\2\u01b4\u01b3\3\2\2\2\u01b5")
        buf.write("\u01b8\3\2\2\2\u01b6\u01b4\3\2\2\2\u01b6\u01b7\3\2\2\2")
        buf.write("\u01b7\u0080\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b9\u01ba\5")
        buf.write("\u0083B\2\u01ba\u0082\3\2\2\2\u01bb\u01bc\t\7\2\2\u01bc")
        buf.write("\u0084\3\2\2\2\u01bd\u01be\t\b\2\2\u01be\u0086\3\2\2\2")
        buf.write("\u01bf\u01c0\t\t\2\2\u01c0\u0088\3\2\2\2\u01c1\u01c2\t")
        buf.write("\n\2\2\u01c2\u008a\3\2\2\2\u01c3\u01c5\t\13\2\2\u01c4")
        buf.write("\u01c3\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6\u01c4\3\2\2\2")
        buf.write("\u01c6\u01c7\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8\u01c9\b")
        buf.write("F\2\2\u01c9\u008c\3\2\2\2\u01ca\u01cb\13\2\2\2\u01cb\u01cc")
        buf.write("\bG\6\2\u01cc\u008e\3\2\2\2\u01cd\u01d1\7$\2\2\u01ce\u01d0")
        buf.write("\5\33\16\2\u01cf\u01ce\3\2\2\2\u01d0\u01d3\3\2\2\2\u01d1")
        buf.write("\u01cf\3\2\2\2\u01d1\u01d2\3\2\2\2\u01d2\u01d8\3\2\2\2")
        buf.write("\u01d3\u01d1\3\2\2\2\u01d4\u01d6\7\2\2\3\u01d5\u01d4\3")
        buf.write("\2\2\2\u01d5\u01d6\3\2\2\2\u01d6\u01d9\3\2\2\2\u01d7\u01d9")
        buf.write("\n\f\2\2\u01d8\u01d5\3\2\2\2\u01d8\u01d7\3\2\2\2\u01d9")
        buf.write("\u01da\3\2\2\2\u01da\u01db\bH\7\2\u01db\u0090\3\2\2\2")
        buf.write("\u01dc\u01e0\7$\2\2\u01dd\u01df\5\33\16\2\u01de\u01dd")
        buf.write("\3\2\2\2\u01df\u01e2\3\2\2\2\u01e0\u01de\3\2\2\2\u01e0")
        buf.write("\u01e1\3\2\2\2\u01e1\u01e3\3\2\2\2\u01e2\u01e0\3\2\2\2")
        buf.write("\u01e3\u01e4\7^\2\2\u01e4\u01e5\n\r\2\2\u01e5\u01e6\b")
        buf.write("I\b\2\u01e6\u0092\3\2\2\2\31\2\u0099\u00a7\u00b5\u00ba")
        buf.write("\u00bd\u00c1\u00c6\u00cd\u00d2\u00d7\u00db\u00e2\u00ea")
        buf.write("\u00f3\u00f7\u01b4\u01b6\u01c6\u01d1\u01d5\u01d8\u01e0")
        buf.write("\t\b\2\2\3\4\2\3\5\3\3\f\4\3G\5\3H\6\3I\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BlockComment = 1
    LineComment = 2
    IntegerConstant = 3
    FloatingConstant = 4
    StringConstant = 5
    BooleanConstant = 6
    Auto = 7
    False_ = 8
    Integer = 9
    While = 10
    Of = 11
    Break = 12
    Float = 13
    Return = 14
    Void = 15
    Inherit = 16
    Boolean_ = 17
    For = 18
    String = 19
    Function = 20
    Do = 21
    True_ = 22
    Out = 23
    Else = 24
    If = 25
    Continue = 26
    Array = 27
    Plus = 28
    Minus = 29
    Star = 30
    Div = 31
    Mod = 32
    Not = 33
    AndAnd = 34
    OrOr = 35
    Equal = 36
    NotEqual = 37
    Less = 38
    LessEqual = 39
    Greater = 40
    GreaterEqual = 41
    ColonColon = 42
    LeftParen = 43
    RightParen = 44
    LeftBracket = 45
    RightBracket = 46
    LeftBrace = 47
    RightBrace = 48
    Dot = 49
    Comma = 50
    Semi = 51
    Colon = 52
    Assign = 53
    Under = 54
    Identifier = 55
    WS = 56
    ERROR_CHAR = 57
    UNCLOSE_STRING = 58
    ILLEGAL_ESCAPE = 59

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'false'", "'integer'", "'while'", "'of'", "'break'", 
            "'float'", "'return'", "'void'", "'inherit'", "'boolean'", "'for'", 
            "'string'", "'function'", "'do'", "'true'", "'out'", "'else'", 
            "'if'", "'continue'", "'array'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", "'<='", 
            "'>'", "'>='", "'::'", "'('", "')'", "'['", "']'", "'{'", "'}'", 
            "'.'", "','", "';'", "':'", "'='", "'_'" ]

    symbolicNames = [ "<INVALID>",
            "BlockComment", "LineComment", "IntegerConstant", "FloatingConstant", 
            "StringConstant", "BooleanConstant", "Auto", "False_", "Integer", 
            "While", "Of", "Break", "Float", "Return", "Void", "Inherit", 
            "Boolean_", "For", "String", "Function", "Do", "True_", "Out", 
            "Else", "If", "Continue", "Array", "Plus", "Minus", "Star", 
            "Div", "Mod", "Not", "AndAnd", "OrOr", "Equal", "NotEqual", 
            "Less", "LessEqual", "Greater", "GreaterEqual", "ColonColon", 
            "LeftParen", "RightParen", "LeftBracket", "RightBracket", "LeftBrace", 
            "RightBrace", "Dot", "Comma", "Semi", "Colon", "Assign", "Under", 
            "Identifier", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "BlockComment", "LineComment", "IntegerConstant", "FloatingConstant", 
                  "DecimalConstant", "DecimalFloatingConstant", "FractionalConstant", 
                  "ExponentPart", "CChar", "EscapeSequence", "StringConstant", 
                  "SCharSequence", "SChar", "BooleanConstant", "Auto", "False_", 
                  "Integer", "While", "Of", "Break", "Float", "Return", 
                  "Void", "Inherit", "Boolean_", "For", "String", "Function", 
                  "Do", "True_", "Out", "Else", "If", "Continue", "Array", 
                  "Plus", "Minus", "Star", "Div", "Mod", "Not", "AndAnd", 
                  "OrOr", "Equal", "NotEqual", "Less", "LessEqual", "Greater", 
                  "GreaterEqual", "ColonColon", "LeftParen", "RightParen", 
                  "LeftBracket", "RightBracket", "LeftBrace", "RightBrace", 
                  "Dot", "Comma", "Semi", "Colon", "Assign", "Under", "Identifier", 
                  "IdentifierNondigit", "Nondigit", "Digit", "NonzeroDigit", 
                  "Sign", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[2] = self.IntegerConstant_action 
            actions[3] = self.FloatingConstant_action 
            actions[10] = self.StringConstant_action 
            actions[69] = self.ERROR_CHAR_action 
            actions[70] = self.UNCLOSE_STRING_action 
            actions[71] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def IntegerConstant_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text=self.text.replace("_","")
     

    def FloatingConstant_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text=self.text.replace("_","")
     

    def StringConstant_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text=self.text[1:-1]
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            	if self.text[-1] in ['\r','\n']:
            		raise UncloseString(self.text[1:-1])
            	else: raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

            	raise IllegalEscape(self.text[1:])

     


