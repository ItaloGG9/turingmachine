// Error esperado: subrutina no definida 'SubQueNoExiste'
maquina A {
    alfabeto { _ }
    estados { q0, qF }
    inicial: q0;
    finales: { qF };
    usa SubQueNoExiste() como sub;
}
