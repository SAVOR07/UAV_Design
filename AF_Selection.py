# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 04:02:34 2024

@author: SAVOR
"""
import numpy as np
import math as m

CL_d = 0.4
AR   = 8
P_Area = 3.5
e      = 0.5
k      = 0.22

AOA_d  = np.arange((180/m.pi),(6*180/m.pi),(180/m.pi))
L      = len(AOA_d)
AOA_l0 = np.arange((-4*180/m.pi),(1*180/m.pi),(180/m.pi))
l      = len(AOA_l0)

#lift coefficient and AOA arrays
CL_aoa = np.zeros((L,l))
Cl_aoa = np.zeros((L,l))
CL0    = np.zeros((L,l))
Cl0    = np.zeros((L,l))

for i in range (L):
    
    for j in range (l):
        
        CL_aoa[i,j] = CL_d/(AOA_d[i]-AOA_l0[j])
        Cl_aoa[i,j] = CL_aoa[i,j]/(1-(k*CL_aoa[i,j]))
        CL0[i,j]    = (-CL_aoa[i,j])*(AOA_l0[j])
        Cl0[i,j]    = (-Cl_aoa[i,j])*(AOA_l0[j])
        
        