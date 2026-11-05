'''
    input("scanner")
    CONCATENA siempre que se introduce un dato por teclado, el intérprete de python lo considera string
    ➜  clase /opt/homebrew/bin/python3 /Users/blanca/Python/curso_ML/clase/Agentic/ejercicios/02_conversiones.py
    Introduce un número: 3
    <class 'str'>
    Introduce otro número: 2 
    <class 'str'>
    Suma: 32
'''

numero1 = int(input("Introduce un número: "))
print(type(numero1))
numero2 = int(input("Introduce otro número: "))
print(type(numero2))
suma = numero1 + numero2
print("Suma:", suma)


# Convertir un str a número real (float(str))
lado = input("Introduce el lado del cuadrado :") # la parte decimal con .
area_cuadrado = float(lado) * float(lado)
area_cuadrado = float(lado) **2 # Al cuadrado
print("Area del cuadrado: ", area_cuadrado)

# Convertir un int a str. str(int)
# print("Suma:" + suma) # Type error
print("Suma:" + str(suma)) 

# convertir un booleano a numerico
# False = 0, True = 1
print(8 + False) # 8
print(8 + True) # 9
print(True + False) # 1

# Todos los tipos de dato es convertible a str
print(str(True))
print(str(4.67))
