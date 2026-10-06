import copy

def expandir_maquina(nombre, repo, call_stack=None, args_actuales=None, params_actuales=None):
    if call_stack is None:
        call_stack = []
    if args_actuales is None:
        args_actuales = []
    if params_actuales is None:
        params_actuales = []
        
    param_map = dict(zip(params_actuales, args_actuales))
    def val(x):
        return param_map.get(x, x)
        
    if nombre in repo.maquinas:
        tabla_orig = repo.maquinas[nombre]
    elif nombre in repo.subrutinas:
        tabla_orig = repo.subrutinas[nombre]
    else:
        return None
        
    if nombre in call_stack:
        repo.errores.append(f"Error semántico: recursión detectada {call_stack} -> {nombre}")
        return None
        
    call_stack.append(nombre)
    tabla = copy.deepcopy(tabla_orig)
    
    # 1. Aplicar parámetros a la propia tabla
    for uso in tabla.usos:
        uso['repetir_var'] = val(uso['repetir_var'])
        uso['args'] = [val(a) for a in uso['args']]
        
    nuevas_trans = {}
    for (st, rd), reglas in tabla.transiciones.items():
        n_st = st # Los parámetros no pueden renombrar estados
        n_rd = val(rd)
        nuevas_reglas = []
        for (nst, wr, mv, l, c) in reglas:
            nuevas_reglas.append((nst, val(wr), val(mv), l, c))
        nuevas_trans[(n_st, n_rd)] = nuevas_reglas
    tabla.transiciones = nuevas_trans
    
    # 2. Expandir subrutinas usadas
    alias_usados = set()
    usos_a_procesar = tabla.usos
    tabla.usos = []
    
    for uso in usos_a_procesar:
        sub_name = uso['nombre']
        args = uso['args']
        rep_var = uso['repetir_var']
        alias = uso['alias']
        linea = uso['linea']
        col = uso['col']
        
        if alias in alias_usados:
            repo.errores.append(f"Error semántico [línea {linea}:{col}]: alias duplicado '{alias}', use 'como'")
            continue
        alias_usados.add(alias)
        
        if sub_name not in repo.subrutinas:
            repo.errores.append(f"Error semántico [línea {linea}:{col}]: subrutina no definida '{sub_name}'")
            continue
            
        sub_template = repo.subrutinas[sub_name]
        
        if len(args) != len(sub_template.params):
            repo.errores.append(f"Error semántico [línea {linea}:{col}]: aridad incorrecta al llamar '{sub_name}'. Esperaba {len(sub_template.params)}, recibió {len(args)}")
            continue
            
        try:
            reps = int(rep_var)
        except ValueError:
            repo.errores.append(f"Error semántico [línea {linea}:{col}]: valor de repetir inválido '{rep_var}'")
            continue
            
        if reps < 1:
            repo.errores.append(f"Error semántico [línea {linea}:{col}]: valor de repetir menor que 1 ({reps})")
            continue
            
        sub_exp = expandir_maquina(sub_name, repo, list(call_stack), args, sub_template.params)
        if not sub_exp:
            continue
            
        for s in sub_exp.alfabeto:
            if s not in tabla.alfabeto and s not in sub_template.params:
                repo.errores.append(f"Error semántico [línea {linea}:{col}]: símbolo '{s}' de '{sub_name}' fuera del alfabeto de '{nombre}'")
                
        # Inyectar N copias
        # Agregar los alias inicial y final como estados válidos si los inyectamos y usamos
        tabla.add_estado_declarado(f"{alias}_ini")
        tabla.add_estado_declarado(f"{alias}_fin")
        
        for i in range(1, reps + 1):
            def renombra(s_name, es_final=False, es_inicial=False):
                if es_inicial and i == 1:
                    return f"{alias}_ini"
                if es_final and i == reps:
                    return f"{alias}_fin"
                if es_final and i < reps:
                    return f"{alias}_{i+1}_{sub_exp.inicial}"
                if es_inicial:
                    return f"{alias}_{i}_{sub_exp.inicial}"
                return f"{alias}_{i}_{s_name}"
                
            for s_name in sub_exp.estados_declarados:
                es_ini = (s_name == sub_exp.inicial)
                es_fin = (s_name in sub_exp.finales)
                nuevo_nombre = renombra(s_name, es_fin, es_ini)
                tabla.add_estado_declarado(nuevo_nombre)
                
            for (st, rd), reglas in sub_exp.transiciones.items():
                es_ini_st = (st == sub_exp.inicial)
                es_fin_st = (st in sub_exp.finales)
                n_st = renombra(st, es_fin_st, es_ini_st)
                
                for (nst, wr, mv, l, c) in reglas:
                    es_ini_nst = (nst == sub_exp.inicial)
                    es_fin_nst = (nst in sub_exp.finales)
                    n_nst = renombra(nst, es_fin_nst, es_ini_nst)
                    
                    tabla.add_transicion(n_st, rd, n_nst, wr, mv, l, c)
                    
    return tabla
