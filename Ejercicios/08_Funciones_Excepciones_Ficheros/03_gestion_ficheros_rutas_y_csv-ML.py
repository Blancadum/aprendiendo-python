"""
Actividad: Manejo de rutas y lectura/escritura de ficheros

Descripción:
Demuestra el uso de la librería 'os' (os.path.join, os.path.abspath, os.getcwd)
para gestionar rutas absolutas y relativas de archivos en el sistema,
y la lectura/procesamiento línea a línea de datos procedentes de un archivo tabular.

Autor: Blanca de Uña Martín
Curso: Machine Learning
"""

# Para indicar el lugar donde se encuentra el fichero
import os   # Libreria para trabajar con metodos del sistema operativo

# Opcion 1
carpeta = "C:/Machine Learning/ejemplos/ficheros/"
fichero = "base_coches.csv"
ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)

# Opcion 2
ruta2 = os.getcwd()

os.system("cls")
# Para pasar cada línea de un fichero a un array
datos = list()  # Inicializamos la tabla de destino
# Método 1 para abrir archivos
archivo = open("C:/Machine Learning/ejemplos/ficheros/base_coches.csv", mode="r")
contenido=archivo.readlines()
archivo.close()             # Es obligatorio cerrar SIEMPRE el fichero
tamanyo = len(contenido)    # Contamos cuantas lineas tiene el fichero

# Variante 1, usando range(len)
for linea in range(len(contenido)):
    columnas = contenido[linea].count("\t")          # Contamos cuantos campos tiene el fichero
    registro = contenido[linea].replace("\n", "")
    datos.append(registro.split("\t"))
datos.clear()           # Borramos el contenido para usar la variante siguiente

# Variante 2, usando enumerate()
for indice, linea in enumerate(contenido):
    columnas = linea.count("\t")
    registro = linea.replace("\n", "")
    datos.append(registro.split("\t"))

datos.clear()           # Borramos el contenido para usar la variante siguiente

# Variante 3, usando el nombre del array directamente:
for linea in contenido:
    columnas = linea.count("\t")
    registro = linea.replace("\n", "")
    datos.append(registro.split("\t"))
datos.clear()           # Borramos el contenido para usar el metodo siguiente

# Método 2 para abrir archivos
with open(carpeta + "base_coches.csv", mode="r") as archivo:
    contenido=archivo.readlines()
    datos.append(['Marca', 'Modelo', 'Año', 'Color', 'Matricula'])
    for linea in contenido:
        columnas = linea.count("\t")
        registro = linea.replace('\n', '')
        datos.append(registro.split("\t"))

filas = len(contenido)          # Contamos cuantas filas tiene el fichero
columnas += 1                   # Numero de columnas con ajuste
filas = len(datos)              # Contamos cuantas filas tiene la tabla
columnas = len(datos[0])        # Contamos cuantas columnas tiene la tabla
print(datos)                    # Dibujo de la tabla sin orden ninguno
print()
for i in range(filas):          # Podemos dibujar asi el contenido del array
    linea = "\t"
    for j in range(columnas):
        linea = linea + str(datos[i][j]) + "\t"
    print(linea)

# Ejemplo de búsqueda: quiero saber cuantos Seat hay en la tabla de datos
cantidad = 0
for i in range(filas):
    if (i>0):                   # Podemos descartar la cabecera empezando desde 1
        if (datos[i][0]=="Seat"):
            cantidad += 1
salida1 = ("Hay " + str(cantidad) + " coches Seat en la tabla")
# Ejemplo de búsqueda: quiero saber cuantos coches hay del 2007 en la tabla de datos
cantidad = 0
for i in range(filas):
    if (i>0):                       # Podemos descartar la cabecera empezando desde 1
        if (datos[i][2]=="2007"):
            cantidad += 1
salida2 = ("Hay " + str(cantidad) + " coches matriculados en 2007")
# Ejemplo de búsqueda: quiero saber cuantos coches azules hay en la tabla de datos
cantidad = 0
for i in range(1, filas, 1):            # Podemos descartar la cabecera empezando desde 1
    if (datos[i][3]=="Azul"):
        cantidad += 1
salida3 = ("Hay " + str(cantidad) + " coches azules")

print("\n" + salida1 + "\n" + salida2 + "\n" + salida3)
# Modos de apertura de ficheros:
#
#   read        mode="r"    Fichero de solo lectura
#   create      mode="x"    Creación de nuevo fichero
#   escritura   mode="w"    Creación y escritura en un fichero
#   añadir      mode="a"    Añade a un fichero creado

with open(carpeta + "mensajes.txt", mode="w") as mensaje:
    mensaje.write(salida1)
with open(carpeta + "mensajes.txt", mode="a") as mensaje:
    mensaje.write("\n" + salida2)
    mensaje.write("\n" + salida3)
with open(carpeta + "mensajes.txt", mode="a") as mensaje:
    mensaje.write("\n\n")
    for i in range(filas):       # Podemos dibujar asi el contenido de la tabla
        linea = ""
        for j in range(columnas):
            linea = linea + str(datos[i][j])
            if (j < columnas):
                linea = linea + "\t"
        mensaje.write(linea + "\n")
