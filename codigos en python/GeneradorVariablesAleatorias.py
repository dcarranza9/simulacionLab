# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 08:32:22 2015

@author: David C
"""
import GeneradoresAleatoriosUniformes as ga
import numpy as np
import scipy.special as sp
import matplotlib.pyplot as plt

class MetodoInversion:
    #Se quiere simular el numero de puntos optenidos al lanzar dos dados 
    def lanzamientoDosDados(self):
        plt.step
        #funcion de distribución cuando la suma de los puntos es 2,3,....,12
        fd=[1/36.,2/36.,3/36.,4/36.,5/36.,6/36.,5/36.,4/36.,3/36.,2/36.,1/36.]
        #funcion de distribucion acumulada        
        fda=np.cumsum(fd)
       
        p=ga.GeneradoresAleatorios().generar_wichmannHill(1,19)
        
        if p<fda[1]:
            print 'El resultado es: ',2
        elif fda[1]<p<fda[2]:
            print 'El resultado es: ',3
        elif fda[2]<p<fda[3]:
            print 'El resultado es: ',4
        elif fda[3]<p<fda[4]:
            print 'El resultado es: ',5
        elif fda[4] <p<fda[5]:
            print 'El resultado es: ',6
        elif fda[5]<p<fda[6]:
            print 'El resultado es: ',7
        elif fda[6]<p<fda[7]:
            print 'El resultado es: ',8
        elif fda[7] < p<fda[8]:
            print 'El resultado es: ',9
        elif fda[8] < p<fda[9]:
            print 'El resultado es: ',10
        elif fda[9] < p<fda[10]:
            print 'El resultado es: ',11
        else:
            print 'El resultado es: ',12
            
    def normal(self,media,desviacion):
        p= ga.GeneradoresAleatorios().generar_wichmannHill(1,77)
        x= 2*p-1        
        erfinv=sp.erfinv(x)
        normInv= media+ desviacion*np.sqrt(2)*(erfinv)
        print normInv
        return normInv
        
             
mi=MetodoInversion()
mi.normal(5,0.5)