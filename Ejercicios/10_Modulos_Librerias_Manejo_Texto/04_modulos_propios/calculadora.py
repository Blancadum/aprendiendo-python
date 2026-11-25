"""
Enunciado:
Demostración de los 3 estilos de importación de módulos en Python:
1. 'import modulo': importa el módulo completo y requiere calificar (modulo.funcion).
2. 'from modulo import recurso': importa un elemento específico directamente en el espacio de nombres.
3. 'from modulo import recurso as alias': renombra el elemento importado con un alias para evitar colisiones.

Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo 12_Modulos
"""

# Forma 1: Importar módulo completo
import operaciones

n1 = 10
n2 = 4

print("--- Forma 1: import operaciones ---")
print("Suma:", operaciones.sumar(n1, n2))
print("Resta:", operaciones.restar(n1, n2))
print("Multiplicación:", operaciones.multiplicar(n1, n2))
print("División:", operaciones.dividir(n1, n2))

# Forma 2: Importar recurso específico directamente
from operaciones import restar

print("\n--- Forma 2: from operaciones import restar ---")
print("Resta directa:", restar(n1, n2))

# Forma 3: Importar con alias (as)
from operaciones import multiplicar as prod

print("\n--- Forma 3: from operaciones import multiplicar as prod ---")
print("Producto con alias:", prod(n1, n2))
