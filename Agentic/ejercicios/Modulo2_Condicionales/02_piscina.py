'''
    una piscina permite entrada a personas mayores de 18 años y menores de 65
    - solicita la edad por teclado
    - acceso permitido si está en rango de edad
    - lo siento, eres menor de 12 años
    - lo siento eres mayor de 65
'''
edad = int(input("Introduce tu edad: "))
permitido = "Bienvenido a la piscina"
denegado_12 = "Lo siento, eres menor de 12 años"
denegado_65 = "Lo siento, superas la edad permitida"
wellcome = "Bienvenido"

if edad >= 12 and edad <= 65:
    print({wellcome})
else:
    if edad < 12:
        print(denegado_12)
    if edad > 65: 
        print(denegado_65)
    
    
    