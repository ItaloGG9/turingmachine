// Error esperado: determinismo violado para (q0, 1)
maquina A {
    alfabeto { 1, _ }
    estados { q0, qF }
    inicial: q0;
    finales: { qF };
    transiciones {
        q0, 1 -> qF, 1, DER;
        q0, 1 -> q0, 1, DER;
    }
}
