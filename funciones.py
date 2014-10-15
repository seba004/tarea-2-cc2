#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      seba
#
# Created:     15-10-2014
# Copyright:   (c) seba 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random
from  numpy import  *
from scipy.misc import derivative
import numpy as np
from scipy import *
from matplotlib import *
import matplotlib.pyplot as plt
from numpy.linalg import norm, solve
from scipy import linalg as al#algebra lineal

def midpoint (intervalos, funcion):
    fun = np.vectorize(funcion)
    x = np.linspace(0, 1, intervalos+1)
    h=(float(1)-float(0))/float(intervalos)
    suma=0
    for i in range(intervalos-1):
        mid=(x[i+1] + x[i])/2
        valor=fun(mid)
        suma= suma+valor
    parte_izquierda=h*suma
    numero=random.random()
    dev=derivative(fun,numero,dx=1,n=2)
    parte_derecha= (((1-0)*h**2)/24)*dev
    resultado= parte_derecha+parte_izquierda
    return resultado

def trapezoide(intervalos,funcion):
    fun = np.vectorize(funcion)
    x = np.linspace(0, 1, intervalos+1)
    h=(float(1)-float(0))/float(intervalos)
    primer=h/float(2)
    y0=fun(0)               #buscar bien que son los y0  e  ym
    ym=fun(intervalos)
    suma=0
    for i in range(intervalos-1):
        valor=fun(i)
        suma= suma+valor
    suma_total=suma*2
    lado_izquierdo=primer*(y0+ym+suma_total)
    numero=random.random()
    dev=derivative(fun,numero,dx=1,n=2)
    lado_derecho= (((1-0)*h**2)/12)*dev
    total=lado_izquierdo-lado_derecho
    return total

def simpson (intervalos,funcion):
    fun = np.vectorize(funcion)
    x = np.linspace(0, 1, intervalos+1)
    h=(float(1)-float(0))/float(intervalos)
    primer = h/3
    y0=fun(0)
    y2m=fun(2*intervalos)
    suma1=0
    for i in range(intervalos):
        valor=fun(2*i)
        suma1= suma1+valor
    suma_total_primera=suma1*4
    suma2=0
    for i in range(intervalos-1):
        valor=fun(2*i)
        suma2= suma2+valor
    suma_total_segunda=suma2*2
    lado_izquierdo=primer*(y0+y2m+suma_total_primera+suma_total_segunda)
    numero=random.random()
    dev=derivative(fun,numero,dx=1,n=2)#el n tiene que ser 4 pero numpy no me daja D:
    lado_derecho= (((1-0)*h**4)/180)*dev
    total =lado_izquierdo-lado_derecho
    return total



if __name__ == '__main__':
    myfun = lambda x : np.sin(x) #1 # x #np.exp(-x)
    intervalos=1000
    #a= midpoint(intervalos,myfun)
    #a= trapezoide(intervalos,myfun)
    a= simpson(intervalos,myfun)
    print(a)


