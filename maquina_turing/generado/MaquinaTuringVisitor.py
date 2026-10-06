# Generated from gramatica/MaquinaTuring.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MaquinaTuringParser import MaquinaTuringParser
else:
    from MaquinaTuringParser import MaquinaTuringParser

# This class defines a complete generic visitor for a parse tree produced by MaquinaTuringParser.

class MaquinaTuringVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MaquinaTuringParser#programa.
    def visitPrograma(self, ctx:MaquinaTuringParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaquinaTuringParser#declaracion.
    def visitDeclaracion(self, ctx:MaquinaTuringParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaquinaTuringParser#declMaquina.
    def visitDeclMaquina(self, ctx:MaquinaTuringParser.DeclMaquinaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaquinaTuringParser#declSubrutina.
    def visitDeclSubrutina(self, ctx:MaquinaTuringParser.DeclSubrutinaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaquinaTuringParser#listaParametros.
    def visitListaParametros(self, ctx:MaquinaTuringParser.ListaParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaquinaTuringParser#sentencia.
    def visitSentencia(self, ctx:MaquinaTuringParser.SentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaquinaTuringParser#sentAlfabeto.
    def visitSentAlfabeto(self, ctx:MaquinaTuringParser.SentAlfabetoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaquinaTuringParser#sentEstados.
    def visitSentEstados(self, ctx:MaquinaTuringParser.SentEstadosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaquinaTuringParser#sentInicial.
    def visitSentInicial(self, ctx:MaquinaTuringParser.SentInicialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaquinaTuringParser#sentFinales.
    def visitSentFinales(self, ctx:MaquinaTuringParser.SentFinalesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaquinaTuringParser#sentTransiciones.
    def visitSentTransiciones(self, ctx:MaquinaTuringParser.SentTransicionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaquinaTuringParser#sentUsa.
    def visitSentUsa(self, ctx:MaquinaTuringParser.SentUsaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaquinaTuringParser#sentCinta.
    def visitSentCinta(self, ctx:MaquinaTuringParser.SentCintaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaquinaTuringParser#sentCabezal.
    def visitSentCabezal(self, ctx:MaquinaTuringParser.SentCabezalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaquinaTuringParser#listaSimbolos.
    def visitListaSimbolos(self, ctx:MaquinaTuringParser.ListaSimbolosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaquinaTuringParser#listaIds.
    def visitListaIds(self, ctx:MaquinaTuringParser.ListaIdsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaquinaTuringParser#transicion.
    def visitTransicion(self, ctx:MaquinaTuringParser.TransicionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaquinaTuringParser#movimiento.
    def visitMovimiento(self, ctx:MaquinaTuringParser.MovimientoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaquinaTuringParser#listaArgumentos.
    def visitListaArgumentos(self, ctx:MaquinaTuringParser.ListaArgumentosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaquinaTuringParser#expresion.
    def visitExpresion(self, ctx:MaquinaTuringParser.ExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaquinaTuringParser#simbolo.
    def visitSimbolo(self, ctx:MaquinaTuringParser.SimboloContext):
        return self.visitChildren(ctx)



del MaquinaTuringParser