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
        chicuad=0.#Almacena la suma acumulada del test
        i=1.
        fo=[]#vector con las frecuencias observadas
        
        while i<=k:
            fi=self.contarMuestras(xau,(i-1)/k,i/k) # Deterina las obsevaciones en una clase 
            fo.append(fi)
            chicuad+=np.square(fi-ei)/ei # Variable que calcula el test
            i+=1
        
        chiprobe,pvalue= st.chisquare(fo,ei)        
        plt.hist(xau,k)
        plt.plot(xau,ei*np.ones_like(xau),lw=2.0,color='r',label="No aparese :(")
        
                        
        
        print chicuad    
        print chiprobe
        print pvalue
                
    def contarMuestras(self,a,vmin,vmax):
        cant=0
        for x in a:
             
            if vmin < x < vmax: # si la observación esta dentro de la clase se cueta una nueva observación
               cant+=1
       
        return cant
        
    def rachas(self):
        x=gau.GeneradoresAleatorios().generar_wichmannHill(100,23)  #Secuencia de numeros aleatorios      
        media,desv,test=0,0,0 #parametros para el calculo del test
        r,n,i=[],0,0       #Parametros para el calculo de las rachas
        while i< (len(x)-1):           
           if x[i+1] >= x[i]:
               r.append(1)
            #   des+=1
           else:               
               r.append(0)               
            #   asc+=1
           i+=1
        i=0 #variable para las iteraciones del vector con las rachas  
        l=0 # Variable Auxiliar para el conteo de rachas
        #[000100011]               
        while i< len(r):#Determina el numero de cambios     que hay en el vector binario (unos y ceros) de rachas
            if i==0:
                l=r[i]
            else:
                if r[i]!=l:
                    n+=1
                if (i==(len(r)-1)):
                    n+=1
            l=r[i]
                
            i+=1
            
        media,desv=(2*n-1)/3.,(16*n-29)/90. #Parametros para la distribución gausiana
                
        test=st.norm.pdf(x,media,desv) # Se calcula el test con la distribución normalizada
        plt.hist(test,25)
        #plt.plot(np.sort(x),x,'o-')
        plt.grid(True)
        
        print n,media,desv
        
    def rachasMediana(self) :
        x=gau.GeneradoresAleatorios().generar_wichmannHill(100,23) #  Se genera la secuencia de numeros aleatorios 
        mediana=np.median(np.sort(x)) #Se calcula la mediana de la secuencia de numeros aleatorios        
        media,desv,test=0,0,0 #Variables para el test
        r,n,i=[],0,0       #Variables para calcular las rachas
        while i< (len(x)-1):# Llena el vector binario(unos y ceros) si el numero esta por encima o debajo de la mediana           
           if x[i]>mediana:
               r.append(1)
            #   des+=1
           else:               
               r.append(0)               
            #   asc+=1
           i+=1
        i=0  
        l=0 
                       
        while i< len(r):#Determina el numero de cambios     que hay en el vector binario (unos y ceros) de rachas
            if i==0:
                l=r[i]
            else:
                if r[i]!=l:
                    n+=1
                if (i==(len(r)-1)):
                  n+=1
            l=r[i]                
            i+=1
            
        media,desv=(2+n)/2.,n/2. #Parametros para la distribución gausiana
        test=st.norm(media,desv)
        
        print test
        
    def permutaciones(self):
        x=gau.GeneradoresAleatorios().generar_wichmannHill(100,23) # Se genera la secuencia de numeros aleatorios 
        kuplas,upla,k=[],[],0 # Vectores para las Uplas y el numero de
        
        
        
                
    def huecos(self):

        x=gau.GeneradoresAleatorios().generar_wichmannHill(100,23) # Se genera la secuencia de numeros aleatorios 
        # Se generan dos valores fijos alpha y beta con 0< alpha < beta < 1
        alpha=gau.GeneradoresAleatorios().generar_wichmannHill(1,31) # Se genera el limite alpha
        beta= gau.GeneradoresAleatorios().generar_wichmannHill(1,29) # Se genera el limite beta
        m=0 #Variable para la logitud del hueco
        x=np.sort(x)
        
a=Contrastes()

