from maquina_turing.generado.MaquinaTuringVisitor import MaquinaTuringVisitor
from maquina_turing.generado.MaquinaTuringParser import MaquinaTuringParser
from maquina_turing.tabla_simbolos import TablaSimbolos

class VisitanteMaquina(MaquinaTuringVisitor):
    def __init__(self, repo):
        self.repo = repo
        
    def visitDeclMaquina(self, ctx:MaquinaTuringParser.DeclMaquinaContext):
        nombre = ctx.ID().getText()
        if nombre in self.repo.maquinas or nombre in self.repo.subrutinas:
            self.repo.errores.append(f"Error semántico [línea {ctx.start.line}:{ctx.start.column}]: nombre duplicado '{nombre}'")
            return
            
        tabla = TablaSimbolos()
        self.procesar_bloques(ctx.sentencia(), tabla, nombre)
        
        # Opcionales de cabezal y cinta
        for stmt in ctx.sentencia():
            if stmt.sentCinta():
                s = stmt.sentCinta().CADENA().getText()
                tabla.cinta_inicial = s[1:-1] # remover comillas
            elif stmt.sentCabezal():
                tabla.cabezal_inicial = int(stmt.sentCabezal().ENTERO().getText())
        
        tabla.check_estructura_basica(nombre, self.repo.errores)
        self.repo.maquinas[nombre] = tabla

    def visitDeclSubrutina(self, ctx:MaquinaTuringParser.DeclSubrutinaContext):
        nombre = ctx.ID().getText()
        if nombre in self.repo.maquinas or nombre in self.repo.subrutinas:
            self.repo.errores.append(f"Error semántico [línea {ctx.start.line}:{ctx.start.column}]: nombre duplicado '{nombre}'")
            return
            
        params = []
        if ctx.listaParametros():
            params = [id.getText() for id in ctx.listaParametros().ID()]
            
        tabla = TablaSimbolos(params=params)
        self.procesar_bloques(ctx.sentencia(), tabla, nombre)
        
        tabla.check_estructura_basica(nombre, self.repo.errores)
        tabla.validar_plantilla(nombre, self.repo.errores)
        self.repo.subrutinas[nombre] = tabla

    def procesar_bloques(self, sentencias, tabla, nombre_contexto):
        for stmt in sentencias:
            if stmt.sentAlfabeto():
                tabla.bloques['alfabeto'] += 1
                for sym in stmt.sentAlfabeto().listaSimbolos().simbolo():
                    res = tabla.add_simbolo(sym.getText())
                    if not res:
                        self.repo.errores.append(f"Error semántico [línea {sym.start.line}:{sym.start.column}] en '{nombre_contexto}': símbolo duplicado '{sym.getText()}'")
                    
            elif stmt.sentEstados():
                tabla.bloques['estados'] += 1
                for id_ctx in stmt.sentEstados().listaIds().ID():
                    res = tabla.add_estado_declarado(id_ctx.getText())
                    if not res:
                        self.repo.errores.append(f"Error semántico [línea {id_ctx.symbol.line}:{id_ctx.symbol.column}] en '{nombre_contexto}': estado duplicado '{id_ctx.getText()}'")
                    
            elif stmt.sentInicial():
                tabla.bloques['inicial'] += 1
                ini_id = stmt.sentInicial().ID().getText()
                tabla.inicial = ini_id
                tabla.inicial_linea = stmt.sentInicial().start.line
                tabla.inicial_col = stmt.sentInicial().start.column
                
            elif stmt.sentFinales():
                tabla.bloques['finales'] += 1
                for id_ctx in stmt.sentFinales().listaIds().ID():
                    fin_id = id_ctx.getText()
                    tabla.finales[fin_id] = {'linea': id_ctx.symbol.line, 'col': id_ctx.symbol.column}
                    
            elif stmt.sentTransiciones():
                for t_ctx in stmt.sentTransiciones().transicion():
                    st = t_ctx.ID(0).getText()
                    rd = t_ctx.simbolo(0).getText()
                    nst = t_ctx.ID(1).getText()
                    wr = t_ctx.simbolo(1).getText()
                    mv = t_ctx.movimiento().getText()
                    linea = t_ctx.start.line
                    col = t_ctx.start.column
                    tabla.add_transicion(st, rd, nst, wr, mv, linea, col)
                    
            elif stmt.sentUsa():
                sub_name = stmt.sentUsa().ID(0).getText()
                args = []
                if stmt.sentUsa().listaArgumentos():
                    args = [e.getText() for e in stmt.sentUsa().listaArgumentos().expresion()]
                    
                repetir_var = '1'
                if stmt.sentUsa().REPETIR():
                    repetir_var = stmt.sentUsa().expresion().getText()
                    
                alias = sub_name
                if stmt.sentUsa().COMO():
                    alias = stmt.sentUsa().ID(1).getText()
                
                tabla.usos.append({
                    'nombre': sub_name,
                    'args': args,
                    'repetir_var': repetir_var,
                    'alias': alias,
                    'linea': stmt.sentUsa().start.line,
                    'col': stmt.sentUsa().start.column
                })
