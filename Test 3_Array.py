# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 20:22:43 2024

@author: SAVOR
"""
import numpy as np
import math as m
l_by_d = np.arange(10,16,0.5)

L_D = [0]*len(l_by_d)

l_d = [[0]*len(l_by_d)]*len(l_by_d)

f=float(m.pi**2)
print(f)

'''
k=0
for x in l_by_d:
    L_D[k]=x
    k=k+1
    m=pow(10,2)
print(L_D)
print(m)'''