"""
Ejercicio 21: Formato tabular y procesamiento de temperaturas (ejercicio21.csv)

Enunciado:
1. Demostrar el uso de f-strings con modificadores de alineación y ancho fijo
   (< para izquierda, > para derecha, ^ para centrado) para formatear tablas en consola.
2. Leer el fichero 'ejercicio21.csv' con registros de temperaturas diarias por fecha y día de la semana.
3. Mostrar los datos tabulados limpiamente alineados por columnas.

Autor: Blanca de Uña Martín
Curso: Machine Learning
"""

import os

# Limpiar pantalla
os.system("cls" if os.name == "nt" else "clear")

# 1. Ejemplo de formateo con anchos fijos y alineación
print("=== Ejemplo de formato tabular con f-strings ===")
cabeceras_demo = ["Nombre", "Edad", "Puntuación"]
datos_demo = [
    ["Alice", 28, 95.5],
    ["Bob", 34, 88.0],
    ["Charlie", 22, 92.3],
    ["Miércoles", 22, 92.3],
]

print(f"{cabeceras_demo[0]:<12} {cabeceras_demo[1]:<6} {cabeceras_demo[2]:>12}")
print("-" * 32)
for fila in datos_demo:
    print(f"{fila[0]:<12} {fila[1]:<6} {fila[2]:>12.1f}")
print()

# 2. Lectura y representación de 'ejercicio21.csv'
ruta_directorio = os.path.dirname(os.path.abspath(__file__))
ruta_csv = os.path.join(ruta_directorio, "ejercicio21.csv")

if os.path.exists(ruta_csv):
    print("=== Lectura de 'ejercicio21.csv' con alineación tabular ===")
    encabezados = ["Fecha", "Día", "T1 (°C)", "T2 (°C)", "T3 (°C)", "T4 (°C)", "T5 (°C)"]
    print(f"{encabezados[0]:<12} {encabezados[1]:<12} {encabezados[2]:>9} {encabezados[3]:>9} {encabezados[4]:>9} {encabezados[5]:>9} {encabezados[6]:>9}")
    print("-" * 75)

    with open(ruta_csv, mode="r", encoding="utf-8-sig") as f:
        for linea in f:
            linea = linea.strip()
            if not linea:
                continue
            campos = linea.split(";")
            if len(campos) >= 7:
                fecha, dia, t1, t2, t3, t4, t5 = campos[:7]
                print(f"{fecha:<12} {dia:<12} {float(t1):>9.1f} {float(t2):>9.1f} {float(t3):>9.1f} {float(t4):>9.1f} {float(t5):>9.1f}")
