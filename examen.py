from SemillaAleatoria import *
import ManejoArchivo as archivo

LIM_M = 100 #lim de la pendiente
LIM_TIEMPO = 30 #lim de ejecucion en segundos

#Ingreso de puntos#
print("Porfavor ingrese una ruta valida para obtener los puntos a usar :)")
ruta=input()
puntos = archivo.LecturaArchivo(ruta).tolist()
print(puntos)

print("Numero de iteraciones (1 a 100):")
num_iteraciones = int(input())

print("Tamano de la poblacion (se recomienda 1000):")
tam_poblacion = int(input())



lim_b = calcular_bLineal(puntos)
print("limites de b: [",-lim_b,",",lim_b,"]")

#generacion de semilla
random.seed(generarSemillaAleatoria()) 

#almanecar mejores globales
mejorZ = 10000
mejorM = 0
mejorB = 0
idVector = 0
pob = 0
inicioTiempo = obtenerTiempo()
finTiempo = 0
for j in range(num_iteraciones):
	#mejores de cada poblacion
	mejorZPob = 100000
	mejorMPob = 0
	mejorBPob = 0
	idVectorPob = 0
	for i in range(tam_poblacion):
		propuestas = generarIndividuoLineal(LIM_M, lim_b) #generacion de individuo
		z = Z_lineal(puntos, propuestas[0], propuestas[1]) #calculo de f.o. con los valores del individuo
		if(z < mejorZPob): #comparacion con el mejor actual de la poblacion
			mejorZPob = z
			mejorMPob = propuestas[0]
			mejorBPob = propuestas[1]
			idVectorPob = i
		#terminar si se pasa de 30 segundos
		finTiempo = obtenerTiempo()
		if(finTiempo - inicioTiempo > LIM_TIEMPO):
			print("Me quede en la poblacion: {}  individuo: {}".format(j,i))
			break
	print("El mejor de poblacion {}, vector {}:, m={}, b={}, Z={}".format(j, idVectorPob, mejorMPob, mejorBPob, mejorZPob))
	if(mejorZPob < mejorZ): #comparacion con el mejor actual de la iteraciones
		mejorZ = mejorZPob
		mejorM = mejorMPob
		mejorB = mejorBPob
		idVector = idVectorPob
		pob = j
	if(finTiempo - inicioTiempo > LIM_TIEMPO):
		print("Me quede en la poblacion: {}  individuo: {}".format(j,i))
		break	

print("tiempo de ejecucion: ", finTiempo - inicioTiempo, "s")
print("MEJOR GLOBAL poblacion {}, vector {}:, m={}, b={}, Z={}".format(pob, idVector,mejorM,mejorB,mejorZ))

#Funcion gaussiana
print("Funcion gaussiana: ")
mejorZ = 10000
mejorM=Mayor(puntos)
mejorK = 0
idVector = 0
pob = 0
infe=0
supe=5
for j in range(num_iteraciones):
	mejorZPob = 10000
	mejorKPob = 0
	idVectorPob = 0
	rango=1
	for i in range(tam_poblacion):
		propuestas = generarIndividuoGauss(infe,supe)
		z = Z_gaussiana(puntos, propuestas, mejorM)
		if(z < mejorZPob):
			mejorZPob = z
			mejorKPob = propuestas	
			supe=mejorKPob+rango
			infe=mejorKPob-rango
			idVectorPob = i
		rango=rango/10
		finTiempo = obtenerTiempo()
		if(finTiempo - inicioTiempo > LIM_TIEMPO):
			print("Me quede en la poblacion: {}  individuo: {}".format(j,i))
			break
	print("El mejor de poblacion {}, vector {}:, m={} k={} Z={}".format(j, idVectorPob,mejorM, mejorKPob, mejorZPob))
	if(mejorZPob < mejorZ):
		mejorZ = mejorZPob
		mejorK = mejorKPob
		idVector = idVectorPob
		pob = j
	if(finTiempo - inicioTiempo > LIM_TIEMPO):
		print("Me quede en la poblacion: {}  individuo: {}".format(j,i))
		break	
print("tiempo de ejecucion: ", finTiempo - inicioTiempo, "s")
print("MEJOR poblacion {}, vector {}:, m={}, K={}, Z={}".format(pob, idVector,-1*mejorM,-1*mejorK,mejorZ))