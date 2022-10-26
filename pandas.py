import pandas as pd
import numpy as np
from colorama import Fore
import random

# crear una  matriz de 2*3*5 con valores aleatorios enteros
a = np.random.randint(0, 100, (2, 3, 5))
# Crear una matriz de 2*3*5 con valores aleatorios 
g = np.random.random((2, 3, 5))
print(g)

print(Fore.YELLOW+"Matriz de  2*3*5:"+Fore.WHITE)
print(a)
print()
# crear una matriz de 5*2*3 con valores = 1
b = np.ones((5, 2, 3))
print(Fore.YELLOW+"Matriz de 5*2*3"+Fore.WHITE)
print(b)
# a y b tienen el mismo tamaño?
print()
print(Fore.YELLOW+"Vamos a ver si tienen el mismo tamaño"+Fore.WHITE,a.shape == b.shape)

# valores maximos minimos y medio de a
d_max = a.max()
d_min = a.min()
d_mean = a.mean()
print()
print(Fore.YELLOW+"Vamos a ver los valores maximos, minimos y el valor del medio"+Fore.WHITE,d_max, d_min, d_mean)

f = np.empty((2, 3, 5))
print(Fore.YELLOW+"Matriz vacia de 2*3*5"+Fore.WHITE)
print(f)

#Para cada valor en a, si es mayor que d_min pero menor que d_mean, asigne 25 al valor correspondiente en f.
#Si el valor es mayor o igual que d_mean pero menor que d_max, asigne 75 al valor correspondiente en f.
#Si el valor es igual a d_max, asigne 100 al valor correspondiente en f.
#Para todos los demás valores, asigne 0 al valor correspondiente en f.
for i in range(2):
    for j in range(3):
        for k in range(5):
            if a[i][j][k] > d_min and a[i][j][k] < d_mean:
                f[i][j][k] = 25
            elif a[i][j][k] >= d_mean and a[i][j][k] < d_max:
                f[i][j][k] = 75
            elif a[i][j][k] == d_max:
                f[i][j][k] = 100
            else:
                f[i][j][k] = 0


print()
print(Fore.YELLOW+"Matriz f:"+Fore.WHITE)
print(f)


