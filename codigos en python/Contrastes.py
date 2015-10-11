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
        n=100#Longitud de la secuencia
        xau=gau.GeneradoresAleatorios().generar_wichmannHill(n,137)#Se define la secuencia de mi generador de 100 muestas
        k=8. # cantidad de subintervalos
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
        
        plt.hist(xau,k,rwidth=1/k)
        plt.grid(True)
        print chicuad    
        print chiprobe
        print pvalue
                
    def contarMuestras(self,a,vmin,vmax):
        cant=0
        for x in a:
             
            if vmin < x < vmax:
               cant+=1
       
        return cant
        
    def rachas(self):
        x=gau.GeneradoresAleatorios().generar_wichmannHill(10,23)
        
        media,desv,test=0,0,0
        r,n,i=[],0,0       
        while i< (len(x)-1):           
           if x[i+1] >= x[i]:
               r.append(1)
            #   des+=1
           else:               
               r.append(0)               
            #   asc+=1
           i+=1
        i=0  
        l=0
                       
        while i< len(r):
            if i==0:
                l=r[i]
            else:
                if r[i]!=l:
                    n+=1
                if (i==(len(r)-1)):
                  n+=1
            l=r[i]
                
            i+=1
            
        media,desv=(2*n-1)/3.,(16*n-29)/90.
        test=st.norm.pdf(x,loc=media,scale=desv)
        print n,r
        
        print test,media,desv
        
      
a=Contrastes()
a.rachas()
