// Error esperado: el símbolo 'ab' no es de un solo carácter
maquina A {
    alfabeto { ab, 1, _ }
    estados { q0, qF }
    inicial: q0;
    finales: { qF };
    transiciones {
        q0, 1 -> qF, 1, DER;
    }
}
