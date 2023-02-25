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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2?")
        buf.write("\u01f2\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\3\2\3\2\3\2\3\2\7\2\u009e\n\2\f\2\16\2\u00a1\13\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\7\3\u00ac\n\3\f\3\16")
        buf.write("\3\u00af\13\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\32")
        buf.write("\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3$\3$\3$\3%")
        buf.write("\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3")
        buf.write(",\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63")
        buf.write("\3\63\3\64\3\64\3\64\7\64\u016e\n\64\f\64\16\64\u0171")
        buf.write("\13\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\38\38\78\u017d")
        buf.write("\n8\f8\168\u0180\138\38\58\u0183\n8\38\38\39\39\3:\3:")
        buf.write("\7:\u018b\n:\f:\16:\u018e\13:\3;\3;\3<\3<\3=\3=\5=\u0196")
        buf.write("\n=\3=\3=\3=\5=\u019b\n=\3>\5>\u019e\n>\3>\3>\3>\7>\u01a3")
        buf.write("\n>\f>\16>\u01a6\13>\3>\3>\3>\3>\3>\3>\7>\u01ae\n>\f>")
        buf.write("\16>\u01b1\13>\3>\3>\5>\u01b5\n>\3?\3?\5?\u01b9\n?\3?")
        buf.write("\3?\3@\3@\3A\6A\u01c0\nA\rA\16A\u01c1\3B\3B\5B\u01c6\n")
        buf.write("B\3C\3C\3D\3D\3D\3E\3E\5E\u01cf\nE\3E\3E\3F\6F\u01d4\n")
        buf.write("F\rF\16F\u01d5\3G\3G\3G\3G\3G\3G\3G\5G\u01df\nG\3H\3H")
        buf.write("\5H\u01e3\nH\3I\6I\u01e6\nI\rI\16I\u01e7\3I\3I\3J\3J\3")
        buf.write("J\3K\3K\3L\3L\3\u009f\2M\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63")
        buf.write("e\64g\65i\2k\2m\2o\66q\67s\2u\2w8y\2{\2}\2\177\2\u0081")
        buf.write("9\u0083\2\u0085\2\u0087\2\u0089:\u008b\2\u008d\2\u008f")
        buf.write(";\u0091<\u0093=\u0095>\u0097?\3\2\f\4\2\f\f\17\17\5\2")
        buf.write("C\\aac|\3\2\62;\3\2\63;\4\2GGgg\4\2--//\6\2\f\f\17\17")
        buf.write("))^^\f\2$$))AA^^cdhhppttvvxx\6\2\f\f\17\17$$^^\5\2\n\f")
        buf.write("\16\17\"\"\2\u01fa\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2")
        buf.write("\2e\3\2\2\2\2g\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2w\3\2\2")
        buf.write("\2\2\u0081\3\2\2\2\2\u0089\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2")
        buf.write("\2\3\u0099\3\2\2\2\5\u00a7\3\2\2\2\7\u00b2\3\2\2\2\t\u00b7")
        buf.write("\3\2\2\2\13\u00bd\3\2\2\2\r\u00c5\3\2\2\2\17\u00cb\3\2")
        buf.write("\2\2\21\u00ce\3\2\2\2\23\u00d4\3\2\2\2\25\u00da\3\2\2")
        buf.write("\2\27\u00e1\3\2\2\2\31\u00e6\3\2\2\2\33\u00ee\3\2\2\2")
        buf.write("\35\u00f6\3\2\2\2\37\u00fa\3\2\2\2!\u0101\3\2\2\2#\u010a")
        buf.write("\3\2\2\2%\u010d\3\2\2\2\'\u0112\3\2\2\2)\u0116\3\2\2\2")
        buf.write("+\u011b\3\2\2\2-\u011e\3\2\2\2/\u0127\3\2\2\2\61\u012d")
        buf.write("\3\2\2\2\63\u012f\3\2\2\2\65\u0131\3\2\2\2\67\u0133\3")
        buf.write("\2\2\29\u0135\3\2\2\2;\u0137\3\2\2\2=\u0139\3\2\2\2?\u013c")
        buf.write("\3\2\2\2A\u013f\3\2\2\2C\u0142\3\2\2\2E\u0145\3\2\2\2")
        buf.write("G\u0147\3\2\2\2I\u014a\3\2\2\2K\u014c\3\2\2\2M\u014f\3")
        buf.write("\2\2\2O\u0152\3\2\2\2Q\u0154\3\2\2\2S\u0156\3\2\2\2U\u0158")
        buf.write("\3\2\2\2W\u015a\3\2\2\2Y\u015c\3\2\2\2[\u015e\3\2\2\2")
        buf.write("]\u0160\3\2\2\2_\u0162\3\2\2\2a\u0164\3\2\2\2c\u0166\3")
        buf.write("\2\2\2e\u0168\3\2\2\2g\u016a\3\2\2\2i\u0172\3\2\2\2k\u0174")
        buf.write("\3\2\2\2m\u0176\3\2\2\2o\u0182\3\2\2\2q\u0186\3\2\2\2")
        buf.write("s\u0188\3\2\2\2u\u018f\3\2\2\2w\u0191\3\2\2\2y\u019a\3")
        buf.write("\2\2\2{\u01b4\3\2\2\2}\u01b6\3\2\2\2\177\u01bc\3\2\2\2")
        buf.write("\u0081\u01bf\3\2\2\2\u0083\u01c5\3\2\2\2\u0085\u01c7\3")
        buf.write("\2\2\2\u0087\u01c9\3\2\2\2\u0089\u01cc\3\2\2\2\u008b\u01d3")
        buf.write("\3\2\2\2\u008d\u01de\3\2\2\2\u008f\u01e2\3\2\2\2\u0091")
        buf.write("\u01e5\3\2\2\2\u0093\u01eb\3\2\2\2\u0095\u01ee\3\2\2\2")
        buf.write("\u0097\u01f0\3\2\2\2\u0099\u009a\7\61\2\2\u009a\u009b")
        buf.write("\7,\2\2\u009b\u009f\3\2\2\2\u009c\u009e\13\2\2\2\u009d")
        buf.write("\u009c\3\2\2\2\u009e\u00a1\3\2\2\2\u009f\u00a0\3\2\2\2")
        buf.write("\u009f\u009d\3\2\2\2\u00a0\u00a2\3\2\2\2\u00a1\u009f\3")
        buf.write("\2\2\2\u00a2\u00a3\7,\2\2\u00a3\u00a4\7\61\2\2\u00a4\u00a5")
        buf.write("\3\2\2\2\u00a5\u00a6\b\2\2\2\u00a6\4\3\2\2\2\u00a7\u00a8")
        buf.write("\7\61\2\2\u00a8\u00a9\7\61\2\2\u00a9\u00ad\3\2\2\2\u00aa")
        buf.write("\u00ac\n\2\2\2\u00ab\u00aa\3\2\2\2\u00ac\u00af\3\2\2\2")
        buf.write("\u00ad\u00ab\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00b0\3")
        buf.write("\2\2\2\u00af\u00ad\3\2\2\2\u00b0\u00b1\b\3\2\2\u00b1\6")
        buf.write("\3\2\2\2\u00b2\u00b3\7c\2\2\u00b3\u00b4\7w\2\2\u00b4\u00b5")
        buf.write("\7v\2\2\u00b5\u00b6\7q\2\2\u00b6\b\3\2\2\2\u00b7\u00b8")
        buf.write("\7h\2\2\u00b8\u00b9\7c\2\2\u00b9\u00ba\7n\2\2\u00ba\u00bb")
        buf.write("\7u\2\2\u00bb\u00bc\7g\2\2\u00bc\n\3\2\2\2\u00bd\u00be")
        buf.write("\7k\2\2\u00be\u00bf\7p\2\2\u00bf\u00c0\7v\2\2\u00c0\u00c1")
        buf.write("\7g\2\2\u00c1\u00c2\7i\2\2\u00c2\u00c3\7g\2\2\u00c3\u00c4")
        buf.write("\7t\2\2\u00c4\f\3\2\2\2\u00c5\u00c6\7y\2\2\u00c6\u00c7")
        buf.write("\7j\2\2\u00c7\u00c8\7k\2\2\u00c8\u00c9\7n\2\2\u00c9\u00ca")
        buf.write("\7g\2\2\u00ca\16\3\2\2\2\u00cb\u00cc\7q\2\2\u00cc\u00cd")
        buf.write("\7h\2\2\u00cd\20\3\2\2\2\u00ce\u00cf\7d\2\2\u00cf\u00d0")
        buf.write("\7t\2\2\u00d0\u00d1\7g\2\2\u00d1\u00d2\7c\2\2\u00d2\u00d3")
        buf.write("\7m\2\2\u00d3\22\3\2\2\2\u00d4\u00d5\7h\2\2\u00d5\u00d6")
        buf.write("\7n\2\2\u00d6\u00d7\7q\2\2\u00d7\u00d8\7c\2\2\u00d8\u00d9")
        buf.write("\7v\2\2\u00d9\24\3\2\2\2\u00da\u00db\7t\2\2\u00db\u00dc")
        buf.write("\7g\2\2\u00dc\u00dd\7v\2\2\u00dd\u00de\7w\2\2\u00de\u00df")
        buf.write("\7t\2\2\u00df\u00e0\7p\2\2\u00e0\26\3\2\2\2\u00e1\u00e2")
        buf.write("\7x\2\2\u00e2\u00e3\7q\2\2\u00e3\u00e4\7k\2\2\u00e4\u00e5")
        buf.write("\7f\2\2\u00e5\30\3\2\2\2\u00e6\u00e7\7k\2\2\u00e7\u00e8")
        buf.write("\7p\2\2\u00e8\u00e9\7j\2\2\u00e9\u00ea\7g\2\2\u00ea\u00eb")
        buf.write("\7t\2\2\u00eb\u00ec\7k\2\2\u00ec\u00ed\7v\2\2\u00ed\32")
        buf.write("\3\2\2\2\u00ee\u00ef\7d\2\2\u00ef\u00f0\7q\2\2\u00f0\u00f1")
        buf.write("\7q\2\2\u00f1\u00f2\7n\2\2\u00f2\u00f3\7g\2\2\u00f3\u00f4")
        buf.write("\7c\2\2\u00f4\u00f5\7p\2\2\u00f5\34\3\2\2\2\u00f6\u00f7")
        buf.write("\7h\2\2\u00f7\u00f8\7q\2\2\u00f8\u00f9\7t\2\2\u00f9\36")
        buf.write("\3\2\2\2\u00fa\u00fb\7u\2\2\u00fb\u00fc\7v\2\2\u00fc\u00fd")
        buf.write("\7t\2\2\u00fd\u00fe\7k\2\2\u00fe\u00ff\7p\2\2\u00ff\u0100")
        buf.write("\7i\2\2\u0100 \3\2\2\2\u0101\u0102\7h\2\2\u0102\u0103")
        buf.write("\7w\2\2\u0103\u0104\7p\2\2\u0104\u0105\7e\2\2\u0105\u0106")
        buf.write("\7v\2\2\u0106\u0107\7k\2\2\u0107\u0108\7q\2\2\u0108\u0109")
        buf.write("\7p\2\2\u0109\"\3\2\2\2\u010a\u010b\7f\2\2\u010b\u010c")
        buf.write("\7q\2\2\u010c$\3\2\2\2\u010d\u010e\7v\2\2\u010e\u010f")
        buf.write("\7t\2\2\u010f\u0110\7w\2\2\u0110\u0111\7g\2\2\u0111&\3")
        buf.write("\2\2\2\u0112\u0113\7q\2\2\u0113\u0114\7w\2\2\u0114\u0115")
        buf.write("\7v\2\2\u0115(\3\2\2\2\u0116\u0117\7g\2\2\u0117\u0118")
        buf.write("\7n\2\2\u0118\u0119\7u\2\2\u0119\u011a\7g\2\2\u011a*\3")
        buf.write("\2\2\2\u011b\u011c\7k\2\2\u011c\u011d\7h\2\2\u011d,\3")
        buf.write("\2\2\2\u011e\u011f\7e\2\2\u011f\u0120\7q\2\2\u0120\u0121")
        buf.write("\7p\2\2\u0121\u0122\7v\2\2\u0122\u0123\7k\2\2\u0123\u0124")
        buf.write("\7p\2\2\u0124\u0125\7w\2\2\u0125\u0126\7g\2\2\u0126.\3")
        buf.write("\2\2\2\u0127\u0128\7c\2\2\u0128\u0129\7t\2\2\u0129\u012a")
        buf.write("\7t\2\2\u012a\u012b\7c\2\2\u012b\u012c\7{\2\2\u012c\60")
        buf.write("\3\2\2\2\u012d\u012e\7-\2\2\u012e\62\3\2\2\2\u012f\u0130")
        buf.write("\7/\2\2\u0130\64\3\2\2\2\u0131\u0132\7,\2\2\u0132\66\3")
        buf.write("\2\2\2\u0133\u0134\7\61\2\2\u01348\3\2\2\2\u0135\u0136")
        buf.write("\7\'\2\2\u0136:\3\2\2\2\u0137\u0138\7#\2\2\u0138<\3\2")
        buf.write("\2\2\u0139\u013a\7(\2\2\u013a\u013b\7(\2\2\u013b>\3\2")
        buf.write("\2\2\u013c\u013d\7~\2\2\u013d\u013e\7~\2\2\u013e@\3\2")
        buf.write("\2\2\u013f\u0140\7?\2\2\u0140\u0141\7?\2\2\u0141B\3\2")
        buf.write("\2\2\u0142\u0143\7#\2\2\u0143\u0144\7?\2\2\u0144D\3\2")
        buf.write("\2\2\u0145\u0146\7>\2\2\u0146F\3\2\2\2\u0147\u0148\7>")
        buf.write("\2\2\u0148\u0149\7?\2\2\u0149H\3\2\2\2\u014a\u014b\7@")
        buf.write("\2\2\u014bJ\3\2\2\2\u014c\u014d\7@\2\2\u014d\u014e\7?")
        buf.write("\2\2\u014eL\3\2\2\2\u014f\u0150\7<\2\2\u0150\u0151\7<")
        buf.write("\2\2\u0151N\3\2\2\2\u0152\u0153\7*\2\2\u0153P\3\2\2\2")
        buf.write("\u0154\u0155\7+\2\2\u0155R\3\2\2\2\u0156\u0157\7]\2\2")
        buf.write("\u0157T\3\2\2\2\u0158\u0159\7_\2\2\u0159V\3\2\2\2\u015a")
        buf.write("\u015b\7}\2\2\u015bX\3\2\2\2\u015c\u015d\7\177\2\2\u015d")
        buf.write("Z\3\2\2\2\u015e\u015f\7\60\2\2\u015f\\\3\2\2\2\u0160\u0161")
        buf.write("\7.\2\2\u0161^\3\2\2\2\u0162\u0163\7=\2\2\u0163`\3\2\2")
        buf.write("\2\u0164\u0165\7<\2\2\u0165b\3\2\2\2\u0166\u0167\7?\2")
        buf.write("\2\u0167d\3\2\2\2\u0168\u0169\7a\2\2\u0169f\3\2\2\2\u016a")
        buf.write("\u016f\5i\65\2\u016b\u016e\5i\65\2\u016c\u016e\5m\67\2")
        buf.write("\u016d\u016b\3\2\2\2\u016d\u016c\3\2\2\2\u016e\u0171\3")
        buf.write("\2\2\2\u016f\u016d\3\2\2\2\u016f\u0170\3\2\2\2\u0170h")
        buf.write("\3\2\2\2\u0171\u016f\3\2\2\2\u0172\u0173\5k\66\2\u0173")
        buf.write("j\3\2\2\2\u0174\u0175\t\3\2\2\u0175l\3\2\2\2\u0176\u0177")
        buf.write("\t\4\2\2\u0177n\3\2\2\2\u0178\u017e\5q9\2\u0179\u017a")
        buf.write("\5e\63\2\u017a\u017b\5q9\2\u017b\u017d\3\2\2\2\u017c\u0179")
        buf.write("\3\2\2\2\u017d\u0180\3\2\2\2\u017e\u017c\3\2\2\2\u017e")
        buf.write("\u017f\3\2\2\2\u017f\u0183\3\2\2\2\u0180\u017e\3\2\2\2")
        buf.write("\u0181\u0183\5w<\2\u0182\u0178\3\2\2\2\u0182\u0181\3\2")
        buf.write("\2\2\u0183\u0184\3\2\2\2\u0184\u0185\b8\3\2\u0185p\3\2")
        buf.write("\2\2\u0186\u0187\5s:\2\u0187r\3\2\2\2\u0188\u018c\5u;")
        buf.write("\2\u0189\u018b\5m\67\2\u018a\u0189\3\2\2\2\u018b\u018e")
        buf.write("\3\2\2\2\u018c\u018a\3\2\2\2\u018c\u018d\3\2\2\2\u018d")
        buf.write("t\3\2\2\2\u018e\u018c\3\2\2\2\u018f\u0190\t\5\2\2\u0190")
        buf.write("v\3\2\2\2\u0191\u0192\5y=\2\u0192x\3\2\2\2\u0193\u0195")
        buf.write("\5{>\2\u0194\u0196\5}?\2\u0195\u0194\3\2\2\2\u0195\u0196")
        buf.write("\3\2\2\2\u0196\u019b\3\2\2\2\u0197\u0198\5\u0081A\2\u0198")
        buf.write("\u0199\5}?\2\u0199\u019b\3\2\2\2\u019a\u0193\3\2\2\2\u019a")
        buf.write("\u0197\3\2\2\2\u019bz\3\2\2\2\u019c\u019e\5\u0081A\2\u019d")
        buf.write("\u019c\3\2\2\2\u019d\u019e\3\2\2\2\u019e\u01a4\3\2\2\2")
        buf.write("\u019f\u01a0\5e\63\2\u01a0\u01a1\5\u0081A\2\u01a1\u01a3")
        buf.write("\3\2\2\2\u01a2\u019f\3\2\2\2\u01a3\u01a6\3\2\2\2\u01a4")
        buf.write("\u01a2\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5\u01a7\3\2\2\2")
        buf.write("\u01a6\u01a4\3\2\2\2\u01a7\u01a8\7\60\2\2\u01a8\u01b5")
        buf.write("\5\u0081A\2\u01a9\u01af\5\u0081A\2\u01aa\u01ab\5e\63\2")
        buf.write("\u01ab\u01ac\5\u0081A\2\u01ac\u01ae\3\2\2\2\u01ad\u01aa")
        buf.write("\3\2\2\2\u01ae\u01b1\3\2\2\2\u01af\u01ad\3\2\2\2\u01af")
        buf.write("\u01b0\3\2\2\2\u01b0\u01b2\3\2\2\2\u01b1\u01af\3\2\2\2")
        buf.write("\u01b2\u01b3\7\60\2\2\u01b3\u01b5\3\2\2\2\u01b4\u019d")
        buf.write("\3\2\2\2\u01b4\u01a9\3\2\2\2\u01b5|\3\2\2\2\u01b6\u01b8")
        buf.write("\t\6\2\2\u01b7\u01b9\5\177@\2\u01b8\u01b7\3\2\2\2\u01b8")
        buf.write("\u01b9\3\2\2\2\u01b9\u01ba\3\2\2\2\u01ba\u01bb\5\u0081")
        buf.write("A\2\u01bb~\3\2\2\2\u01bc\u01bd\t\7\2\2\u01bd\u0080\3\2")
        buf.write("\2\2\u01be\u01c0\5m\67\2\u01bf\u01be\3\2\2\2\u01c0\u01c1")
        buf.write("\3\2\2\2\u01c1\u01bf\3\2\2\2\u01c1\u01c2\3\2\2\2\u01c2")
        buf.write("\u0082\3\2\2\2\u01c3\u01c6\n\b\2\2\u01c4\u01c6\5\u0085")
        buf.write("C\2\u01c5\u01c3\3\2\2\2\u01c5\u01c4\3\2\2\2\u01c6\u0084")
        buf.write("\3\2\2\2\u01c7\u01c8\5\u0087D\2\u01c8\u0086\3\2\2\2\u01c9")
        buf.write("\u01ca\7^\2\2\u01ca\u01cb\t\t\2\2\u01cb\u0088\3\2\2\2")
        buf.write("\u01cc\u01ce\7$\2\2\u01cd\u01cf\5\u008bF\2\u01ce\u01cd")
        buf.write("\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0")
        buf.write("\u01d1\7$\2\2\u01d1\u008a\3\2\2\2\u01d2\u01d4\5\u008d")
        buf.write("G\2\u01d3\u01d2\3\2\2\2\u01d4\u01d5\3\2\2\2\u01d5\u01d3")
        buf.write("\3\2\2\2\u01d5\u01d6\3\2\2\2\u01d6\u008c\3\2\2\2\u01d7")
        buf.write("\u01df\n\n\2\2\u01d8\u01df\5\u0085C\2\u01d9\u01da\7^\2")
        buf.write("\2\u01da\u01df\7\f\2\2\u01db\u01dc\7^\2\2\u01dc\u01dd")
        buf.write("\7\17\2\2\u01dd\u01df\7\f\2\2\u01de\u01d7\3\2\2\2\u01de")
        buf.write("\u01d8\3\2\2\2\u01de\u01d9\3\2\2\2\u01de\u01db\3\2\2\2")
        buf.write("\u01df\u008e\3\2\2\2\u01e0\u01e3\5%\23\2\u01e1\u01e3\5")
        buf.write("\t\5\2\u01e2\u01e0\3\2\2\2\u01e2\u01e1\3\2\2\2\u01e3\u0090")
        buf.write("\3\2\2\2\u01e4\u01e6\t\13\2\2\u01e5\u01e4\3\2\2\2\u01e6")
        buf.write("\u01e7\3\2\2\2\u01e7\u01e5\3\2\2\2\u01e7\u01e8\3\2\2\2")
        buf.write("\u01e8\u01e9\3\2\2\2\u01e9\u01ea\bI\2\2\u01ea\u0092\3")
        buf.write("\2\2\2\u01eb\u01ec\13\2\2\2\u01ec\u01ed\bJ\4\2\u01ed\u0094")
        buf.write("\3\2\2\2\u01ee\u01ef\13\2\2\2\u01ef\u0096\3\2\2\2\u01f0")
        buf.write("\u01f1\13\2\2\2\u01f1\u0098\3\2\2\2\30\2\u009f\u00ad\u016d")
        buf.write("\u016f\u017e\u0182\u018c\u0195\u019a\u019d\u01a4\u01af")
        buf.write("\u01b4\u01b8\u01c1\u01c5\u01ce\u01d5\u01de\u01e2\u01e7")
        buf.write("\5\b\2\2\38\2\3J\3")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BlockComment = 1
    LineComment = 2
    Auto = 3
    False_ = 4
    Integer = 5
    While = 6
    Of = 7
    Break = 8
    Float = 9
    Return = 10
    Void = 11
    Inherit = 12
    Boolean_ = 13
    For = 14
    String = 15
    Function = 16
    Do = 17
    True_ = 18
    Out = 19
    Else = 20
    If = 21
    Continue = 22
    Array = 23
    Plus = 24
    Minus = 25
    Star = 26
    Div = 27
    Mod = 28
    Not = 29
    AndAnd = 30
    OrOr = 31
    Equal = 32
    NotEqual = 33
    Less = 34
    LessEqual = 35
    Greater = 36
    GreaterEqual = 37
    ColonColon = 38
    LeftParen = 39
    RightParen = 40
    LeftBracket = 41
    RightBracket = 42
    LeftBrace = 43
    RightBrace = 44
    Dot = 45
    Comma = 46
    Semi = 47
    Colon = 48
    Assign = 49
    Under = 50
    Identifier = 51
    Literal = 52
    IntegerConstant = 53
    FloatingConstant = 54
    DigitSequence = 55
    StringLiteral = 56
    Boolean = 57
    WS = 58
    ERROR_CHAR = 59
    UNCLOSE_STRING = 60
    ILLEGAL_ESCAPE = 61

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
            "BlockComment", "LineComment", "Auto", "False_", "Integer", 
            "While", "Of", "Break", "Float", "Return", "Void", "Inherit", 
            "Boolean_", "For", "String", "Function", "Do", "True_", "Out", 
            "Else", "If", "Continue", "Array", "Plus", "Minus", "Star", 
            "Div", "Mod", "Not", "AndAnd", "OrOr", "Equal", "NotEqual", 
            "Less", "LessEqual", "Greater", "GreaterEqual", "ColonColon", 
            "LeftParen", "RightParen", "LeftBracket", "RightBracket", "LeftBrace", 
            "RightBrace", "Dot", "Comma", "Semi", "Colon", "Assign", "Under", 
            "Identifier", "Literal", "IntegerConstant", "FloatingConstant", 
            "DigitSequence", "StringLiteral", "Boolean", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "BlockComment", "LineComment", "Auto", "False_", "Integer", 
                  "While", "Of", "Break", "Float", "Return", "Void", "Inherit", 
                  "Boolean_", "For", "String", "Function", "Do", "True_", 
                  "Out", "Else", "If", "Continue", "Array", "Plus", "Minus", 
                  "Star", "Div", "Mod", "Not", "AndAnd", "OrOr", "Equal", 
                  "NotEqual", "Less", "LessEqual", "Greater", "GreaterEqual", 
                  "ColonColon", "LeftParen", "RightParen", "LeftBracket", 
                  "RightBracket", "LeftBrace", "RightBrace", "Dot", "Comma", 
                  "Semi", "Colon", "Assign", "Under", "Identifier", "IdentifierNondigit", 
                  "Nondigit", "Digit", "Literal", "IntegerConstant", "DecimalConstant", 
                  "NonzeroDigit", "FloatingConstant", "DecimalFloatingConstant", 
                  "FractionalConstant", "ExponentPart", "Sign", "DigitSequence", 
                  "CChar", "EscapeSequence", "SimpleEscapeSequence", "StringLiteral", 
                  "SCharSequence", "SChar", "Boolean", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[54] = self.Literal_action 
            actions[72] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def Literal_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text=self.text.replace("_","")
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     


