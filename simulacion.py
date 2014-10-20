import random
from  numpy import  *
from scipy.misc import derivative
import numpy as np
from scipy import *
#from matplotlib import *
#import matplotlib.pyplot as plt
from numpy.linalg import norm, solve
from scipy import linalg as al#algebra lineal
import time

def crear_matriz(fila,columna):
    matriz= np.zeros([fila,columna],dtype='int')
    return matriz

def imprimir_matriz(matriz):
    print '\n'.join(' '.join(str(cell) for cell in row) for row in matriz)
    return

class agente:
    def __init__(self,x,y,peso):
        self.x=x
        self.y=y
        self.peso=peso
    def move_x(self,x_in):
        self.x=x_in
    def move_y(self,y_in):
        self.y=y_in


def cantidad_agentes():
    print("Cuantos agentes desea?")
    agentes = input()
    return agentes

def creacion_agentes(cantidad):
    agentes=[]
    for i in range(cantidad):
        print("posicion en x del agente ",i)
        pos_x = input()
        print("posicion en y del agente ",i)
        pos_y = input()
        print("peso del agente ",i)
        peso = input()
        i = agente(pos_x,pos_y,peso)
        agentes.append(i)
    return agentes#lista de agentes

def incorporacion_agentes(agentes,matriz):
    for i in agentes:
        matriz[i.x,i.y]=1
    return matriz


if __name__ == '__main__':
    a=crear_matriz(15,15)
    imprimir_matriz(a)
    b=cantidad_agentes()
    t=creacion_agentes(b)
    ma=incorporacion_agentes(t,a)
    imprimir_matriz(ma)