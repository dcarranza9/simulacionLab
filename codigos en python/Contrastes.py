# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 10:14:28 2015

@author: David C
"""
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
import GeneradoresAleatoriosUniformes as gau

class Contrastes:
    def chiCuadrado(self):
        n=100
        xt=[1.0]*n#Se define la secuencia teórica de 100 muestas
        xnp=np.random.uniform(0,1,n)#Se define la secuencia de numpy de 100 muestas
        xau=gau.GeneradoresAleatorios().generar_wichmannHill(n,137)#Se define la secuencia de mi generador de 100 muestas
        
        k=10. # cantidad de subintervalos
        ei=n/k #Cantidad esperada de observaciones
        chicuad=0.
        i=1.
        fo=[]
        
        while i<=k:
            fi=self.contarMuestras(xau,(i-1)/k,i/k)
            fo.append(fi)
            chicuad+=np.square(fi-ei)/ei
            i+=1
        
        chiprobe,pvalue= st.chisquare(fo,ei)
        
        plt.hist(xau,k,normed=False)
        plt.grid(True)
        
        print chicuad    
        print chiprobe
        print pvalue
                
    def contarMuestras(self,a,vmin,vmax):
        cant=0
        for x in a:
             
            if vmin < x < vmax:
               cant+=1
        print vmin, '-> ',vmax,'-> ', cant  
        return cant
a=Contrastes()
a.chiCuadrado()
