// Error esperado: estado inicial 'qZ' no declarado en 'estados'
maquina A {
    alfabeto { 1, _ }
    estados { q0, qF }
    inicial: qZ;
    finales: { qF };
    transiciones {
        q0, 1 -> qF, 1, DER;
    }
}
