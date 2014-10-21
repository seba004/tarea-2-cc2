import random
from  numpy import  *
from scipy.misc import derivative
import numpy as np
from scipy import *
#from matplotlib import *
import matplotlib.pyplot as plt
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
    print(distancia_x)
    vector_x=distancia_x/sqrt(distancia_x**2 +distancia_y**2)
    vector_y=distancia_y/sqrt(distancia_x**2 +distancia_y**2)
    e=math.e

    influencia_x=0
    influencia_y=0
    if (distancia_x < ri and distancia_x != float(0)):

        influencia_x= e*((float(agente1.peso)*float(agente2.peso))/float(ri*distancia_x))*float(vector_x)
    if (distancia_x >= ri and distancia_x != float(0)):

        influencia_x= ((e*float(agente1.peso)*float(agente2.peso))/float(distancia_x**2))*-float(vector_x)




    if (distancia_y < ri and distancia_y != 0):
        influencia_y= e*((float(agente1.peso)*float(agente2.peso))/float(ri*distancia_y))*float(vector_y)
    if (distancia_y >= ri and distancia_y != 0):
        influencia_y= ((e*float(agente1.peso)*float(agente2.peso))/float(distancia_y**2))*-float(vector_y)

    return influencia_x,influencia_y

def sum_influencias(lista_agentes,ri):
    cantidad=len(lista_agentes)
    for i in range (cantidad):
        suma_x=0
        suma_y=0
        for j in range(1,cantidad):
            valor_x,valor_y=influencia(lista_agentes[0],lista_agentes[j],ri)
            #print(valor_x)
            suma_x=suma_x+valor_x
            suma_y=suma_y+valor_y
        lista_agentes[0].change_influ_x(suma_x)
        lista_agentes[0].change_influ_y(suma_y)
        primer = lista_agentes.pop( 0 )
        lista_agentes.append(primer)
    return lista_agentes

def ingreso_datos():
    ri=10 # rango maximo de accion de repulsion
    pi= 5 # peso de agentes
    lista_agentes=[]
    tiempo= 45 #tiempo de simulacion
#    lista_agentes.append(agente(2,2,pi,0,0,0,0))# xi,yi,pi,vx,vy,influenciax,influencia y donde x e y son pos y vx y vy son vel
#    lista_agentes.append(agente(-2,2,pi,0,0,0,0))# xi,yi,pi,vx,vy,influenciax,influencia y donde x e y son pos y vx y vy son vel
#    lista_agentes.append(agente(-2,-2,pi,0,0,0,0))# xi,yi,pi,vx,vy,influenciax,influencia y donde x e y son pos y vx y vy son vel
#    lista_agentes.append(agente(2,-2,pi,0,0,0,0))# xi,yi,pi,vx,vy,influenciax,influencia y donde x e y son pos y vx y vy son vel
#    lista_agentes.append(agente(0,0,pi,0,0,0,0))# xi,yi,pi,vx,vy,influenciax,influencia y donde x e y son pos y vx y vy son vel
    lista_agentes.append(agente(0,0,1,0,0,0,0))# xi,yi,pi,vx,vy,influenciax,influencia y donde x e y son pos y vx y vy son vel
    lista_agentes.append(agente(4,1,pi,0,0,0,0))# xi,yi,pi,vx,vy,influenciax,influencia y donde x e y son pos y vx y vy son vel
    lista_agentes.append(agente(4,3,pi,0,0,0,0))# xi,yi,pi,vx,vy,influenciax,influencia y donde x e y son pos y vx y vy son vel
    lista_agentes.append(agente(1,4,pi,0,0,0,0))# xi,yi,pi,vx,vy,influenciax,influencia y donde x e y son pos y vx y vy son vel
    lista_agentes.append(agente(-3,1,pi,0,0,0,0))# xi,yi,pi,vx,vy,influenciax,influencia y donde x e y son pos y vx y vy son vel
    lista_agentes.append(agente(-3,4,pi,0,0,0,0))# xi,yi,pi,vx,vy,influenciax,influencia y donde x e y son pos y vx y vy son vel
    lista_agentes.append(agente(2,-1,pi,0,0,0,0))# xi,yi,pi,vx,vy,influenciax,influencia y donde x e y son pos y vx y vy son vel
    lista_agentes.append(agente(5,-3,pi,0,0,0,0))# xi,yi,pi,vx,vy,influenciax,influencia y donde x e y son pos y vx y vy son vel
    lista_agentes.append(agente(-4,-1,pi,0,0,0,0))# xi,yi,pi,vx,vy,influenciax,influencia y donde x e y son pos y vx y vy son vel
    lista_agentes.append(agente(-2,-2,pi,0,0,0,0))# xi,yi,pi,vx,vy,influenciax,influencia y donde x e y son pos y vx y vy son vel
    lista_agentes.append(agente(-2,-4,pi,0,0,0,0))# xi,yi,pi,vx,vy,influenciax,influencia y donde x e y son pos y vx y vy son vel
    lista_agentes=sum_influencias(lista_agentes,ri)

    return lista_agentes


def edo_euler(funcion, v_inicial, n):
    h = 1 / float(n)
    y = v_inicial
    for i in range(n):
        y = y + h * funcion
        #print y
    return y

def aplicacion_euler(lista_agentes):
    cantidad=len(lista_agentes)
    for i in range (cantidad):
        #print(lista_agentes[i].influencia_x)
        valor_x=round(edo_euler(lista_agentes[i].influencia_x,lista_agentes[i].vx,100))
        valor_y=round(edo_euler(lista_agentes[i].influencia_y,lista_agentes[i].vy,100))
        base_x=lista_agentes[i].x
        base_y=lista_agentes[i].y
        if(base_x <0 and base_y>0):
            valor_x=abs(valor_x)
        if(base_x<0 and base_y<0):
            valor_y=abs(valor_y)
            valor_x=abs(valor_x)
        if(base_x>0 and base_y<0):
            valor_y=abs(valor_y)

        lista_agentes[i].move_x(base_x+valor_x)
        lista_agentes[i].move_y(base_y+valor_y)
    return lista_agentes


#funciones dibujooooo

def listas (lista_agentes):
    cantidad=len(lista_agentes)
    x=[]
    y=[]
    for i in range (cantidad):
            x.append(lista_agentes[i].x)
            y.append(lista_agentes[i].y)
    return x,y

def simulacion ():
    x=[]
    y=[]
    fig, ax = plt.subplots()
    agentes=ingreso_datos()
    x,y=listas(agentes)
    points, = ax.plot(x, y, marker='o', linestyle='None')
    ax.set_xlim(-120, 120)
    ax.set_ylim(-120, 120)
    tim=10
    t1= time.clock()
    while True:
        agentes=aplicacion_euler(agentes)
        x,y=listas(agentes)
        points.set_data(x, y)
        plt.pause(0.5)
        t2= time.clock()
        if (t2-t1 >= tim):
            plt.close()
            break
    return agentes



if __name__ == '__main__':

    t= simulacion()