from SemillaAleatoria import *


LIM_M = 100 #lim de la pendiente

puntos1 = [[1, 0.42], [3, 0.75],[3.5, 1],[4, 0.42]]
puntos2 = [[.2, 0.1], [.5, 0.83],[.9,.4]]
puntos3 = [[15,.3], [25,.45],[30,.78], [34, 1], [40,0.85]]

print ("prueba de limite de b lineal")
print(calcular_bLineal(puntos1))

print ("prueba restriccion")
lim_m = 100
lim_b = 132.25
r = 80
print(restriccion(r, lim_m, 0))

print("prueba Z lineal")
m = .1863
b = .2369
print(Z_lineal(puntos1, m, b))

print("prueba Z gaussiana")
k = -0.1487
m = 3.5
print(Z_gaussiana(puntos1, k, m))

print("prueba generacion individuo:")
ind = generarIndividuoLineal(LIM_M, lim_b)
print(ind[0]) #m
print(ind[1]) #b
