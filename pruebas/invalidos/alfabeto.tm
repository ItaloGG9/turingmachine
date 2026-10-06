// Error esperado: símbolo leído '1' no pertenece al alfabeto
maquina A {
    alfabeto { _ }
    estados { q0, qF }
    inicial: q0;
    finales: { qF };
    transiciones {
        q0, 1 -> qF, 1, DER;
    }
}
