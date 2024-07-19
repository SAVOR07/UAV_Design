# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 18:53:26 2024

@author: SAVOR
"""
def temp(h):
        
    if h<0:
        print("\nInvalid Input of Alttitude")
     
    elif h<11000:
        T = 15.04 - (0.00649*h)
        
    elif h<25000:
        T = -56.46
            
    elif h<47000:
        T = -131.21 + (0.00299*h)

    elif h>47000:
        print("\nModel does not support the altitude above 47000m\n")
    
    if T == 0:
        print("Will be modified soon!\n")
    else:
               
        return(T)