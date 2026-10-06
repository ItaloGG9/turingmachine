# DSL de Máquinas de Turing

Este proyecto es un intérprete de un DSL (Domain-Specific Language) para definir y simular Máquinas de Turing, desarrollado con Python 3 y ANTLR4. Cumple con los requerimientos del Certamen I de Lenguajes de Programación.

## Requisitos
* Python 3
* Java (para regenerar el parser con ANTLR, si modificas `gramatica/MaquinaTuring.g4`)

## Cómo compilar y ejecutar
Usa los siguientes comandos `make` provistos (requieren `make` instalado en el sistema; en caso contrario, lee el contenido de `Makefile` para ejecutar los comandos equivalentes):

* `make deps`: Instala las dependencias de Python (`antlr4-python3-runtime==4.9.3`).
* `make parser`: Regenera los archivos lexer/parser/visitor a partir de la gramática `.g4`.
* `make run ARCHIVO=ejemplos/complemento.tm CINTA=010`: Simula una máquina de Turing.
* `make demo`: Ejecuta las 4 máquinas de ejemplo demostrativas (complemento, sumador, incrementador, subrutinas).
* `make test`: Ejecuta toda la batería de pruebas (casos válidos y los más de 15 casos inválidos detallando su falla correspondiente).

Alternativa manual:
```bash
python main.py ejemplos/complemento.tm 010
```

## Sintaxis del DSL y Ejemplos

### Máquina de Ejemplo (Negador Unario)
```text
maquina Complemento {
    alfabeto { 0, 1, _ }
    estados { q0, qA }
    inicial: q0;
    finales: { qA };
    transiciones {
        q0, 0 -> q0, 1, DER; 
        q0, 1 -> q0, 0, DER; 
        q0, _ -> qA, _, QUIETO; 
    }
}
```

### Composición por Subrutinas
Las subrutinas permiten parametrizar tanto por Símbolo como por Entero (estructuralmente). Se declaran fuera de las máquinas y se instancian con la palabra clave `usa`.

```text
subrutina escribir_simbolo(s) {
    alfabeto { 1, _ }
    estados { qE, qF }
    inicial: qE;
    finales: { qF };
    transiciones {
        qE, _ -> qF, s, DER;
        qE, 1 -> qF, s, DER;
    }
}

maquina Prueba {
    alfabeto { 1, _ }
    estados { inicial, final }
    inicial: inicial;
    finales: { final };
    
    // Inyección múltiple mediante repetidor, creando 3 copias y enlazándolas automáticamente:
    usa escribir_simbolo(1) repetir 3 como esc;
    
    transiciones {
        inicial, _ -> esc_ini, _, QUIETO;
        esc_fin, _ -> final, _, QUIETO;
    }
}
```
> **Nota de inyección:** Cuando se utiliza un `usa` con un alias (o por defecto el nombre de la subrutina), el intérprete inyecta en la máquina padre dos estados especiales virtuales llamados `<alias>_ini` y `<alias>_fin` que sirven como puntos de anclaje estables para no tener que depender de la cantidad de repeticiones de la subrutina instanciada.

## Acciones Semánticas
Las acciones se construyen utilizando el patrón de diseño `Visitor` provisto por ANTLR (`VisitanteMaquina`):
1. **Visit:** Se recorre el Árbol de Sintaxis Abstracta (AST).
2. **Construcción:** Para cada nodo, se llena una `TablaSimbolos` en memoria por máquina y subrutina.
3. **Expansión (Macros):** En `expansion.py`, se resuelven recursivamente las sentencias `usa`, reemplazando variables locales y clonando la tabla de transiciones, auto-vinculando los estados finales de iteraciones a los iniciales subsiguientes.

## Tabla de Símbolos y Validaciones
Las validaciones son estrictas y acumulativas (se reportan todos los errores, sin detenerse al primero) en `tabla_simbolos.py`:
- **Determinismo:** Ninguna tupla `(estado, simbolo_leido)` tiene múltiples transiciones.
- El estado inicial y los finales están declarados en la lista de estados, y su bloque existe exactamente una vez.
- Se reportan nombres de estados y símbolos duplicados dentro de la misma máquina.
- Todo símbolo leído/escrito pertenece explícitamente al `alfabeto`.
- El alfabeto incluye el símbolo blanco (`_`).
- Cada símbolo es de **un solo carácter**.
- Los movimientos deben ser válidos (`DER`, `IZQ` o `QUIETO`).
- Durante la expansión de subrutinas se comprueban la aridad, el valor de `repetir`, la ausencia de recursión y los alias duplicados.
- Se validan estructuralmente todas las máquinas y subrutinas declaradas en el archivo, incluso las que no se usan o simulan.
- Las subrutinas se validan tempranamente como plantilla en su propia tabla.
- Se valida el rango correcto al inicializar el cabezal (`--cabezal` o `cabezal:`).

## Supuestos de Diseño (Bordes de la cinta)
**Cinta Extensible Dinámicamente:** La cinta de la máquina es finita en memoria pero conceptualmente infinita, es decir, **dinámicamente extensible por ambos extremos**.
- Celda `0` es el comienzo original de la cinta dada por el input inicial.
- Si el cabezal retrocede más allá de la celda `0`, la cinta extiende su memoria agregando una nueva celda en el índice `0` con el símbolo blanco (`_`). 
- Las posiciones hacia la izquierda del 0 original quedan con índices negativos (-1, -2, ...), mientras que las extensiones a la derecha se agregan al final.
- **Detención:** La máquina se detiene y reporta resultado final al entrar a un estado declarado como `final`, si no encuentra una transición declarada para `(estado, simbolo)` (RECHAZA), o si alcanza la variable `--max-pasos` para evitar bucles infinitos.

