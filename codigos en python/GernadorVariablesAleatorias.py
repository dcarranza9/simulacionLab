# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 08:32:22 2015

@author: David C
"""
import GeneradoresAleatoriosUniformes as ga
import numpy as np

class MetodoInversion:
    #Se quiere simular el numero de puntos optenidos al lanzar dos dados 
    def lanzamientoDosDados(self):
        #funcion de distribución cuando la suma de los puntos es 2,3,....,12
        fd=[1/36.,2/36.,3/36.,4/36.,5/36.,6/36.,5/36.,4/36.,3/36.,2/36.,1/36.]
        #funcion de distribucion acumulada        
        fda=np.cumsum(fd)
        p=ga.GeneradoresAleatoriosUniformes().generar_wichmannHill()  

mi=MetodoInversion()
mi.lanzamientoDosDados()