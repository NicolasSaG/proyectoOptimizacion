from SemillaAleatoria import *

LIM_M = 100 #lim de la pendiente
LIM_TIEMPO = 30 #lim de ejecucion en segundos

puntos1 = [[1, 0.42], [3, 0.75],[3.5, 1],[4, 0.42]]
puntos2 = [[.2, 0.1], [.5, 0.83],[.9,.4]]
puntos3 = [[15,.3], [25,.45],[30,.78], [34, 1], [40,0.85]]

#almanecar mejores globales
mejorZ = 10000
mejorM = 0
mejorB = 0
idVector = 0
pob = 0
lim_b = calcular_bLineal(puntos1)
print("limites de b: [",-lim_b,",",lim_b,"]")

#generacion de semilla
random.seed(generarSemillaAleatoria()) 

inicioTiempo = obtenerTiempo()
finTiempo = 0
for j in range(100):
	#mejores de cada poblacion
	mejorZPob = 10000
	mejorMPob = 0
	mejorBPob = 0
	idVectorPob = 0
	for i in range(1000):
		propuestas = generarIndividuoLineal(LIM_M, lim_b) #generacion de individuo
		z = Z_lineal(puntos1, propuestas[0], propuestas[1]) #calculo de f.o. con los valores del individuo
		if(z < mejorZPob): #comparacion con el mejor actual de la poblacion
			mejorZPob = z
			mejorMPob = propuestas[0]
			mejorBPob = propuestas[1]
			idVectorPob = i
		#terminar si se pasa de 30 segundos
		finTiempo = obtenerTiempo()
		if(finTiempo - inicioTiempo > 30):
			break
	#print("Mejor vector de poblacion ",j,":", idVectorPob, mejorMPob, mejorBPob, mejorZPob)
	if(mejorZPob < mejorZ): #comparacion con el mejor actual de la iteraciones
		mejorZ = mejorZPob
		mejorM = mejorMPob
		mejorB = mejorBPob
		idVector = idVectorPob
		pob = j
	if(finTiempo - inicioTiempo > 30):
    		print("Me quede en la poblacion: ", j, ", individuo: ", i)
		break	

print("tiempo de ejecucion: ", finTiempo - inicioTiempo, "s")
print("MEJOR poblacion",pob,", vector", idVector,": m=",mejorM, ", b=",mejorB, "Z=", mejorZ)
#Funcion gaussiana


print("Limite b",lim_b)
print("Funcion gaussiana: ")
poblacion = [] 
mejorZ = 10000
mejorM=Mayor(puntos1)
mejorK = 0
idVector = 0
pob = 0
infe=0
supe=5
for j in range(1000):
	mejorZPob = 10000
	mejorKPob = 0
	idVectorPob = 0
	rango=1
	for i in range(1000):
		propuestas = generarIndividuoGauss(infe,supe)
		z = Z_gaussiana(puntos1, propuestas, mejorM)
		if(z < mejorZPob):
			mejorZPob = z
			mejorKPob = propuestas	
			supe=mejorKPob+rango
			infe=mejorKPob-rango
			idVectorPob = i
		rango=rango/10
	#print("Mejor vector de poblacion ",j,":", idVectorPob, -mejorKPob, bbmejorZPob)
	if(mejorZPob < mejorZ):
		mejorZ = mejorZPob
		mejorK = mejorKPob
		idVector = idVectorPob
		pob = j

print("MEJOR poblacion",pob,", vector", idVector,": m=",-mejorM, ", K=",-mejorK, "Z=", mejorZ)
