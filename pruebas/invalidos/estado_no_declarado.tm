// Error esperado: estado no declarado 'qX'
maquina A {
    alfabeto { 1, _ }
    estados { q0, qF }
    inicial: q0;
    finales: { qF };
    transiciones {
        q0, 1 -> qX, 1, DER;
    }
}
