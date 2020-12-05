from SemillaAleatoria import *
LIM_M = 100 #lim de la pendiente
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

print("prueba generacion individuo:")
ind = generarIndividuoLineal(LIM_M, lim_b)
print(ind[0]) #m
print(ind[1]) #b

#iteracion 1
	#generar poblacion con 100 individuos, calcularle su Z 
	#ver en esa poblacion el de Mayor Z y guardarlo

print("\npoblacion 1")
poblacion = [] 
mejorZ = -999999
mejorM = 0
mejorB = 0
idVector = 0
pob = 0
for j in range(1000):
	mejorZPob = -999999
	mejorMPob = 0
	mejorBPob = 0
	idVectorPob = 0
	for i in range(1000):
		propuestas = generarIndividuoLineal(LIM_M, lim_b)
		z = Z_lineal(puntos, propuestas[0], propuestas[1])
		if(z > mejorZPob):
			mejorZPob = z
			mejorMPob = propuestas[0]
			mejorBPob = propuestas[1]
			idVectorPob = i
	print("Mejor vector de poblacion ",j,":", idVectorPob, mejorMPob, mejorBPob, mejorZPob)
	if(mejorZPob > mejorZ):
		mejorZ = mejorZPob
		mejorM = mejorMPob
		mejorB = mejorBPob
		idVector = idVectorPob
		pob = j
print("MEJOR poblacoin",pob,", vector", idVector,": m=",mejorM, ", b=",mejorB, "Z=", mejorZ)