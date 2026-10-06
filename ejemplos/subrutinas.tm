subrutina escribir_simbolo(s) {
    alfabeto { 1, _ }
    estados { qE, qF }
    inicial: qE;
    finales: { qF };
    transiciones {
        qE, _ -> qF, s, DER;
        qE, 1 -> qF, s, DER;
    }
}

subrutina escribir_unos(n) {
    alfabeto { 1, _ }
    estados { ini, fin }
    inicial: ini;
    finales: { fin };
    usa escribir_simbolo(1) repetir n como e;
    transiciones {
        ini, _ -> e_ini, _, QUIETO;
        ini, 1 -> e_ini, 1, QUIETO;
        e_fin, _ -> fin, _, QUIETO;
        e_fin, 1 -> fin, 1, QUIETO;
    }
}

subrutina mover_hasta_blanco(dir) {
    alfabeto { 1, _ }
    estados { qM, qF }
    inicial: qM;
    finales: { qF };
    transiciones {
        qM, 1 -> qM, 1, dir;
        qM, _ -> qF, _, QUIETO;
    }
}

maquina AgregarUnos {
    alfabeto { 1, _ }
    estados { inicio, fin }
    inicial: inicio;
    finales: { fin };
    
    usa mover_hasta_blanco(DER) como mover;
    usa escribir_unos(3) como esc;
    
    transiciones {
        inicio, 1 -> mover_ini, 1, QUIETO;
        mover_fin, _ -> esc_ini, _, QUIETO;
        esc_fin, _ -> fin, _, QUIETO;
        
        // Si inicia con cinta vacía
        inicio, _ -> esc_ini, _, QUIETO;
    }
}
