import pandas as pd
import numpy

x = list()
y = list()

def LecturaArchivo(ruta):
    df = pd.read_csv(ruta)
    x = pd.unique(df['x']).tolist()
    y = pd.unique(df['y']).tolist()
    puntos = numpy.zeros(shape=(len(x),2))
    for i in range (len(x)):
        puntos[i] = [x[i],y[i]]
    return puntos
        