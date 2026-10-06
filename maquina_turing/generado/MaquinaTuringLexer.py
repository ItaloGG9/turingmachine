# Generated from gramatica/MaquinaTuring.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2 ")
        buf.write("\u00fe\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3")
        buf.write("\6\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\31\3\31\7\31\u00c1\n\31\f\31\16\31\u00c4\13\31")
        buf.write("\3\32\6\32\u00c7\n\32\r\32\16\32\u00c8\3\33\3\33\7\33")
        buf.write("\u00cd\n\33\f\33\16\33\u00d0\13\33\3\33\3\33\3\33\7\33")
        buf.write("\u00d5\n\33\f\33\16\33\u00d8\13\33\3\33\5\33\u00db\n\33")
        buf.write("\3\34\3\34\3\35\6\35\u00e0\n\35\r\35\16\35\u00e1\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\36\7\36\u00ea\n\36\f\36\16\36\u00ed")
        buf.write("\13\36\3\36\3\36\3\37\3\37\3\37\3\37\7\37\u00f5\n\37\f")
        buf.write("\37\16\37\u00f8\13\37\3\37\3\37\3\37\3\37\3\37\3\u00f6")
        buf.write("\2 \3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= \3\2\n\5\2C\\aa")
        buf.write("c|\6\2\62;C\\aac|\3\2\62;\3\2$$\3\2))\13\2##%(,-//\61")
        buf.write("\61>B``~~\u0080\u0080\5\2\13\f\17\17\"\"\4\2\f\f\17\17")
        buf.write("\2\u0105\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3")
        buf.write("\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2")
        buf.write("-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3")
        buf.write("\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\3")
        buf.write("?\3\2\2\2\5A\3\2\2\2\7C\3\2\2\2\tE\3\2\2\2\13G\3\2\2\2")
        buf.write("\rI\3\2\2\2\17K\3\2\2\2\21M\3\2\2\2\23U\3\2\2\2\25_\3")
        buf.write("\2\2\2\27h\3\2\2\2\31p\3\2\2\2\33x\3\2\2\2\35\u0080\3")
        buf.write("\2\2\2\37\u008d\3\2\2\2!\u0091\3\2\2\2#\u0099\3\2\2\2")
        buf.write("%\u009e\3\2\2\2\'\u00a4\3\2\2\2)\u00ac\3\2\2\2+\u00b0")
        buf.write("\3\2\2\2-\u00b4\3\2\2\2/\u00bb\3\2\2\2\61\u00be\3\2\2")
        buf.write("\2\63\u00c6\3\2\2\2\65\u00da\3\2\2\2\67\u00dc\3\2\2\2")
        buf.write("9\u00df\3\2\2\2;\u00e5\3\2\2\2=\u00f0\3\2\2\2?@\7}\2\2")
        buf.write("@\4\3\2\2\2AB\7\177\2\2B\6\3\2\2\2CD\7*\2\2D\b\3\2\2\2")
        buf.write("EF\7+\2\2F\n\3\2\2\2GH\7.\2\2H\f\3\2\2\2IJ\7<\2\2J\16")
        buf.write("\3\2\2\2KL\7=\2\2L\20\3\2\2\2MN\7o\2\2NO\7c\2\2OP\7s\2")
        buf.write("\2PQ\7w\2\2QR\7k\2\2RS\7p\2\2ST\7c\2\2T\22\3\2\2\2UV\7")
        buf.write("u\2\2VW\7w\2\2WX\7d\2\2XY\7t\2\2YZ\7w\2\2Z[\7v\2\2[\\")
        buf.write("\7k\2\2\\]\7p\2\2]^\7c\2\2^\24\3\2\2\2_`\7c\2\2`a\7n\2")
        buf.write("\2ab\7h\2\2bc\7c\2\2cd\7d\2\2de\7g\2\2ef\7v\2\2fg\7q\2")
        buf.write("\2g\26\3\2\2\2hi\7g\2\2ij\7u\2\2jk\7v\2\2kl\7c\2\2lm\7")
        buf.write("f\2\2mn\7q\2\2no\7u\2\2o\30\3\2\2\2pq\7k\2\2qr\7p\2\2")
        buf.write("rs\7k\2\2st\7e\2\2tu\7k\2\2uv\7c\2\2vw\7n\2\2w\32\3\2")
        buf.write("\2\2xy\7h\2\2yz\7k\2\2z{\7p\2\2{|\7c\2\2|}\7n\2\2}~\7")
        buf.write("g\2\2~\177\7u\2\2\177\34\3\2\2\2\u0080\u0081\7v\2\2\u0081")
        buf.write("\u0082\7t\2\2\u0082\u0083\7c\2\2\u0083\u0084\7p\2\2\u0084")
        buf.write("\u0085\7u\2\2\u0085\u0086\7k\2\2\u0086\u0087\7e\2\2\u0087")
        buf.write("\u0088\7k\2\2\u0088\u0089\7q\2\2\u0089\u008a\7p\2\2\u008a")
        buf.write("\u008b\7g\2\2\u008b\u008c\7u\2\2\u008c\36\3\2\2\2\u008d")
        buf.write("\u008e\7w\2\2\u008e\u008f\7u\2\2\u008f\u0090\7c\2\2\u0090")
        buf.write(" \3\2\2\2\u0091\u0092\7t\2\2\u0092\u0093\7g\2\2\u0093")
        buf.write("\u0094\7r\2\2\u0094\u0095\7g\2\2\u0095\u0096\7v\2\2\u0096")
        buf.write("\u0097\7k\2\2\u0097\u0098\7t\2\2\u0098\"\3\2\2\2\u0099")
        buf.write("\u009a\7e\2\2\u009a\u009b\7q\2\2\u009b\u009c\7o\2\2\u009c")
        buf.write("\u009d\7q\2\2\u009d$\3\2\2\2\u009e\u009f\7e\2\2\u009f")
        buf.write("\u00a0\7k\2\2\u00a0\u00a1\7p\2\2\u00a1\u00a2\7v\2\2\u00a2")
        buf.write("\u00a3\7c\2\2\u00a3&\3\2\2\2\u00a4\u00a5\7e\2\2\u00a5")
        buf.write("\u00a6\7c\2\2\u00a6\u00a7\7d\2\2\u00a7\u00a8\7g\2\2\u00a8")
        buf.write("\u00a9\7|\2\2\u00a9\u00aa\7c\2\2\u00aa\u00ab\7n\2\2\u00ab")
        buf.write("(\3\2\2\2\u00ac\u00ad\7F\2\2\u00ad\u00ae\7G\2\2\u00ae")
        buf.write("\u00af\7T\2\2\u00af*\3\2\2\2\u00b0\u00b1\7K\2\2\u00b1")
        buf.write("\u00b2\7\\\2\2\u00b2\u00b3\7S\2\2\u00b3,\3\2\2\2\u00b4")
        buf.write("\u00b5\7S\2\2\u00b5\u00b6\7W\2\2\u00b6\u00b7\7K\2\2\u00b7")
        buf.write("\u00b8\7G\2\2\u00b8\u00b9\7V\2\2\u00b9\u00ba\7Q\2\2\u00ba")
        buf.write(".\3\2\2\2\u00bb\u00bc\7/\2\2\u00bc\u00bd\7@\2\2\u00bd")
        buf.write("\60\3\2\2\2\u00be\u00c2\t\2\2\2\u00bf\u00c1\t\3\2\2\u00c0")
        buf.write("\u00bf\3\2\2\2\u00c1\u00c4\3\2\2\2\u00c2\u00c0\3\2\2\2")
        buf.write("\u00c2\u00c3\3\2\2\2\u00c3\62\3\2\2\2\u00c4\u00c2\3\2")
        buf.write("\2\2\u00c5\u00c7\t\4\2\2\u00c6\u00c5\3\2\2\2\u00c7\u00c8")
        buf.write("\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9")
        buf.write("\64\3\2\2\2\u00ca\u00ce\7$\2\2\u00cb\u00cd\n\5\2\2\u00cc")
        buf.write("\u00cb\3\2\2\2\u00cd\u00d0\3\2\2\2\u00ce\u00cc\3\2\2\2")
        buf.write("\u00ce\u00cf\3\2\2\2\u00cf\u00d1\3\2\2\2\u00d0\u00ce\3")
        buf.write("\2\2\2\u00d1\u00db\7$\2\2\u00d2\u00d6\7)\2\2\u00d3\u00d5")
        buf.write("\n\6\2\2\u00d4\u00d3\3\2\2\2\u00d5\u00d8\3\2\2\2\u00d6")
        buf.write("\u00d4\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7\u00d9\3\2\2\2")
        buf.write("\u00d8\u00d6\3\2\2\2\u00d9\u00db\7)\2\2\u00da\u00ca\3")
        buf.write("\2\2\2\u00da\u00d2\3\2\2\2\u00db\66\3\2\2\2\u00dc\u00dd")
        buf.write("\t\7\2\2\u00dd8\3\2\2\2\u00de\u00e0\t\b\2\2\u00df\u00de")
        buf.write("\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1\u00df\3\2\2\2\u00e1")
        buf.write("\u00e2\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3\u00e4\b\35\2")
        buf.write("\2\u00e4:\3\2\2\2\u00e5\u00e6\7\61\2\2\u00e6\u00e7\7\61")
        buf.write("\2\2\u00e7\u00eb\3\2\2\2\u00e8\u00ea\n\t\2\2\u00e9\u00e8")
        buf.write("\3\2\2\2\u00ea\u00ed\3\2\2\2\u00eb\u00e9\3\2\2\2\u00eb")
        buf.write("\u00ec\3\2\2\2\u00ec\u00ee\3\2\2\2\u00ed\u00eb\3\2\2\2")
        buf.write("\u00ee\u00ef\b\36\2\2\u00ef<\3\2\2\2\u00f0\u00f1\7\61")
        buf.write("\2\2\u00f1\u00f2\7,\2\2\u00f2\u00f6\3\2\2\2\u00f3\u00f5")
        buf.write("\13\2\2\2\u00f4\u00f3\3\2\2\2\u00f5\u00f8\3\2\2\2\u00f6")
        buf.write("\u00f7\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f7\u00f9\3\2\2\2")
        buf.write("\u00f8\u00f6\3\2\2\2\u00f9\u00fa\7,\2\2\u00fa\u00fb\7")
        buf.write("\61\2\2\u00fb\u00fc\3\2\2\2\u00fc\u00fd\b\37\2\2\u00fd")
        buf.write(">\3\2\2\2\13\2\u00c2\u00c8\u00ce\u00d6\u00da\u00e1\u00eb")
        buf.write("\u00f6\3\b\2\2")
        return buf.getvalue()


class MaquinaTuringLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    MAQUINA = 8
    SUBRUTINA = 9
    ALFABETO = 10
    ESTADOS = 11
    INICIAL = 12
    FINALES = 13
    TRANSICIONES = 14
    USA = 15
    REPETIR = 16
    COMO = 17
    CINTA = 18
    CABEZAL = 19
    DER = 20
    IZQ = 21
    QUIETO = 22
    FLECHA = 23
    ID = 24
    ENTERO = 25
    CADENA = 26
    CARACTER_ESPECIAL = 27
    ESPACIO = 28
    COMENTARIO = 29
    COMENTARIO_BLOQUE = 30

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'{'", "'}'", "'('", "')'", "','", "':'", "';'", "'maquina'", 
            "'subrutina'", "'alfabeto'", "'estados'", "'inicial'", "'finales'", 
            "'transiciones'", "'usa'", "'repetir'", "'como'", "'cinta'", 
            "'cabezal'", "'DER'", "'IZQ'", "'QUIETO'", "'->'" ]

    symbolicNames = [ "<INVALID>",
            "MAQUINA", "SUBRUTINA", "ALFABETO", "ESTADOS", "INICIAL", "FINALES", 
            "TRANSICIONES", "USA", "REPETIR", "COMO", "CINTA", "CABEZAL", 
            "DER", "IZQ", "QUIETO", "FLECHA", "ID", "ENTERO", "CADENA", 
            "CARACTER_ESPECIAL", "ESPACIO", "COMENTARIO", "COMENTARIO_BLOQUE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "MAQUINA", "SUBRUTINA", "ALFABETO", "ESTADOS", "INICIAL", 
                  "FINALES", "TRANSICIONES", "USA", "REPETIR", "COMO", "CINTA", 
                  "CABEZAL", "DER", "IZQ", "QUIETO", "FLECHA", "ID", "ENTERO", 
                  "CADENA", "CARACTER_ESPECIAL", "ESPACIO", "COMENTARIO", 
                  "COMENTARIO_BLOQUE" ]

    grammarFileName = "MaquinaTuring.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


