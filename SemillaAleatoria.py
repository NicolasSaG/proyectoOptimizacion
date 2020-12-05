def restriccion(value, lim, tipo):
	cumple = False
	if tipo == 0: #<=
		if value <= lim: 
			cumple = True
	else : # >=
		if value >= lim: 
			cumple = True
	return cumple

def Z(puntos, m, b):
	z_value = 0 
	for (x,y) in puntos:
		z_value += abs(m*x + b - y)
	z_value *= -1 
	return z_value