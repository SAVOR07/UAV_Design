# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 18:44:15 2024

Density Calculator at some altitude h in meters

@author: SAVOR
"""
import math as m

def density(h):
        
    if h<0:
        print("\nInvalid Input of Alttitude")
     
    elif h<11000:
        T = 15.04 - (0.00649*h)
        P = (101.29*pow((((T+273.1)/288.08)),5.256))
        
    elif h<25000:
        T = -56.46
        P = ((22.65)*(m.exp(1.73-(0.000157*h))))
    
    elif h<47000:
        T = -131.21 + (0.00299*h)
        P = 2.488*(pow(((T+273.1)/(216.6)),(-11.388)))
    elif h>47000:
        print("\nModel does not support the altitude above 47000m\n")
    rho = float(P/((T+273.1)*0.2869))
    
    if T == 0:
        print("Will be modified soon!\n")
    else:
               
        return(rho)