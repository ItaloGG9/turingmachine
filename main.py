import sys
import argparse
from antlr4 import FileStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener

from maquina_turing.generado.MaquinaTuringLexer import MaquinaTuringLexer
from maquina_turing.generado.MaquinaTuringParser import MaquinaTuringParser
from maquina_turing.tabla_simbolos import Repositorio
from maquina_turing.visitor import VisitanteMaquina
from maquina_turing.expansion import expandir_maquina
from maquina_turing.interprete import simular

class EscuchaErrores(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"Error sintáctico [línea {line}:{column}]: {msg}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Intérprete del DSL de máquinas de Turing")
    parser.add_argument("archivo", help="Archivo .tm a procesar")
    parser.add_argument("cinta", nargs='?', default="", help="Cinta inicial (vacía por defecto)")
    parser.add_argument("--maquina", help="Máquina a ejecutar")
    parser.add_argument("--max-pasos", type=int, default=10000, help="Límite de pasos")
    parser.add_argument("--listar", action="store_true", help="Lista las máquinas definidas")
    parser.add_argument("--verboso", action="store_true", help="Imprime la representación interna")
    parser.add_argument("--cabezal", type=int, help="Posición inicial del cabezal")
    
    args = parser.parse_args()
    
    input_stream = FileStream(args.archivo, encoding='utf-8')
    lexer = MaquinaTuringLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(EscuchaErrores())
    
    stream = CommonTokenStream(lexer)
    tm_parser = MaquinaTuringParser(stream)
    tm_parser.removeErrorListeners()
    tm_parser.addErrorListener(EscuchaErrores())
    
    tree = tm_parser.programa()
    
    repo = Repositorio()
    visitor = VisitanteMaquina(repo)
    visitor.visit(tree)
    
    # Validar que no hayan errores de parseo o recolección
    repo.check_errores()
    
    if not repo.maquinas:
        print("Error: No se definió ninguna máquina en el archivo.")
        sys.exit(1)
        
    # Se expanden y validan todas las máquinas del archivo, no solo la que se ejecuta
    maquinas_expandidas = {}
    for nombre in repo.maquinas.keys():
        exp = expandir_maquina(nombre, repo)
        if exp:
            exp.validar_maquina_completa(nombre, repo.errores)
            maquinas_expandidas[nombre] = exp
            
    repo.check_errores()
    
    if args.listar:
        print("Máquinas disponibles:")
        for m in repo.maquinas.keys():
            print(f" - {m}")
        return
        
    nombre_maquina = args.maquina
    if not nombre_maquina:
        nombre_maquina = list(repo.maquinas.keys())[0]
        
    if nombre_maquina not in maquinas_expandidas:
        print(f"Error: La máquina '{nombre_maquina}' no existe.")
        sys.exit(1)
        
    maquina_a_ejecutar = maquinas_expandidas[nombre_maquina]
    
    if args.cabezal is not None:
        maquina_a_ejecutar.cabezal_inicial = args.cabezal
        
    cinta_str = args.cinta
    if not cinta_str and maquina_a_ejecutar.cinta_inicial:
        cinta_str = maquina_a_ejecutar.cinta_inicial
        
    simular(nombre_maquina, maquina_a_ejecutar, cinta_str, args.max_pasos, args.verboso)

if __name__ == '__main__':
    main()
