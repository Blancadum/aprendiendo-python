"""
Enunciado:
Ejemplo del banco con control de excepciones y uso de variable global:
- Partimos de un saldo inicial de 1000 euros.
- Creamos una función retirar(importe) que descuenta la cantidad del saldo.
- Si el importe a retirar es superior al saldo disponible, lanzar una excepción
  con el mensaje "No tienes saldo suficiente".
- Usar 'global saldo' dentro de la función para permitir la reasignación de la
  variable definida fuera de su ámbito local.

Autor: Blanca de Uña Martín
Curso: Python Agentic - Modulo 11_Excepciones
"""

saldo = 1000  # Saldo global inicial


def retirar(importe):
    # 'global saldo' permite modificar la variable saldo del ámbito global.
    # Sin esta declaración, Python lanzaría UnboundLocalError al intentar reasignar
    # saldo en 'saldo -= importe'.
    global saldo

    if importe > saldo:
        raise Exception("No tienes saldo suficiente")
    else:
        saldo -= importe


try:
    print("Intentando retirar 1200 euros...")
    retirar(1200)

except Exception as ex:
    print("Operación denegada:", ex)

else:
    print("Retirada completada con éxito.")

finally:
    print("Saldo actual en cuenta:", saldo)
