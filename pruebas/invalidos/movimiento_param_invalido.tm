// Error esperado: movimiento inválido 'XYZ'
subrutina S(d) {
    alfabeto { 1, _ }
    estados { i, f }
    inicial: i;
    finales: { f };
    transiciones {
        i, 1 -> f, 1, d;
    }
}

maquina A {
    alfabeto { 1, _ }
    estados { i, f }
    inicial: i;
    finales: { f };
    usa S(XYZ) como s;
    transiciones {
        i, 1 -> s_ini, 1, DER;
        s_fin, 1 -> f, 1, DER;
    }
}
