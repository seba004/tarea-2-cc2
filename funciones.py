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
    h=(float(1)-float(0))/float(intervalos)
    valor=0
    suma=0
    for i in range(1,intervalos+1):
        wi=(valor+valor+h)/2
        suma= suma+funcion(wi)
        valor=valor+h
    return suma*h

def trapezoide(intervalos,funcion):
    h=(float(1)-float(0))/float(intervalos)
    h2=h/2
    fa=funcion(0)
    fb=funcion(1)
    numero=0
    suma=0
    for i in range(1,intervalos):
        numero=numero+h
        valor=funcion(numero)
        suma=suma+valor
    suma=suma*2
    final=(fa+fb+suma)*h2
    return final

def simpson (intervalos,funcion):
    h=(float(1)-float(0))/float(intervalos)
    h3=h/3
    fa=funcion(0)
    fb=funcion(1)
    x=np.linspace(0,1,intervalos+1)
    suma1=0
    for i in range(1,intervalos/2):
        suma1= suma1+funcion(x[2*i])
    suma1=suma1*2
    suma2=0
    for i in range(1,(intervalos/2)+1):
        suma2=suma2+funcion(x[2*i-1])
    suma2=suma2*4
    final=h3*(fa+fb+suma1+suma2)
    return final





if __name__ == '__main__':
    myfun = lambda x : x**2 #1 # x #np.exp(-x)
    intervalos=6
    a= midpoint(intervalos,myfun)
    b= trapezoide(intervalos,myfun)
    c= simpson(intervalos,myfun)
    print("midpoint es: ",a)
    print("trapecio es: ",b)
    print("simpson es: ",c)


