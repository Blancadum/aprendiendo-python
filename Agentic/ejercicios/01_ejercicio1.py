'''
    # numero1 = int(input("Introduce un número:"))
    Solicitar al usuario estos tres datos: nombre, apellido y la edad
    mostrar un mensaje de bienvenida con esos datos
'''
nombre = input("Introduce tu nombre: ")
apellido = input("Introduce tu apellido: ")
edad = input("Introduce tu edad: ")

print("Bienvenida al curso, " + nombre + " " + apellido + ". Tienes " + edad + " años.")
# otra forma de mostrar información: f"literal {variable}""
print(f"Bienvenido {nombre} {apellido} y tienes {edad} años")