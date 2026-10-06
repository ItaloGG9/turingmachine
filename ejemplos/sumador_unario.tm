maquina SumadorUnario {
    alfabeto { 1, +, _ }
    estados { q0, q1, q2, qF }
    inicial: q0;
    finales: { qF };
    transiciones {
        // Avanza sobre los unos
        q0, 1 -> q0, 1, DER;
        
        // Reemplaza el + por un 1
        q0, + -> q1, 1, DER;
        
        // Sigue avanzando sobre el segundo sumando
        q1, 1 -> q1, 1, DER;
        
        // Llega al final, retrocede para borrar el último 1
        q1, _ -> q2, _, IZQ;
        
        // Borra el 1 extra, reemplazándolo por blanco
        q2, 1 -> qF, _, QUIETO;
    }
}
