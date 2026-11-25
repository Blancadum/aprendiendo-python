"""
Ejercicio 22: Análisis de préstamos hipotecarios (bank-loans.csv)

Enunciado:
Cargar y analizar el fichero 'bank-loans.csv' que contiene información sobre solicitantes de crédito:
- Edad (age), ocupación (job), estado civil (marital), educación (education).
- Historial crediticio: impago previo (default), préstamo hipotecario (housing) y préstamo personal (loan).

Objetivos del análisis:
1. Cargar el dataset verificando el delimitador ';' y la codificación adecuada.
2. Explorar la distribución de solicitudes por tipo de empleo y estado civil.
3. Calcular métricas básicas y proporciones de clientes con hipoteca o préstamos concedidos.

Autor: Blanca de Uña Martín
Curso: Machine Learning
"""

import os
import csv
from collections import Counter

# Limpiar pantalla
os.system("cls" if os.name == "nt" else "clear")

# Obtener ruta absoluta del archivo CSV
ruta_dir = os.path.dirname(os.path.abspath(__file__))
ruta_csv = os.path.join(ruta_dir, "bank-loans.csv")

if os.path.exists(ruta_csv):
    with open(ruta_csv, mode="r", encoding="utf-8-sig") as f:
        lector = csv.DictReader(f, delimiter=";")
        filas = list(lector)

    print(f"=== Resumen del Dataset de Préstamos ({len(filas)} registros) ===")
    print("Campos disponibles:", lector.fieldnames)

    print("\n=== Muestra de los primeros 3 registros ===")
    for fila in filas[:3]:
        print(fila)

    ocupaciones = Counter(fila["job"] for fila in filas)
    print("\n=== Distribución por Ocupación (Top 5) ===")
    for ocupacion, cuenta in ocupaciones.most_common(5):
        print(f"  {ocupacion:<15}: {cuenta} ({cuenta / len(filas) * 100:.1f}%)")

    estados_civiles = Counter(fila["marital"] for fila in filas)
    print("\n=== Distribución por Estado Civil ===")
    for estado, cuenta in estados_civiles.items():
        print(f"  {estado:<15}: {cuenta} ({cuenta / len(filas) * 100:.1f}%)")

    hipotecas = Counter(fila["housing"] for fila in filas)
    print("\n=== Clientes con Préstamo Hipotecario (housing) ===")
    for opcion, cuenta in hipotecas.items():
        print(f"  {opcion:<15}: {cuenta} ({cuenta / len(filas) * 100:.1f}%)")
else:
    print(f"No se ha encontrado el archivo {ruta_csv}")
