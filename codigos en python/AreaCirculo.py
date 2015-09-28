# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 10:35:46 2015

@author: David C
"""
import GeneradoresAleatoriosUniformes as al
import numpy as np
import matplotlib.pyplot as plt

class CalculaArea:
    def graficar(self,xdentro,ydentro,xfuera,yfuera,k,ateorica,acalculada):    
        
        plt.figure('Area de un circulo con valores aleatorios')#Crea una nueva ventana con el titulo       
        plt.clf()#Limpia la ventana "Clear figure"
        #Se agrega un subtitulo dentro de la ventana
        plt.suptitle('Area Calculada: '+str(acalculada)+'\nArea Teorica: '+str(ateorica)+'\n Diferencia: '+ str(acalculada-ateorica),fontsize=10,fontweight='bold',bbox=dict(facecolor='white', alpha=0.5),horizontalalignment='center')        
        #Se grafincan los puntos 
        plt.scatter(xfuera,yfuera,label='Puntos Fuera') 
        plt.scatter(xdentro,ydentro,c='r',label='Puntos Dentro') 
        #Se configura la leyenda
        plt.legend(loc=1)        
        plt.grid(True)#Se activa la grilla
        #Configuracion de etiquetas en los ejes
        plt.xlabel('Valores en X',fontsize=16)
        plt.ylabel('Valores en Y',fontsize=16)
        #Limite de cada eje
        plt.xlim(-k,k)
        plt.ylim(-k,k)
        #Configuracion de textos adicionales al subtitulo de la ventana
        plt.figtext(0.7,0.98,'#Total ptos. Dentro:'+str(len(xdentro)),fontweight='bold',fontsize=9,bbox=dict(facecolor='red', alpha=0.7))
        plt.figtext(0.7,0.95,'#Total Ptos. Fuera : '+str(len(xfuera)),fontweight='bold',fontsize=9,bbox=dict(facecolor='blue', alpha=0.7))
        plt.figtext(0.7,0.92,'Total de puntos(N) : '+str(len(xdentro)+len(xfuera)),fontweight='bold',fontsize=9,bbox=dict(facecolor='white', alpha=0.5))
        #Propiedad equitativa para los ejes, hace que se vea como un circulo y no como una elipse
        plt.axis('equal')     
               
    def linealizar(self,k,randu):
        #Recibe una lista de valores aleatorios y hace la transformación lineal
        y=[]
        for val in randu:
            tmp=2*(val-0.5)*k #transforma cada valor con y=2k(x-1/2)
            y.append(tmp)
        return y#Retorna una lista con los valores transformados
            
    def calcularAreas(self):
        #Se piden los parametros
        radio=int(raw_input('Ingrese el radio del circulo: '))
        k=int(raw_input('Ingrese el valor k del rectangulo: '))
        n=int(raw_input('Ingrese la cantidad de aleatorios: '))
        #Se generan los numero aleatoeros y se guardan
        randux=al.GeneradoresAleatorios().generar_wichmannHill(n,29)
        randuy=al.GeneradoresAleatorios().generar_wichmannHill(n,77)
        #Se definen listas para clasificar los puntos que caen dentro y fuera
        xf,yf,xd,yd=[] , [] , [] , []
        #Se definen Variables para almacenar y calcular el resultado de las áreas respectivas
        areaAnalitica, areaCalculada, i =0 , 0 , 0
        vbin=0.0
        #Se almacenan los valores de la transformación lineal de los valores aleatorios generados       
        xi,yi=self.linealizar(k,randux) , self.linealizar(k,randuy)       
        
        
        while i < len(xi):
            #Se calcula si el punto esta dentro o fuera del circulo
            v = (np.power(xi[i],2)) + (np.power(yi[i],2))#x^2 + y^2=r^2 Formula de la circunferencia
            if v <= np.power(radio,2) :
                #Si el punto esta dentro se almacena cada componente para identificarlas al graficar
                xd.append(xi[i])#x-dentro
                yd.append(yi[i])#y-dentro
                vbin+=1.0 #Se aumenta la variabñe binaria para calcular el área              
            else:
                #Si el punto esta fuera tambien se almacena cada componente para identificarlas al graficar
                xf.append(xi[i])#x-fuera
                yf.append(yi[i])#y-fuera                             
            i+=1
        #Se hace el calculo respectvo de las areas
        areaAnalitica=(np.pi)*(np.power(radio,2))# pi*r^2 Area teorica 
        areaCalculada=(vbin*4*np.power(k,2))/(len(xi))# [n(2k)^2]/N
        # Se manda a graficar la figura con todos los parametros calculados
        self.graficar(xd,yd,xf,yf,k,areaAnalitica,areaCalculada)
            
c=CalculaArea()
c.calcularAreas()
