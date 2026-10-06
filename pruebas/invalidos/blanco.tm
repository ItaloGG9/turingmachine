// Error esperado: el alfabeto debe incluir el símbolo blanco '_'
maquina A {
    alfabeto { 0, 1 }
    estados { q0, qF }
    inicial: q0;
    finales: { qF };
    transiciones {
        q0, 1 -> qF, 1, DER;
    }
}
