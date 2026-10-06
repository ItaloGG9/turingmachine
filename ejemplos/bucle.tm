maquina BucleInfinito {
    alfabeto { 0, 1, _ }
    estados { q0, qF }
    inicial: q0;
    finales: { qF };
    transiciones {
        q0, _ -> q0, _, DER;
    }
}
