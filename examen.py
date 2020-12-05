from SemillaAleatoria import *
puntos = [[1, 0.42], [3, 0.75],[3.5, 1],[4, 0.42]]

print ("prueba de limite de b lineal")
print(calcular_bLineal(puntos))

print ("prueba restriccion")
lim_m = 100
lim_b = 132.5
r = 80
print(restriccion(r, lim_m, 0))

print("prueba Z lineal")
m = .1863
b = .2369
print(Z_lineal(puntos, m, b))

print("prueba Z gaussiana")
k = -0.1487
m = 3.5
print(Z_gaussiana(puntos, k, m))