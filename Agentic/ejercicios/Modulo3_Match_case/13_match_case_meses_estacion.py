'''
    solicitar al usuraio un número del 1 al 12
    mostrar a qué estación del año pertenece: 
    - Diciembre, enero y febrero: Invierno
    - marzo, abril, mayo: primavera
    - junio, julio, agosto: verano
    - septiembre, octubre y noviembre: otoño
'''

numero = input("Escribe un número del mes: (1 - 12): ")


match numero:
    case "12" | "1" | "2":
        print("Invierno")
    case "3"  | "4" | "5":
        print("Primavera")
    case "6"  | "7" | "8":
        print("Verano")
    case "9" | "10" | "11":
        print("Otoño")

    case _:
        print("No es un mes válido")
        