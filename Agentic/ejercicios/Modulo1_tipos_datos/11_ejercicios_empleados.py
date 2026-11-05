'''
    Tenemos 3 empleados hablando de sus sueldos
    - el empleado 1 cobra 1800
    - el empleado 2 cobra 2100
    - el empleado 3 cobra 1800
    - mostrar si el empleado 1 cobra más que el empleado 2
    - si el empleado 2 cobra más que el empleado 3
    - si el empleado 1 cobra lo mismo que el empleado 3
    - si el sueldo del empleado 2 es distinto del sueldo del empleado 1
    - si el sueldo del empleado 3 es menor o igual que el del empleado 1
'''

empleado1 = 1800
empleado2 = 2100
empleado3 = 1800

print("¿El empleado 1 cobra más que el empleado 2?: ", (empleado1 > empleado2)) # True
print("¿El empleado 2 cobra más que el empleado 3?: ", (empleado2 > empleado3)) #True
print("¿Empleado 1 cobra lo mismo que el empleado 3?: ", (empleado1 == empleado3)) #True
print("¿Empleado 2 cobra distinto que el empleado 1:", (empleado2 != empleado1)) #True
print("¿Empleado 3 es menor o igual que el empleado 1?: ", (empleado2 <= empleado1)) #True