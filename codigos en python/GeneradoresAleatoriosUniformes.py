# -*- coding: utf-8 -*-
"""
Created on Wed Sep 09 11:29:47 2015

@author: David C
"""

class GeneradoresAleatorios:
    def generar_Conguencial(self,cant,semilla):
       x0=semilla
       m=2305843009213693951
       a=5
       b=1
       xi=x0
       v=[]
       while cant>0: 
           xi=float((a*xi+b)%m)
           ui=xi/m
           #print ui           
           v.append(ui)
           cant-=1
           
       return v

           
    def generar_midsquare(self,cant,semilla):
                
        x0=semilla
        aux=x0        
        n=0
        ui='0.'+str(x0)    
        cuadrado=str(x0*x0)
        v=[]       
        
        while aux>0:
            aux=aux/10
            n+=1
        n=n/2
       
        while len(cuadrado) < (4*n):
            cuadrado='0'+cuadrado
           
        while cant>0:
            xi=cuadrado
            xi=xi[n:len(xi)-n]
            ui='0.'+ str(xi)
            cuadrado=str(int(xi)*int(xi))
            
            while len(cuadrado)<4*n:
                cuadrado='0'+str(cuadrado)
            #print 'Ui',float(ui)
            v.append(float(ui))    
            cant-=1
        return v   
            
    def generar_wichmannHill(self,cant,semilla): 
       x0=semilla
       y0=7*semilla
       z0=2*semilla
       mx=30269
       my=30307
       mz=30323
       ax=171
       ay=172
       az=170
       xi=x0
       yi=y0
       zi=z0
       v=[]
       while cant>0: 
           xi=float((ax*xi) % mx)
           yi=float((ay*yi) % my)
           zi=float((az*zi) % mz)
           
           ui=((xi/mx)+(yi/my)+(zi/mz)) % 1
           #print ui
           v.append(ui)            
           cant-=1
       if len(v)==1:     
          return v[0]
       else:
           return v

    def generar_randu(self,cant,semilla): 
       m=2147483648
       a=65539
       xi=semilla
       v=[]
       while cant>0: 
           xi=float((a*xi) % m)
           ui=xi/m
           #print ui
           v.append(ui)            
           cant-=1
       return v