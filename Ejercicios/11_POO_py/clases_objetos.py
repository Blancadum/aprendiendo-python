"""
"""

class Persona: 
    # En Python, solo se permite un constructor por clase
    def __init__ (self, nombre, edad):
        # Crear propiedades, atributos, campos, variables de instancia
        # self es un puntero, se apunta a si mismo
        # Es el equivalente a this en java
        
        self.nombre = nombre
        self.edad = edad
        

    # Se pueden crear más constructores si se define un constructor por defecto
    def __init__ (self):
        pass

# Crear un objeto de persona

persona = Persona()
persona1 = Persona("Maria", 35)
persona2 = Persona("Pedro", 42)

print(persona)
print(persona1)
print(persona2)

