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
#from matplotlib import *
#import matplotlib.pyplot as plt
from numpy.linalg import norm, solve
from scipy import linalg as al#algebra lineal
import time

def midpoint (intervalos, funcion,a,b):#(a,b) es de donde a donde va la int
    h=(float(b)-float(a))/float(intervalos)
    valor=a
    suma=0
    for i in range(1,intervalos+1):
        wi=(valor+valor+h)/2
        suma= suma+funcion(wi)
        valor=valor+h
    return suma*h

def trapezoide(intervalos,funcion,a,b):#(a,b) es de donde a donde va la int
    h=(float(b)-float(a))/float(intervalos)
    h2=h/2
    fa=funcion(a)
    fb=funcion(b)
    numero=a
    suma=0
    for i in range(1,intervalos):
        numero=numero+h
        valor=funcion(numero)
        suma=suma+valor
    suma=suma*2
    final=(fa+fb+suma)*h2
    return final
#creo que interbalos tiene queser pares para simpson
def simpson (intervalos,funcion,a,b):#(a,b) es de donde a donde va la int
    h=(float(b)-float(a))/float(intervalos)
    h3=h/3
    fa=funcion(a)
    fb=funcion(b)
    x=np.linspace(a,b,intervalos+1)
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


def gauss (intervalos,funcion):

    xi,wi=np.polynomial.legendre.leggauss(intervalos)
    suma=0

    for i in range (1,intervalos):
        suma=suma+(wi[i]*funcion(xi[i]))
    suma=suma+wi[0]*funcion(xi[0])
    return suma


def legen (intervalos):
    xi,wi=np.polynomial.legendre.leggauss(intervalos)
    return xi,wi

def new_gauss(intervalos,funcion,xi,wi):

    suma=0

    for i in range (1,intervalos):
        suma=suma+(wi[i]*funcion(xi[i]))
    suma=suma+wi[0]*funcion(xi[0])
    return suma

if __name__ == '__main__':
    myfun = lambda x : x**2 #1 # x #np.exp(-x)
    intervalos=10
    t1 = time.clock()
    for i in range(0,1000):
        a= midpoint(intervalos,myfun,-1,1)
    t2 = time.clock()

    t3 = time.clock()
    for i in range(0,1000):
        b= trapezoide(intervalos,myfun,-1,1)
    t4 = time.clock()

    t5 = time.clock()
    for i in range(0,1000):
        c= simpson(intervalos,myfun,-1,1)
    t6 = time.clock()

    t7 = time.clock()
    for i in range(0,1000):
         d=gauss(intervalos,myfun)
    t8 = time.clock()

    t9=time.clock()
    xi,wi= legen(intervalos)
    for i in range(0,1000):
         d=new_gauss(intervalos,myfun,xi,wi)
    t10 = time.clock()

    print("El tiempo de punto medio es: ", t2-t1)
    print("El tiempo de trapecio es: ", t4-t3)
    print("El tiempo de simpson es: ", t6-t5)
    print("El tiempo de gauss es: ", t8-t7)
    print("El tiempo de gauss modificado es: ", t10-t9)