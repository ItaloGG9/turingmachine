import sys

def asegurar_celda(cinta, cabezal, desplazamiento_cero):
    if cabezal < 0:
        cinta.insert(0, '_')
        cabezal = 0
        desplazamiento_cero += 1
    elif cabezal >= len(cinta):
        cinta.append('_')
    return cabezal, desplazamiento_cero

def simular(nombre, tabla, cinta_str, max_pasos=10000, verboso=False):
    # Validar cinta inicial
    for c in cinta_str:
        if c not in tabla.alfabeto:
            print(f"Error: la cinta inicial contiene el símbolo '{c}' que no pertenece al alfabeto de la máquina.")
            sys.exit(1)
            
    if verboso:
        print(f"--- Representación Interna de '{nombre}' ---")
        print(f"inicial = {tabla.inicial}")
        print(f"finales = {{ {', '.join(tabla.finales.keys())} }}")
        for (st, rd), reglas in tabla.transiciones.items():
            for nst, wr, mv, l, c in reglas:
                print(f"({st}, {rd}) -> ({nst}, {wr}, {mv})")
        print("---------------------------------------")
        
    cinta = list(cinta_str) if cinta_str else ['_']
    
    # Manejar cabezal inicial (opcional)
    cabezal_rel = tabla.cabezal_inicial
        
    if cabezal_rel < 0 or cabezal_rel >= len(cinta):
        limite = max(0, len(cinta)-1)
        print(f"Error: posición inicial del cabezal {cabezal_rel} fuera de la cinta (0..{limite})")
        sys.exit(1)
            
    head = cabezal_rel
    desplazamiento_cero = 0
    estado = tabla.inicial
    paso = 0
    
    print(f"{'paso':<5} {'estado':<25} {'lee':<5} {'acción':<25} {'cinta después':<15} {'cabezal'}")
    
    while estado not in tabla.finales:
        if paso >= max_pasos:
            resultado = "DETENIDA POR LÍMITE DE PASOS"
            break
            
        head, desplazamiento_cero = asegurar_celda(cinta, head, desplazamiento_cero)
        lee = cinta[head]
        
        clave = (estado, lee)
        if clave not in tabla.transiciones:
            resultado = f"RECHAZA (sin transición para ({estado}, {lee}))"
            break
            
        nst, wr, mv, l, c = tabla.transiciones[clave][0]
        
        cinta[head] = wr
        accion = f"escribe {wr}, mueve {mv}"
        
        estado_previo = estado
        estado = nst
        if mv == 'DER':
            head += 1
        elif mv == 'IZQ':
            head -= 1
        elif mv != 'QUIETO':
            print(f"Error interno: movimiento desconocido '{mv}'")
            sys.exit(1)
            
        cinta_str_actual = " ".join(cinta)
        cabezal_str = f"-> celda {head - desplazamiento_cero}"
        print(f"{paso:<5} {estado_previo:<25} {lee:<5} {accion:<25} {cinta_str_actual:<15} {cabezal_str}")
        paso += 1
        
    if estado in tabla.finales:
        resultado = "ACEPTA"
        head, desplazamiento_cero = asegurar_celda(cinta, head, desplazamiento_cero)
            
        lee_final = cinta[head]
        cinta_str_actual = " ".join(cinta)
        accion_final = f"pasa a {estado} (acepta)"
        print(f"{paso:<5} {estado:<25} {lee_final:<5} {accion_final:<25} {cinta_str_actual:<15} (alto)")
        
    # Limpiar blancos sobrantes (revisando si quedaron solos)
    cinta_final = list(cinta)
    while len(cinta_final) > 0 and cinta_final[0] == '_':
        cinta_final.pop(0)
    while len(cinta_final) > 0 and cinta_final[-1] == '_':
        cinta_final.pop()
        
    cf = "".join(cinta_final) if cinta_final else "(vacía)"
    
    print(f"\nResultado: {resultado}")
    print(f"Cinta final: {cf}")
