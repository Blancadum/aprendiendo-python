import os

os.system("cls")

# Los bucles son partes del programa que se repiten

# Podemos encontrarnos con dos tipos de bucles:

# Los bucles finitos o determinados: aquellos que se repiten un numero 
# fijo de veces. Se construyen con FOR.

# Los bucles no finitos o indeterminados: aquellos que se repiten un numero 
# variable de veces. Se construyen con WHILE.

# for (i=10; i>0; i--){
#    alert(i);
#    }



for i in range(10):
    print(i)

print("")

for i in range(10, 0, -1):
    print(i)
    
    
    # Resolucion del ejercicio 11
    
os.system("cls")

valor = 0

texto = ""
    
while valor <= 0:  

    valor = int(input("Escribe un numero entero positivo mayor que cero: "))


for i in range(valor):
    
    texto = texto + "* "
    
    
    
print(texto)



