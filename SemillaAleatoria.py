import math

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
	z_value *= -1 
	return z_value

def Z_gaussiana(puntos, k, m):
	z_value = 0 
	for (x,y) in puntos:
		z_value += abs(math.exp(-k*((x-m)**2)))
	z_value *= -1 
	return z_value

