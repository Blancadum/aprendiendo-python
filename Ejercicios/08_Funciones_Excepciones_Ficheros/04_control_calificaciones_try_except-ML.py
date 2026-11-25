"""
Ejercicio 16: Control de calificaciones y asignaturas suspensas

Descripción:
Solicita al usuario la nota obtenida en cinco asignaturas (Matemáticas, Física,
Química, Historia y Lengua) validando que estén entre 0 y 10 con control de
errores try/except. Al final, informa si aprueba el curso completo (todas >= 5)
o lista las materias que debe repetir.

Autor: Blanca de Uña Martín
Curso: Machine Learning
"""

# Importación de la librería 'os' para interactuar con comandos del sistema operativo
import os

# Limpiar la pantalla de la terminal (usa 'clear' para Mac/Linux y 'cls' para Windows)
# Permite tener una consola limpia antes de ejecutar el programa
os.system("clear")

# Ejercicio 16.- Control de calificaciones y asignaturas suspensas
# Solicita al usuario la nota de 5 materias (Matemáticas, Física, Química, Historia y Lengua).
# Valida mediante try-except que las notas sean numéricas y pertenezcan al rango [0, 10].
# Al final, informa si se aprueba el curso completo o indica qué asignaturas se deben repetir.

def main():
    # 1. Lista de asignaturas y lista acumuladora de suspensos
    asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
    suspensos = []

    print("=== INTRODUCCIÓN DE CALIFICACIONES (0 a 10) ===")
    print()

    # 2. Recorrer cada asignatura pidiendo y validando la nota
    for asignatura in asignaturas:
        while True:
            try:
                nota_str = input(f"¿Qué nota has sacado en {asignatura}? ")
                nota = float(nota_str)

# Validación de rango de nota permitido
                if 0 <= nota <= 10:
                    if nota < 5:  # Consideramos suspenso si la calificación es menor a 5
                        suspensos.append(asignatura)
                    break
                else:
                    print("  -> Error: La nota debe estar entre 0 y 10. Inténtalo de nuevo.")
            except ValueError:
# Se captura el error si el usuario introduce letras o caracteres no numéricos
                print("  -> Error: Entrada no válida. Introduce un número decimal o entero.")

    # 3. Evaluación final del curso
    print()
    print("--- RESULTADO ACADÉMICO ---")
    if len(suspensos) == 0:
        print("🎉 ¡Enhorabuena! Has aprobado todas las asignaturas y pasas al curso siguiente.")
    else:
# Formateamos la lista de suspensos separada por comas usando .join()
        asignaturas_suspensas = ", ".join(suspensos)
        print(f"⚠️ Debes repetir las siguientes asignaturas: {asignaturas_suspensas}")

if __name__ == "__main__":
    main()
