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

if __name__ == '__main__':
    myfun = lambda x : x**2 #1 # x #np.exp(-x)
    intervalos=100
    a= midpoint(intervalos,myfun)
    print(a)


