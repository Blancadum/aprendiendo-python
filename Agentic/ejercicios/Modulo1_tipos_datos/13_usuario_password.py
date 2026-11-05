'''
    Solicitar usuario y password por teclado
    - Mostrar si el usuario es "admin" y el password "python123"
'''

user = input("introduce usuario: ")
password = input("introduce contraseña: ")

print("¿El usuario es admin?", user == "admin" and password == "python123" )
print("¿La contraseña es python123?", password == "python123" ) 
print("Credenciales son válidas?", user == "admin" and password == "python123")