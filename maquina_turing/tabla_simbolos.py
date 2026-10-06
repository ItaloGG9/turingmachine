import sys

class TablaSimbolos:
    def __init__(self, params=None):
        self.params = params or []
        self.cinta_inicial = ""
        self.cabezal_inicial = 0
        self.alfabeto = set()
        self.estados_declarados = set() # Solo para llevar registro de si se duplicaron o no
        self.inicial = None
        self.inicial_linea = 0
        self.inicial_col = 0
        self.finales = {} # nombre -> {'linea': int, 'col': int}
        self.transiciones = {} # (estado, sim) -> [(nuevo_estado, sim, mov, linea, col)]
        self.usos = []
        self.bloques = {
            'alfabeto': 0,
            'estados': 0,
            'inicial': 0,
            'finales': 0
        }
        
    def add_simbolo(self, sim):
        if sim in self.alfabeto:
            return False
        self.alfabeto.add(sim)
        return True
        
    def add_estado_declarado(self, nombre):
        if nombre in self.estados_declarados:
            return False
        self.estados_declarados.add(nombre)
        return True
                
    def add_transicion(self, estado, lee, nuevo_estado, escribe, mov, linea, col):
        key = (estado, lee)
        if key not in self.transiciones:
            self.transiciones[key] = []
        self.transiciones[key].append((nuevo_estado, escribe, mov, linea, col))

    def check_estructura_basica(self, nombre_maquina, errores):
        """Validaciones de integridad básica de la estructura"""
        if self.bloques['alfabeto'] != 1:
            errores.append(f"Error semántico en '{nombre_maquina}': bloque duplicado o ausente 'alfabeto'.")
        if self.bloques['estados'] != 1:
            errores.append(f"Error semántico en '{nombre_maquina}': bloque duplicado o ausente 'estados'.")
        if self.bloques['inicial'] != 1:
            errores.append(f"Error semántico en '{nombre_maquina}': inicial ausente o duplicado.")
        if self.bloques['finales'] != 1:
            errores.append(f"Error semántico en '{nombre_maquina}': bloque duplicado o ausente 'finales'.")
        if len(self.transiciones) == 0 and len(self.usos) == 0:
            errores.append(f"Error semántico en '{nombre_maquina}': máquina o subrutina vacía (sin transiciones ni 'usa').")

    def validar_plantilla(self, nombre_contexto, errores):
        if self.inicial and self.inicial not in self.estados_declarados:
            errores.append(f"Error semántico [línea {self.inicial_linea}:{self.inicial_col}] en '{nombre_contexto}': estado inicial '{self.inicial}' no declarado en 'estados'.")
            
        for f, pos in self.finales.items():
            if f not in self.estados_declarados:
                errores.append(f"Error semántico [línea {pos['linea']}:{pos['col']}] en '{nombre_contexto}': estado final '{f}' no declarado en 'estados'.")
                
        for (st, rd), reglas in self.transiciones.items():
            nst, wr, mv, l, c = reglas[0]
            
            def es_valido(estado):
                if estado in self.estados_declarados:
                    return True
                for uso in self.usos:
                    alias = uso['alias']
                    if estado == f"{alias}_ini" or estado == f"{alias}_fin":
                        return True
                return False
                
            if not es_valido(st):
                errores.append(f"Error semántico [línea {l}:{c}] en '{nombre_contexto}': estado no declarado '{st}'")
            if not es_valido(nst):
                errores.append(f"Error semántico [línea {l}:{c}] en '{nombre_contexto}': estado no declarado '{nst}'")

    def validar_maquina_completa(self, nombre_maquina, errores):
        # El alfabeto debe incluir el símbolo blanco '_'
        if '_' not in self.alfabeto:
            errores.append(f"Error semántico en '{nombre_maquina}': el alfabeto debe incluir el símbolo blanco '_'")
            
        # Los símbolos deben ser de un solo carácter
        for s in self.alfabeto:
            if len(s) != 1:
                errores.append(f"Error semántico en '{nombre_maquina}': el símbolo '{s}' no es de un solo carácter")
                
        # El estado inicial y los finales deben estar declarados en la lista de estados
        if self.inicial and self.inicial not in self.estados_declarados:
            errores.append(f"Error semántico [línea {self.inicial_linea}:{self.inicial_col}] en '{nombre_maquina}': estado inicial '{self.inicial}' no declarado en 'estados'.")
            
        if not self.finales:
            errores.append(f"Error semántico en '{nombre_maquina}': debe haber al menos un estado final declarado.")
            
        for f, pos in self.finales.items():
            if f not in self.estados_declarados:
                errores.append(f"Error semántico [línea {pos['linea']}:{pos['col']}] en '{nombre_maquina}': estado final '{f}' no declarado en 'estados'.")
        
        # Validación de determinismo, estados y alfabeto en transiciones, y movimientos válidos
        for (st, rd), reglas in self.transiciones.items():
            if len(reglas) > 1:
                lineas = [r[3] for r in reglas]
                l = reglas[0][3]
                c = reglas[0][4]
                errores.append(f"Error semántico [línea {l}:{c}] en '{nombre_maquina}': determinismo violado para ({st}, {rd}) en líneas {lineas}")
                
            nst, wr, mv, l, c = reglas[0]
            
            if st not in self.estados_declarados:
                errores.append(f"Error semántico [línea {l}:{c}] en '{nombre_maquina}': estado no declarado '{st}'")
            if nst not in self.estados_declarados:
                errores.append(f"Error semántico [línea {l}:{c}] en '{nombre_maquina}': estado no declarado '{nst}'")
            if rd not in self.alfabeto:
                errores.append(f"Error semántico [línea {l}:{c}] en '{nombre_maquina}': símbolo leído '{rd}' no pertenece al alfabeto")
            if wr not in self.alfabeto:
                errores.append(f"Error semántico [línea {l}:{c}] en '{nombre_maquina}': símbolo escrito '{wr}' no pertenece al alfabeto")
                
            # Validar Movimiento
            if mv not in ['DER', 'IZQ', 'QUIETO']:
                errores.append(f"Error semántico [línea {l}:{c}] en '{nombre_maquina}': movimiento inválido '{mv}' (use DER, IZQ o QUIETO)")

class Repositorio:
    def __init__(self):
        self.maquinas = {}
        self.subrutinas = {}
        self.errores = []
        
    def check_errores(self):
        if self.errores:
            for err in self.errores:
                print(err)
            sys.exit(1)
