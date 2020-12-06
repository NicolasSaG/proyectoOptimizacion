import math
import random
import subprocess
import time

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

def calcular_bLineal(puntos):
	b = 0
	for (x,y) in puntos:
		b += x
	b = b**2
	return b

def Z_lineal(puntos, m, b):
	z_value = 0 
	for (x,y) in puntos:
		z_value += abs(m*x + b - y)
 
	return z_value

def Z_gaussiana(puntos, k, m):
	z_value = 0 
	for (x,y) in puntos:
		z_value += abs(math.exp(-k*((x-m)**2)))
	return z_value

def generarIndividuoLineal(m, b):
	return random.uniform(-m, m), random.uniform(-b, b)