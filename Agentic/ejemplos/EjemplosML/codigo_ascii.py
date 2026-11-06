
import os

os.system("cls")


while True: 

    clave = input("Escribe una contraseña minimo de 8 caracteres que tenga mayúsculas, minúsculas, numeros y simbolos: ")
    
    if len(clave) >= 8:
        
        clave_ascii = list()
        
        for i in range(len(clave)):
                clave_ascii.append(ord(clave[i]))
                
        break
   



print(clave)
print(clave_ascii)

numeros = 0
minusculas = 0
mayusculas = 0
simbolos = 0

for i in range(len(clave_ascii)):
    codigo = clave_ascii[i]
    
    # Uniendo minusculas y mayusculas

    if (codigo >= 48) and (codigo <= 57):
        numeros = numeros + 1
        
    elif ((codigo >= 65) and (codigo <= 90)) or (codigo == 154) or (codigo == 165) or (codigo == 181) or (codigo == 144) or (codigo == 214) or (codigo == 224) or (codigo == 233):
       mayusculas = mayusculas + 1
       
    elif ((codigo >= 97) and (codigo <= 122)) or (codigo == 129) or (codigo == 164) or ((codigo >= 160) and (codigo <= 163)) or (codigo == 130):
       minusculas = minusculas + 1
       
    else:
        simbolos = simbolos + 1
        

print("En la contraseña hay " + str(numeros) + " numeros, " + str(minusculas) + " minusculas," + str(mayusculas) + " mayusculas y " + str(simbolos) + " simbolos.")








# Ejemplo 2

valor = "51234567"

letra = valor[0:1]

numero2 = valor.replace(letra,"")

print(numero2)

print(letra)

numero = valor[1:8]

print(numero)


codigo = ord(letra)

print(codigo)

if (codigo >= 48) and (codigo <= 57):
    print ("Es un numero")
elif (codigo >= 65) and (codigo <= 90) or (codigo == 165):
    print ("Es una letra mayuscula")
elif (codigo >= 97) and (codigo <= 122) or (codigo == 164):
    print ("Es una letra minuscula")
elif (codigo >= 160) and (codigo <= 163) or (codigo == 130):
    print ("es una vocal acentuada minúscula")
elif (codigo == 181) or (codigo == 144) or (codigo == 214) or (codigo == 224) or (codigo == 233):
    print ("es una vocal acentuada mayúscula")
else:
    print ("Es un simbolo")
    
