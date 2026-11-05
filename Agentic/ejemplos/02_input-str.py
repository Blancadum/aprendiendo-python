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

numero1 = input("Introduce un número: ")
print(type(numero1))
numero2 = input("Introduce otro número: ")
print(type(numero2))
suma = numero1 + numero2
print("Suma:", suma)
