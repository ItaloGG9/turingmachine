subrutina escribir(s) {
    alfabeto { 1, 0, _ }
    estados { s, f }
    inicial: s;
    finales: { f };
    transiciones { s, _ -> f, s, DER; }
}
maquina M {
    alfabeto { 1, 0, _ }
    estados { q0, qA }
    inicial: q0;
    finales: { qA };
    usa escribir(1) como e;
    transiciones { q0, _ -> e_ini, _, QUIETO; e_fin, _ -> qA, _, QUIETO; }
}
