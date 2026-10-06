maquina IncrementadorBinario {
    alfabeto { 0, 1, _ }
    estados { q0, q1, qF }
    inicial: q0;
    finales: { qF };
    transiciones {
        // Mover el cabezal hasta el extremo derecho
        q0, 0 -> q0, 0, DER;
        q0, 1 -> q0, 1, DER;
        q0, _ -> q1, _, IZQ;
        
        // Sumar 1 de derecha a izquierda
        // Si hay 1, acarreamos (se vuelve 0) y seguimos a la izquierda
        q1, 1 -> q1, 0, IZQ;
        
        // Si hay 0, le sumamos el acarreo (se vuelve 1) y terminamos
        q1, 0 -> qF, 1, QUIETO;
        
        // Si llegamos a un blanco (extremo izquierdo), extendemos la cinta y terminamos
        q1, _ -> qF, 1, QUIETO;
    }
}
