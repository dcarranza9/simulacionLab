# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 14:58:52 2015

@author: David C
"""

import numpy as np
import scipy.special as sp
import matplotlib.pyplot as plt

        
        #funcion de distribución cuando la suma de los puntos es 2,3,....,12
        fd=[1/117.,2/117.,3/117.,4/117.,5/117.,6/117.,7/117.,8/117.,9/117.,9/117.,9/117.,9/117,9/117.,8/117.,7/117.,6/117.,5/117.,4/117.,3/117.,2/117.,1/117.]
        
        #funcion de distribucion acumulada        
        fda=np.cumsum(fd)
        vesperado=
        p=ga.GeneradoresAleatorios().generar_wichmannHill(100,19)
                    
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
            elif fda[10] < p<fda[11]:
                print 'El resultado es: ',12
            elif fda[11] < p<fda[12]:
                print 'El resultado es: ',13  
            elif fda[12] < p<fda[13]:
                print 'El resultado es: ',13
            elif fda[13] < p<fda[14]:
                print 'El resultado es: ',14
            elif fda[14] < p<fda[15]:
                print 'El resultado es: ',15
            elif fda[15] < p<fda[16]:
                print 'El resultado es: ',16
            elif fda[16] < p<fda[17]:
                print 'El resultado es: ',17
            elif fda[18] < p<fda[19]:
                print 'El resultado es: ',18
            elif fda[19] < p<fda[20]:
                print 'El resultado es: ',19
            elif fda[20] < p<fda[21]:
                print 'El resultado es: ',20
            else:
                print 'El resultado es: ',22