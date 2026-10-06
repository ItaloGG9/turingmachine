import subprocess
import sys

def run_test(cmd, expect_fail=False, keywords=None, exact_match_lines=None):
    import os
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        env=env,
        shell=True
    )
    out, err = process.communicate()
    retcode = process.returncode
    
    output = out + err
    
    # Validar que NUNCA exista un Traceback
    if "Traceback" in output:
        print(f"FAILED (Traceback found): {cmd}")
        print("Output:")
        print(output)
        return False
    
    passed = True
    if expect_fail:
        if retcode == 0:
            passed = False
            print(f"FAILED (expected to fail but succeeded): {cmd}")
        else:
            if keywords:
                for kw in keywords:
                    if kw.lower() not in output.lower():
                        passed = False
                        print(f"FAILED (keyword '{kw}' not found): {cmd}")
                        print("Output:")
                        print(output)
                        break
    else:
        if retcode != 0:
            passed = False
            print(f"FAILED (expected to succeed but failed): {cmd}")
            print("Output:")
            print(output)
            
        if exact_match_lines:
            lines = output.strip().split('\n')
            for exact_line in exact_match_lines:
                found = any(exact_line.strip() == line.strip() for line in lines)
                if not found:
                    passed = False
                    print(f"FAILED (exact output line '{exact_line}' not found): {cmd}")
                    print("Output:")
                    print(output)
                    break
            
    if passed:
        print(f"OK: {cmd}")
    return passed

def main():
    print("Compilando tests...\\n")
    
    all_passed = True
    python_cmd = sys.executable
    
    # Pruebas Validas
    valid_tests = [
        (f"{python_cmd} main.py ejemplos/complemento.tm 010", False, [], ["Resultado: ACEPTA", "Cinta final: 101"]),
        (f"{python_cmd} main.py ejemplos/sumador_unario.tm 111+11", False, [], ["Resultado: ACEPTA", "Cinta final: 11111"]),
        (f"{python_cmd} main.py ejemplos/sumador_unario.tm 111+", False, [], ["Resultado: ACEPTA", "Cinta final: 111"]),
        (f"{python_cmd} main.py ejemplos/sumador_unario.tm +11", False, [], ["Resultado: ACEPTA", "Cinta final: 11"]),
        (f"{python_cmd} main.py ejemplos/sumador_unario.tm 11", False, [], ["Resultado: RECHAZA (sin transición para (q0, _))", "Cinta final: 11"]),
        (f"{python_cmd} main.py ejemplos/incrementador_binario.tm 1011", False, [], ["Resultado: ACEPTA", "Cinta final: 1100"]),
        (f"{python_cmd} main.py ejemplos/incrementador_binario.tm 111", False, [], ["Resultado: ACEPTA", "Cinta final: 1000"]),
        (f"{python_cmd} main.py ejemplos/incrementador_binario.tm 0", False, [], ["Resultado: ACEPTA", "Cinta final: 1"]),
        (f"{python_cmd} main.py ejemplos/subrutinas.tm 11", False, [], ["Resultado: ACEPTA", "Cinta final: 11111"]),
        (f"{python_cmd} main.py ejemplos/bucle.tm --max-pasos 50", False, [], ["Resultado: DETENIDA POR LÍMITE DE PASOS", "Cinta final: (vacía)"]),
        
        # Test de enteros:
        (f"{python_cmd} main.py pruebas/validos/enteros.tm \"\" --maquina M1", False, [], ["Resultado: ACEPTA", "Cinta final: 1"]),
        (f"{python_cmd} main.py pruebas/validos/enteros.tm \"\" --maquina M5", False, [], ["Resultado: ACEPTA", "Cinta final: 11111"]),
        (f"{python_cmd} main.py pruebas/validos/enteros.tm \"\" --maquina M23", False, [], ["Resultado: ACEPTA", "Cinta final: 11111"]),
        
        # Test nuevo de bloque 2
        (f"{python_cmd} main.py pruebas/validos/parametro_igual_a_estado.tm", False, [], ["Resultado: ACEPTA", "Cinta final: 1"])
    ]
    
    for cmd, fail, kws, matches in valid_tests:
        if not run_test(cmd, fail, kws, matches):
            all_passed = False
            
    # Pruebas Invalidas
    invalid_tests = [
        (f"{python_cmd} main.py pruebas/invalidos/determinismo.tm", True, ["determinismo"]),
        (f"{python_cmd} main.py pruebas/invalidos/estado_no_declarado.tm", True, ["no declarado"]),
        (f"{python_cmd} main.py pruebas/invalidos/alfabeto.tm", True, ["alfabeto"]),
        (f"{python_cmd} main.py pruebas/invalidos/blanco.tm", True, ["blanco"]),
        (f"{python_cmd} main.py pruebas/invalidos/char_largo.tm", True, ["un solo car"]),
        (f"{python_cmd} main.py pruebas/invalidos/error_sintactico.tm", True, ["missing", ";"]),
        (f"{python_cmd} main.py pruebas/invalidos/movimiento_param_invalido.tm", True, ["movimiento inv"]),
        (f"{python_cmd} main.py pruebas/invalidos/sub_no_definida.tm", True, ["no definida"]),
        (f"{python_cmd} main.py pruebas/invalidos/inicial_no_declarado.tm", True, ["inicial", "no declarado"]),
        (f"{python_cmd} main.py pruebas/invalidos/final_no_declarado.tm", True, ["final", "no declarado"])
    ]
        
    for cmd, fail, kws in invalid_tests:
        if not run_test(cmd, fail, kws, []):
            all_passed = False
            
    if not all_passed:
        sys.exit(1)
    else:
        print("\nTodos los tests pasaron exitosamente.")
        sys.exit(0)

if __name__ == '__main__':
    main()
