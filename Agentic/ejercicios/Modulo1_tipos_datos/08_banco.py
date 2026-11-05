'''
    Una persona tiene en su cuenta 1250€
     - Recibe una transferencia de 357€
     - Paga 3 facturas de 85€ cada una
     - Recibe un bizum de 200€
     - retira el 10% de su saldo (necesitaréis otra variable)
    Mostrar saldo final
'''

saldo = 1250
saldo += 375
saldo -= 3*85
saldo += 200
retiro = saldo * 10 / 100
saldo -= retiro


print(f"El saldo final es: {int(saldo)}")
print("Saldo Final:", int(saldo))
print("Saldo Final:", (saldo))