## Traza de Ejemplo (Complemento Unario)
```text
paso  estado                    lee   acción                    cinta después   cabezal
0     q0                        0     escribe 1, mueve DER      1 1 0           -> celda 1
1     q0                        1     escribe 0, mueve DER      1 0 0           -> celda 2
2     q0                        0     escribe 1, mueve DER      1 0 1           -> celda 3
3     q0                        _     pasa a q0 (acepta)        1 0 1           (alto)

Resultado: ACEPTA
Cinta final: 101
```

## Gramática en EBNF y Tokens

### Reglas Léxicas (Tokens)
```ebnf
MAQUINA           ::= "maquina"
SUBRUTINA         ::= "subrutina"
ALFABETO          ::= "alfabeto"
ESTADOS           ::= "estados"
INICIAL           ::= "inicial"
FINALES           ::= "finales"
TRANSICIONES      ::= "transiciones"
USA               ::= "usa"
REPETIR           ::= "repetir"
COMO              ::= "como"
CINTA             ::= "cinta"
CABEZAL           ::= "cabezal"

DER               ::= "DER"
IZQ               ::= "IZQ"
QUIETO            ::= "QUIETO"
FLECHA            ::= "->"

ID                ::= [a-zA-Z_][a-zA-Z0-9_]*
ENTERO            ::= [0-9]+
CADENA            ::= '"' ~["]* '"' | "'" ~[']* "'"
CARACTER_ESPECIAL ::= [+\-*/!@#$%^&<>=?|~]
```

### Reglas Sintácticas (Gramática Libre de Contexto)
```ebnf
programa         ::= declaracion+ EOF
declaracion      ::= declMaquina | declSubrutina
declMaquina      ::= MAQUINA ID "{" sentencia+ "}"
declSubrutina    ::= SUBRUTINA ID "(" listaParametros? ")" "{" sentencia+ "}"
listaParametros  ::= ID ("," ID)*

sentencia        ::= sentAlfabeto | sentEstados | sentInicial | sentFinales 
                   | sentTransiciones | sentUsa | sentCinta | sentCabezal

sentAlfabeto     ::= ALFABETO "{" listaSimbolos "}"
sentEstados      ::= ESTADOS "{" listaIds "}"
sentInicial      ::= INICIAL ":" ID ";"
sentFinales      ::= FINALES ":" "{" listaIds "}" ";"
sentTransiciones ::= TRANSICIONES "{" transicion+ "}"
sentUsa          ::= USA ID ("(" listaArgumentos? ")")? (REPETIR expresion)? (COMO ID)? ";"
sentCinta        ::= CINTA ":" CADENA ";"
sentCabezal      ::= CABEZAL ":" ENTERO ";"

listaSimbolos    ::= simbolo ("," simbolo)*
listaIds         ::= ID ("," ID)*
transicion       ::= ID "," simbolo FLECHA ID "," simbolo "," movimiento ";"
movimiento       ::= DER | IZQ | QUIETO | ID
listaArgumentos  ::= expresion ("," expresion)*
expresion        ::= ID | ENTERO | simbolo | movimiento
simbolo          ::= ID | ENTERO | CARACTER_ESPECIAL
```


## Pruebas

Para ejecutar las pruebas del lenguaje, utilice el comando:
```bash
make test
```

La suite incluye pruebas válidas que aseguran que los ejemplos y los bordes funcionan correctamente, además de **10 casos inválidos** que demuestran la robustez de las validaciones semánticas del DSL:

| Archivo / comando | Qué demuestra |
|---|---|
| `determinismo.tm` | Determinismo (validación exigida) |
| `estado_no_declarado.tm` | Estados usados en transiciones están declarados (exigida) |
| `inicial_no_declarado.tm` | El estado inicial existe (exigida) |
| `final_no_declarado.tm` | Los estados finales existen (exigida) |
| `alfabeto.tm` | Símbolos leídos/escritos pertenecen al alfabeto (exigida) |
| `blanco.tm` | El alfabeto incluye el blanco `_` (exigida) |
| `char_largo.tm` | Cada símbolo es de un solo carácter (restricción del modelo) |
| `error_sintactico.tm` | La GLC rechaza un programa mal formado, con línea y columna |
| `movimiento_param_invalido.tm` | Movimiento inválido llegado por un parámetro |
| `sub_no_definida.tm` | Se rechaza usar una subrutina inexistente |

*Nota:* Existen otras validaciones en el código (duplicados, alcance en subrutinas, rango del cabezal, etc.) que no tienen un test automático unitario propio en esta tabla pero que son garantizadas por el compilador.

## Estructura del Proyecto

```text
TuringMachineDSL/
├── README.md
├── Makefile
├── requirements.txt
├── main.py
├── gramatica/
│   └── MaquinaTuring.g4
├── maquina_turing/
│   ├── generado/
│   ├── tabla_simbolos.py
│   ├── expansion.py
│   ├── interprete.py
│   └── visitor.py
├── herramientas/
│   ├── limpiar.py
│   └── antlr-4.9.3-complete.jar
├── ejemplos/
└── pruebas/
    ├── run_tests.py
    ├── validos/
    └── invalidos/
```
