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



class agente:
    def __init__(self,x,y,peso,vx,vy,influencia_x,influencia_y):
        self.x=x
        self.y=y
        self.peso=peso
        self.vx=vx
        self.vy=vy
        self.influencia_x=influencia_x
        self.influencia_y=influencia_y

    def change_influ_x(self,influ_in_x):
        self.influencia_x=influ_in_x

    def change_influ_y(self,influ_in_y):
        self.influencia_y=influ_in_y

    def move_x(self,x_in):
        self.x=x_in

    def move_y(self,y_in):
        self.y=y_in

    def move_vx(self,vx_in):
        self.vx=vx_in

    def move_vy(self,vy_in):
        self.vy=vy_in

def influencia(agente1,agente2,ri):
    distancia_x=abs(agente1.x -agente2.x)
    distancia_y=abs(agente1.y -agente2.y)
    vector_x=distancia_x/sqrt(distancia_x**2 +distancia_y**2)
    vector_y=distancia_y/sqrt(distancia_x**2 +distancia_y**2)
    e=math.e
    influencia_x=0
    influencia_y=0
    if (distancia_x < ri):
        influencia_x= e*((float(agente1.peso)*float(agente2.peso))/float(ri*distancia_x))*float(vector_x)
    if (distancia_x >= ri):
        influencia_x= ((e*float(agente1.peso)*float(agente2.peso))/float(distancia_x**2))*-float(vector_x)

    if (distancia_y < ri):
        influencia_y= e*((float(agente1.peso)*float(agente2.peso))/float(ri*distancia_y))*float(vector_y)
    if (distancia_y >= ri):
        influencia_y= ((e*float(agente1.peso)*float(agente2.peso))/float(distancia_y**2))*-float(vector_y)

    return influencia_x,influencia_y

def sum_influencias(lista_agentes,ri):
    cantidad=len(lista_agentes)
    for i in range (cantidad):
        suma_x=0
        suma_y=0
        for j in range(1,cantidad):
            valor_x,valor_y=influencia(lista_agentes[0],lista_agentes[j],ri)
            suma_x=suma_x+valor_x
            suma_y=suma_y+valor_y
        lista_agentes[0].change_influ_x(suma_x)
        lista_agentes[0].change_influ_y(suma_y)
        primer = lista_agentes.pop( 0 )
        lista_agentes.append(primer)
    return lista_agentes

def ingreso_datos():
    ri=45 # rango maximo de accion de repulsion
    pi= 2 # peso de agentes
    lista_agentes=[]
    tiempo= 45 #tiempo de simulacion
    lista_agentes.append(agente(0,0,pi,5,5,0,0))# xi,yi,pi,vx,vy,influenciax,influencia y donde x e y son pos y vx y vy son vel
    lista_agentes.append(agente(2,2,pi,5,5,0,0))# xi,yi,pi,vx,vy,influenciax,influencia y donde x e y son pos y vx y vy son vel
    lista_agentes.append(agente(5,5,pi,5,5,0,0))# xi,yi,pi,vx,vy,influenciax,influencia y donde x e y son pos y vx y vy son vel
    lista_agentes=sum_influencias(lista_agentes,ri)

    return lista_agentes




#funciones dibujooooo
def crear_matriz(fila,columna):
    matriz= np.zeros([fila,columna],dtype='int')
    return matriz

def imprimir_matriz(matriz):
    print '\n'.join(' '.join(str(cell) for cell in row) for row in matriz)
    return

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
    #a=crear_matriz(15,15)
    #imprimir_matriz(a)
    #b=cantidad_agentes()
    #t=creacion_agentes(b)
    #ma=incorporacion_agentes(t,a)
    #imprimir_matriz(ma)
    t=ingreso_datos()