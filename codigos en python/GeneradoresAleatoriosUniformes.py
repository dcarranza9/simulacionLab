# -*- coding: utf-8 -*-
"""
Created on Wed Sep 09 11:29:47 2015

@author: David C
"""

class GeneradoresAleatoriosUniformes:
    def generar_Conguencial(self,cant):
       x0=5
       m=2305843009213693951
       a=5
       b=1
       xi=x0
       
       while cant>0: 
           xi=float((a*xi+b)%m)
           ui=xi/m
           print ui           
           cant-=1

           
    def generar_midsquare(self,cant):
                
        x0=1009
        aux=x0        
        n=0
        ui='0,'+str(x0)    
        cuadrado=str(x0*x0)        
        
        while aux>0:
            aux=aux/10
            n+=1
        n=n/2
       
        while len(cuadrado) < (4*n):
            cuadrado='0'+cuadrado
           
        while cant>0:
            xi=cuadrado
            xi=xi[n:len(xi)-n]
            ui='0,'+ str(xi)
            cuadrado=str(int(xi)*int(xi))
            
            while len(cuadrado)<4*n:
                cuadrado='0'+str(cuadrado)
            print 'Ui',ui
            cant-=1
    def generar_wichmannHill(self,cant): 
       x0=5
       y0=7
       z0=2       
       mx=30269
       my=30307
       mz=30323
       ax=171
       ay=172
       az=170
       xi=x0
       yi=y0
       zi=z0
       
       while cant>0: 
           xi=float((ax*xi) % mx)
           yi=float((ay*yi) % my)
           zi=float((az*zi) % mz)
           
           ui=((xi/mx)+(yi/my)+(zi/mz)) % 1
           print ui           
           cant-=1
           
    def imprimir(self,h):
       i=0
       while i<=10 :
           v=list.append(i)
           i+=1
       return v
