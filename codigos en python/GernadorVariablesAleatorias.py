# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 08:32:22 2015

@author: David C
"""
import GeneradoresAleatoriosUniformes as ga
class MetodoInversion:
    
    def generarVANormal(self,cant):
      ha=ga.GeneradoresAleatoriosUniformes().imprimir(cant)
      for num in ha:
          