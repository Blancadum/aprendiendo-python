
# Funcion convertir, le pasamos un NIF o NIE y nos devuelve el dato con la máscara



def convertir(valor):
  
    longitud = len(valor)

    if (longitud == 9):
        
        letra = valor[0:1]

        if (letra == "X") or (letra == "Y") or (letra == "Z"):
            mascara = valor[0:1] + "-" + valor[1:2] + "." + valor[2:5] + "." + valor[5:8] +"-" + valor[8:9]
        else:
            mascara = valor[0:2] + "." + valor[2:5] + "." + valor[5:8] +"-" + valor[8:9]

    else:
        
        mascara = "Dato no válido"

    return mascara
    



# Inicio del programa

cadena = input("Escribe un NIF o un NIE: ")

conversion = convertir(cadena)

print(conversion)
