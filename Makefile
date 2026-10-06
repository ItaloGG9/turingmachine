# Detectar comando python cross-platform
ifeq ($(OS),Windows_NT)
    PYTHON ?= python
else
    PYTHON ?= $(shell command -v python3 || command -v python)
endif

JAVA ?= java
ANTLR_JAR = herramientas/antlr-4.9.3-complete.jar

.PHONY: all deps parser run demo test clean

all: parser

deps:
	$(PYTHON) -m pip install -r requirements.txt

parser:
	$(JAVA) -jar $(ANTLR_JAR) -Dlanguage=Python3 -visitor -no-listener -Xexact-output-dir -o maquina_turing/generado gramatica/MaquinaTuring.g4

run:
	$(PYTHON) main.py $(ARCHIVO) $(CINTA)

demo:
	$(PYTHON) main.py ejemplos/complemento.tm 010
	$(PYTHON) main.py ejemplos/sumador_unario.tm 111+11
	$(PYTHON) main.py ejemplos/incrementador_binario.tm 1011
	$(PYTHON) main.py ejemplos/subrutinas.tm 11

test:
	$(PYTHON) pruebas/run_tests.py

clean:
	$(PYTHON) herramientas/limpiar.py
