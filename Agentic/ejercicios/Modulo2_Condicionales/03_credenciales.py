'''
    Solicitar usaurio y password por teclado
    - si el usuario es "admin" y el password es "python123"
    - Mostrar "credenciales no válidas" o "credenciales correctas"
'''
user = input("Introduce tu usuario: ")
password = input("Introduce tu contraseña: ")
acceso_permitido = "Credenciales correctas"
acceso_denegado = "Credenciales incorrectas"

if user == "admin" and password == "python123":
    print(acceso_permitido)

if user != "admin" and password != "python123":
    print(acceso_denegado)