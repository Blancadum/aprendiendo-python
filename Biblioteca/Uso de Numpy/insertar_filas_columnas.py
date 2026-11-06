import numpy as np

tabla = np.zeros((4,3))

print(tabla)
# [[0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]]   
print()
print(tabla.shape)
# (4, 3) # dimensiones de matriz en forma de tupla


tabla = np.insert(tabla, tabla.shape[0], np.array((20, 20, 20)), axis=0)

# 0 o tambien axis=0
# se agrega a la ultima fila a.shape[0]
# para denotar fila se usa cero (0) axis = 0
print()
print(tabla)
# [[ 0.  0.  0.]
#  [ 0.  0.  0.]
#  [ 0.  0.  0.]
#  [ 0.  0.  0.]
#  [20. 20. 20.]]


tabla = np.insert(tabla, tabla.shape[1], np.array((10, 10, 10, 10, 10)), axis=1)

# 1 o tambien axis=1
# se agrega a la ultima columna a.shape[1]
# para denotar columna se usa uno (1) axis = 1
print()
print(tabla)
# [[ 0.  0.  0. 10.]
#  [ 0.  0.  0. 10.]
#  [ 0.  0.  0. 10.]
#  [ 0.  0.  0. 10.]
#  [20. 20. 20. 10.]]

