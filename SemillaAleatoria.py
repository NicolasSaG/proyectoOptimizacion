import math, random, subprocess, time

def obtenerTiempo():
    	return time.process_time()

def generarSemillaAleatoria():
	# traverse the software list 
	#pip install wmic
	data = subprocess.check_output(['wmic', 'process', 'list', 'brief'])
	a = str(data)
	n_proc = 0
	t = time.localtime()
	try:
	  for i in range(len(a)):
	  	a.split("\\r\\r\\n")[i]
	except IndexError as e:
	  return i * t.tm_hour * t.tm_min * t.tm_sec

def restriccion(value, lim, tipo):
	cumple = False
	if tipo == 0: #<=
		if value <= lim: 
			cumple = True
	else : # >=
		if value >= lim: 
			cumple = True
	return cumple

#calcular el limite de b
def calcular_bLineal(puntos): #(Zx)^2 = b
	lim_b = 0
	for (x,y) in puntos: #sumar los valores de x
		lim_b += x
	lim_b = lim_b**2 #elevar la suma al cuadrado
	return lim_b

def Mayor(puntos):
	xaux = 0
	yaux = 0
	for (x,y) in puntos:
		if(y>yaux):
			yaux=y
			xaux=x
	return xaux

def Z_lineal(puntos, m, b):
	z_value = 0 
	#sumar valores absolutos de la recta dados los puntos y 
	#m y b generados aleatoriamente
	for (x,y) in puntos: 
		z_value += abs(m*x + b - y) 
	return z_value

def Z_gaussiana(puntos, k, m):
	z_value = 0
	for (x,y) in puntos:
		z_value += abs(math.exp(-k*((x-m)*(x-m))))
	return z_value

#generacion de individuo para limites de la funcion lineal
def generarIndividuoLineal(m, b):
	return random.uniform(-m, m), random.uniform(-b, b)
def generarIndividuoGauss(i,s):
	return random.uniform(i,s)

