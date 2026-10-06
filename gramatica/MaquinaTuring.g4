grammar MaquinaTuring;

// ==========================================
// REGLAS SINTÁCTICAS (Gramática Libre de Contexto)
// ==========================================

programa: declaracion+ EOF;

declaracion: declMaquina | declSubrutina;

declMaquina: MAQUINA ID '{' sentencia+ '}';

declSubrutina: SUBRUTINA ID '(' listaParametros? ')' '{' sentencia+ '}';

listaParametros: ID (',' ID)*;

sentencia: sentAlfabeto
         | sentEstados
         | sentInicial
         | sentFinales
         | sentTransiciones
         | sentUsa
         | sentCinta
         | sentCabezal ;

sentAlfabeto: ALFABETO '{' listaSimbolos '}';
sentEstados: ESTADOS '{' listaIds '}';
sentInicial: INICIAL ':' ID ';';
sentFinales: FINALES ':' '{' listaIds '}' ';';
sentTransiciones: TRANSICIONES '{' transicion+ '}';
sentUsa: USA ID ('(' listaArgumentos? ')')? (REPETIR expresion)? (COMO ID)? ';';

sentCinta: CINTA ':' CADENA ';';
sentCabezal: CABEZAL ':' ENTERO ';';

listaSimbolos: simbolo (',' simbolo)*;
listaIds: ID (',' ID)*;

transicion: ID ',' simbolo FLECHA ID ',' simbolo ',' movimiento ';';

movimiento: DER | IZQ | QUIETO | ID;

listaArgumentos: expresion (',' expresion)*;
expresion: ID | ENTERO | simbolo | movimiento; 

// Un símbolo de la cinta
simbolo: ID | ENTERO | CARACTER_ESPECIAL;

// ==========================================
// REGLAS LÉXICAS (Expresiones Regulares)
// ==========================================

MAQUINA: 'maquina';
SUBRUTINA: 'subrutina';
ALFABETO: 'alfabeto';
ESTADOS: 'estados';
INICIAL: 'inicial';
FINALES: 'finales';
TRANSICIONES: 'transiciones';
USA: 'usa';
REPETIR: 'repetir';
COMO: 'como';
CINTA: 'cinta';
CABEZAL: 'cabezal';

DER: 'DER';
IZQ: 'IZQ';
QUIETO: 'QUIETO';
FLECHA: '->';

ID: [a-zA-Z_][a-zA-Z0-9_]*;
ENTERO: [0-9]+;
CADENA: '"' ~["]* '"' | '\'' ~[']* '\'';
CARACTER_ESPECIAL: [+\-*/!@#$%^&<>=?|~];

ESPACIO: [ \t\r\n]+ -> skip;
COMENTARIO: '//' ~[\r\n]* -> skip;
COMENTARIO_BLOQUE: '/*' .*? '*/' -> skip;
