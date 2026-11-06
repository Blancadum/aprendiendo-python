def main():
    asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
    suspensos = []

    for asignatura in asignaturas:
        while True:
            try:
                nota_str = input(f"¿Qué nota has sacado en {asignatura}? ")
                nota = float(nota_str)
                if 0 <= nota <= 10:
                    if nota < 5:  # Asumimos que se aprueba con 5
                        suspensos.append(asignatura)
                    break
                else:
                    print("La nota debe estar entre 0 y 10. Inténtalo de nuevo.")
            except ValueError:
                print("Valor no válido. Introduce un número entre 0 y 10.")

    if len(suspensos) == 0:
        print("Has aprobado todo, pasas al curso siguiente")
    else:
        # Se puede dar formato a la lista de asignaturas separada por comas
        asignaturas_suspensas = ", ".join(suspensos)
        print(f"Debes repetir {asignaturas_suspensas}")

if __name__ == "__main__":
    main()
