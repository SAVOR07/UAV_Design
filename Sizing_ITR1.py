# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 23:28:37 2024

@author: SAVOR
"""
import numpy as np
import matplotlib.pyplot as plt
import Wt_Iterations_trial_2 as WT_ITR2
import density as rho
import math as m

#w=float(input("\nAnalyse the graphs and finalise a weight configuration along with the L/D value: "))
#l_by_d=float(input("\nEnter the L/D value corresponding to the weight configuration selected!: "))
h=float(800)
w=float(20.1658)
Wn=float(w*9.81)
l_by_d=float(15)
TR=float(0.4)

V=WT_ITR2.V_icruise
rho = rho.density(h)

AR=np.arange(4,10,0.5)
WbyS=np.arange(4,10,0.5)

#1D ARRAY
ar=[0]*len(AR)
e=[0]*len(AR)
k=[0]*len(AR)
#2D ARRAY
wBYs=[[0]*len(AR)]*len(AR)
CL_d=[[0]*len(AR)]*len(AR)
S=[[0]*len(AR)]*len(AR)
b=[[0]*len(AR)]*len(AR)
Cr=[[0]*len(AR)]*len(AR)
Ct=[[0]*len(AR)]*len(AR)
CD_d=[[0]*len(AR)]*len(AR)
CD0=[[0]*len(AR)]*len(AR)

j=0
for x in AR:
    ar[j]=x
    e[j]=((1.78*(1-(0.045*(x**0.68))-0.64)))
    k[j]=1/(m.pi*e[j]*x)
    i=0

    for y in WbyS:
        wBYs[i][j]=y
        CL_d[i][j]=(2*y*9.81)/(rho*(V**2))
        S[i][j]   = w/y
        b[i][j]   = m.sqrt(x*(S[i][j]))
        Cr[i][j]  = (2*(S[i][j]))/((b[i][j])*(1+TR))
        Ct[i][j]  = (Cr[i][j])*TR
        CD_d[i][j]= (CL_d[i][j])/(l_by_d)
        CD0[i][j] = CD_d[i][j]-((k[j])*(CL_d[i][j]**2))
        
print('All set!')