from SemillaAleatoria import *

print ("prueba restriccion")
lim_m = 100
lim_b = 132.5
r = 80
print(restriccion(r, lim_m, 0))
print("prueba Z")
puntos = [[1, 0.42], [3, 0.75],[3.5, 1],[4, 0.42]]
m = -82.67716535
b = 54.55882353
print(Z(puntos, m, b))