
            # Para indicar el lugar donde se encuentra el fichero

import os   # Libreria para trabajar con metodos del sistema operativo
from os import system

os.system('cls' if os.name == 'nt' else 'clear')

current_folder = os.path.dirname(os.path.abspath(__file__))


import random
import pandas as pd
import matplotlib.pyplot as plt

# Ejemplo de aplicación de Matplotlib a una lista 
# Escribir un programa que pregunte al usuario por un rango de años, genere una cantidad
# de ventas de forma aleatoria de 0 a 100 redondeando a 2 decimales

# El programa mostrará el contenido de la lista un diagrama de líneas con la evolución de las ventas.

# Preguntamos por el año inicial
inicio = int(input('Introduce el año inicial: '))

# Preguntamos por el año final
final = int(input('Introduce el año final: '))

# Reordenamos los años si no están bien colocados

if (inicio > final):
    cambio = final
    final = inicio
    inicio = cambio

# Definimos un diccionario vacío para guardar las ventas de cada año

ventas = {}

# Bucle iterativo para preguntar las ventas de cada año y guardarlas en el diccionario
# Configuramos i como indice usando los años desde el año de inicio hasta el año final
# Debemos usar final+1 para que añada el último 

for i in range(inicio, final+1):

    # Preguntamos por las ventas del año i y las guardamos en el diccionario con la clave el año y el valor las ventas
    
    #ventas[i] = float(input('Introduce las ventas del año ' + str(i) +': '))

    ventas[i] = round(random.uniform(0,100),2)


#ventas = pd.Series(ventas, dtype='float')

print(ventas)


# Definimos la figura y los ejes del gráfico con Matplotlib
    
fig, grafico = plt.subplots()



print("\n1-Dispersion\n2-Lineas\n3-Areas\n4-Barras Verticales\n5-Barras Horizontales\n")

eleccion = int(input("Elige el gráfico que quieres mostrar (1-5): "))
color = input("Elige el color del gráfico: ")

# Dibujamos los puntos con las ventas a partir del diccionario
# Usamos el índice (años) para el eje X y los valores para el eje Y




match (eleccion):

    case 1: 
   
        grafico.scatter(ventas.keys(), ventas.values(), color = color)

    case 2: 
   
        grafico.plot(ventas.keys(), ventas.values(), color = color)


    case 3: 
   
        grafico.fill_between(ventas.keys(), ventas.values(), color = color)

    case 4: 
   
        grafico.bar(ventas.keys(), ventas.values(), color = color)

    case 5: 
   
        grafico.barh(list(ventas.keys()), list(ventas.values()), color = color)

    case _:
        print("No has elegido un gráfico de la lista")


if (eleccion >= 1) and (eleccion <= 5):

    # Guardamos el gráfico en una carpeta

    plt.savefig('diagrama.png')

    # Mostramos el gráfico por pantalla

    plt.show()
    