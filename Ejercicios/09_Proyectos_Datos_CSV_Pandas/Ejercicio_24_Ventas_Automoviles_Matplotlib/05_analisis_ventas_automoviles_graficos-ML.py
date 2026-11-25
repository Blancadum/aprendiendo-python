"""
Ejercicio 24: Análisis de ventas de automóviles y representación gráfica (coches.csv)

Enunciado:
El fichero 'coches.csv' contiene información sobre modelos de automóviles vendidos en EE.UU. (Marca, Modelo, Tipo, Potencia, Precio en dólares).

I. Análisis y transformación de datos:
1. Cargar el fichero y eliminar filas con valores desconocidos o incompletos.
2. Calcular el precio en euros aplicando el tipo de cambio (1 $ = 0.94 €).
3. Mostrar por pantalla las 10 últimas filas.
4. Mostrar por pantalla el número de marcas distintas.
5. Mostrar por pantalla el número de modelos de cada marca, ordenado de mayor a menor frecuencia.
6. Mostrar la marca y el modelo del coche más caro.
7. Mostrar el precio medio en euros agrupado por marca, ordenado de menor a mayor precio.

II. Representación gráfica (Matplotlib):
1. Gráfico de barras verticales: Porcentaje de modelos por marca (color fondo '#0dbb75', borde '#df7312', con título y etiquetas de ejes). Guardar como 'diagrama24_linea.png'.
2. Gráfico de dispersión: Potencia vs Precio (color '#5112df', marcador triángulo '^'). Guardar como 'diagrama24_dispersion.png'.
3. Generar un fichero ZIP con los diagramas y el código.

Autor: Blanca de Uña Martín
Curso: Machine Learning
"""

import os
import csv
from collections import Counter, defaultdict

# Limpiar pantalla
os.system("cls" if os.name == "nt" else "clear")

ruta_dir = os.path.dirname(os.path.abspath(__file__))
ruta_csv = os.path.join(ruta_dir, "coches.csv")

if not os.path.exists(ruta_csv):
    print(f"No se encuentra el archivo {ruta_csv}")
    exit()

# I. Lectura y limpieza
datos = []
TIPO_CAMBIO_DOLAR_EURO = 0.94

with open(ruta_csv, mode="r", encoding="utf-8-sig") as f:
    lector = csv.DictReader(f, delimiter=";")
    for fila in lector:
        # Validar valores completos
        if not fila.get("Marca") or not fila.get("Precio") or not fila.get("Potencia"):
            continue
        try:
            precio_usd = float(fila["Precio"])
            potencia = float(fila["Potencia"])
            precio_eur = round(precio_usd * TIPO_CAMBIO_DOLAR_EURO, 2)
            fila["Precio_EUR"] = precio_eur
            fila["Potencia_num"] = potencia
            fila["Precio_USD_num"] = precio_usd
            datos.append(fila)
        except ValueError:
            continue

print(f"Número de registros válidos tras limpieza: {len(datos)}")

# Últimas 10 filas
print("\n=== Últimas 10 filas ===")
for reg in datos[-10:]:
    print(f"{reg['Marca']} {reg['Modelo']} | Tipo: {reg['Tipo']} | Potencia: {reg['Potencia_num']} CV | Precio: {reg['Precio_EUR']} €")

# Número de marcas y modelos por marca
marcas = Counter(r["Marca"] for r in datos)
print(f"\nNúmero de marcas distintas: {len(marcas)}")
print("\n=== Modelos por marca (de mayor a menor) ===")
for marca, cuenta in marcas.most_common():
    print(f"  {marca:<15}: {cuenta} modelos")

# Coche más caro
coche_mas_caro = max(datos, key=lambda x: x["Precio_EUR"])
print(f"\nCoche más caro: {coche_mas_caro['Marca']} {coche_mas_caro['Modelo']} ({coche_mas_caro['Precio_EUR']} € / {coche_mas_caro['Precio_USD_num']} $)")

# Precio medio por marca
precios_por_marca = defaultdict(list)
for r in datos:
    precios_por_marca[r["Marca"]].append(r["Precio_EUR"])

medias_marca = {m: sum(precios) / len(precios) for m, precios in precios_por_marca.items()}
medias_ordenadas = sorted(medias_marca.items(), key=lambda x: x[1])

print("\n=== Precio medio en euros por marca (ordenado de menor a mayor) ===")
for marca, media in medias_ordenadas:
    print(f"  {marca:<15}: {media:.2f} €")

# II. Gráficos con Matplotlib (si está disponible)
try:
    import matplotlib.pyplot as plt

    # Gráfico 1: Barras
    top_marcas = marcas.most_common(15)
    nombres_marcas = [m[0] for m in top_marcas]
    porcentajes = [(m[1] / len(datos)) * 100 for m in top_marcas]

    plt.figure(figsize=(12, 6))
    plt.bar(nombres_marcas, porcentajes, color="#0dbb75", edgecolor="#df7312", linewidth=1.5)
    plt.title("Porcentaje de Modelos por Marca (Top 15)", fontsize=14)
    plt.xlabel("Marca", fontsize=12)
    plt.ylabel("Porcentaje (%)", fontsize=12)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    ruta_g1 = os.path.join(ruta_dir, "diagrama24_linea.png")
    plt.savefig(ruta_g1)
    plt.close()
    print(f"\n[OK] Gráfico de barras guardado en: {ruta_g1}")

    # Gráfico 2: Dispersión Potencia vs Precio
    potencias = [r["Potencia_num"] for r in datos]
    precios_e = [r["Precio_EUR"] for r in datos]

    plt.figure(figsize=(10, 6))
    plt.scatter(potencias, precios_e, color="#5112df", marker="^", alpha=0.7)
    plt.title("Relación Potencia vs Precio", fontsize=14)
    plt.xlabel("Potencia (CV)", fontsize=12)
    plt.ylabel("Precio (€)", fontsize=12)
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    ruta_g2 = os.path.join(ruta_dir, "diagrama24_dispersion.png")
    plt.savefig(ruta_g2)
    plt.close()
    print(f"[OK] Gráfico de dispersión guardado en: {ruta_g2}")

except ImportError:
    print("\nNota: Para generar los diagramas gráficos instale matplotlib ('pip install matplotlib').")
