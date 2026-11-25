"""
Ejercicio 23: Estudio de utilización de Airbnb en Madrid desde GitHub

Enunciado:
El objetivo de este trabajo es comprobar si se está utilizando la plataforma Airbnb por parte de empresas,
en lugar de particulares, para alquiler turístico en el centro de Madrid.

Apartado 1 (Fichero CSV en GitHub):
URL: https://gitfront.io/r/inboxdatascience/ae9DCzQ7R1Sc/pythonfiles/raw/madrid-airbnb-listings-apartado1.csv
- Extraer del fichero de alojamientos una lista con todos los alojamientos (cada uno como un diccionario
  con id, anfitrión, distrito, precio y plazas).
- Funciones a implementar:
  1. Contar el número de alojamientos en cada distrito.
  2. Filtrar alojamientos con capacidad >= número de ocupantes deseado.
  3. Obtener los 10 alojamientos más económicos de un distrito específico.
  4. Diccionario con cada anfitrión y el número de alojamientos que posee.

Apartado 6 (Fichero CSV en GitHub):
URL: https://gitfront.io/r/inboxdatascience/ae9DCzQ7R1Sc/pythonfiles/raw/madrid-airbnb-listings-apartado6.csv
- Extraer los alojamientos para procesar campos: id, anfitrion, url, tipo_alojamiento, distrito,
  precio, gastos_limpieza, plazas, noches_minimas, puntuacion y precio_persona.
- Funciones a implementar:
  1. Diccionario con tipos de alojamiento y sus porcentajes por distrito.
  2. Número de alojamientos por anfitrión en los distritos seleccionados (ordenados descendente).
  3. Promedio de plazas por anfitrión en cada distrito.
- Generar ficheros CSV de salida para cada apartado.

Autor: Blanca de Uña Martín
Curso: Machine Learning
"""

import os
import urllib.request
import csv

# Limpiar pantalla
os.system("cls" if os.name == "nt" else "clear")

URL_APARTADO_1 = "https://gitfront.io/r/inboxdatascience/ae9DCzQ7R1Sc/pythonfiles/raw/madrid-airbnb-listings-apartado1.csv"
URL_APARTADO_6 = "https://gitfront.io/r/inboxdatascience/ae9DCzQ7R1Sc/pythonfiles/raw/madrid-airbnb-listings-apartado6.csv"

def descargar_o_leer_csv(url: str, nombre_local: str):
    """Descarga el fichero si no existe en local o lo lee directamente."""
    ruta_local = os.path.join(os.path.dirname(os.path.abspath(__file__)), nombre_local)
    if not os.path.exists(ruta_local):
        print(f"Descargando {nombre_local} desde GitHub...")
        try:
            urllib.request.urlretrieve(url, ruta_local)
            print(f"Descargado con éxito: {nombre_local}")
        except Exception as e:
            print(f"No se pudo descargar automáticamente: {e}")
            return None
    return ruta_local

print("=== Ejercicio 23: Airbnb Madrid ===")
print("Consulte el enunciado completo en 'enunciado_airbnb_madrid.pdf'.")
print(f"URL Apartado 1: {URL_APARTADO_1}")
print(f"URL Apartado 6: {URL_APARTADO_6}")
