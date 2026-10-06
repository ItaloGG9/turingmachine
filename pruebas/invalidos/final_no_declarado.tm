// Error esperado: estado final 'qW' no declarado en 'estados'
maquina A {
    alfabeto { 1, _ }
    estados { q0, qF }
    inicial: q0;
    finales: { qW };
    transiciones {
        q0, 1 -> qF, 1, DER;
    }
}
