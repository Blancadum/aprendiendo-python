"""
tenemos 47 caramelos a repartir entre 5 niños
    Mostrar cuántos caramelos sobran

Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo1_tipos_datos
"""

caramelos = 47
ninos = 5

por_nino = int(caramelos//ninos)
sobran = caramelos % ninos

print(f"Cuántos caramelos hay en total: {caramelos}")
print(f"Esos caramelos repartidos entre {ninos} niños: {por_nino} caramelos por niño")
print(f"Y sobran: {sobran} caramelos")
