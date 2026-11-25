"""
Enunciado:
Demostración de cómo forzar y lanzar excepciones controladas mediante 'raise'.
Definir una función 'solicitar_edad' que pida la edad al usuario.
Si la edad introducida es menor que cero, lanzar una excepción personalizada
con el mensaje "La edad no puede ser negativa".

Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo 11_Excepciones
"""


def solicitar_edad():
    edad = int(input("Introduce tu edad: "))
    if edad < 0:
        # Lanzamos manualmente una excepción usando 'raise'
        raise Exception("La edad no puede ser negativa")
    else:
        return edad


try:
    edad = solicitar_edad()
except Exception as ex:
    print("Error detectado:", ex)
else:
    print("Edad del usuario:", edad)
