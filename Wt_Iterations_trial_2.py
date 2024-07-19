# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 19:04:04 2024

Weight Estimation Iteration for battery weight and proppulsion weight with variation of L/D from 10 to 16

@author: SAVOR
"""
import numpy as np
import matplotlib.pyplot as plt
#Lets start!

W_b = float(20)             #Baseline weight MR
E_i=float(2.2)              #Ideal Endurance MR
V_icruise=float(30)         #ideal cruise velocity MR
W_pl=float(6)               #Payload Weight MR
SED=float(170)              #Specific Energy Density HD
Wst_Wto=float(0.3)          #Structural Weight Ratio HD
Wpro_Wto=float(0.08)        #Propulsion weight Ratio HD
eff_prop=float(0.9)
eff_motor=float(0.98)
eff_elec=float(0.9)
l_by_d = np.arange(10,16,0.5)

#Empty Arrays
L_D = [0]*len(l_by_d)
W_Final=[0]*len(l_by_d)
W_BATT=[0]*len(l_by_d)
W_PRO=[0]*len(l_by_d)

#L_by_D=

    #Varying L/D from 10 to 16 to get variation plot of weights
k=0
for x in l_by_d:
    w=W_b
    L_D[k]=x
    W_STR = (Wst_Wto*w)
    W_pro = (Wpro_Wto*w)
    #i=0
    Wi=W_b
    Wf=0
    while abs(Wi-Wf)>(pow(10,(-12))):
        #i      = i+1
        Wi     = w
        Pr     = (Wi*9.81*V_icruise)/(x)
        P_batt = (Pr)/(eff_elec*eff_motor*eff_prop)
        W_batt = (P_batt*E_i)/SED
        w      = W_STR + W_pro + W_pl + W_batt
        Wf     = w
        #print(str(w)+"\n"+str(Wf)+"\n"+str(Wi)+"\n")
    
    W_STR = (Wst_Wto*w)
    W_pro= (Wpro_Wto*w)
    #i=0
    Wi=w
    Wf=0
    while abs(Wi-Wf)>(pow(10,(-12))):
        #i      = i+1
        Wi     = w
        Pr     = (Wi*9.81*V_icruise)/(x)
        P_batt = (Pr)/(eff_elec*eff_motor*eff_prop)
        W_batt = (P_batt*E_i)/SED
        w      = W_STR + W_pro + W_pl + W_batt
        Wf     = w
        #print(str(w)+"\n"+str(Wf)+"\n"+str(Wi)+"\n")
        
    W_Final[k]=w
    W_BATT[k]=W_batt
    W_PRO[k]=W_pro
    #print(W_Final)
    #print(W_BATT)
    #print(W_PRO)
    k=k+1

#I1_WtItr(W_b,E_i,V_icruise,W_pl,SED,Wst_Wto,Wpro_Wto,eff_prop,eff_motor,eff_elec,l_by_d)

plt.subplot(3,1,1)
plt.plot(l_by_d,W_BATT)
plt.ylabel("W_batt")

plt.subplot(3,1,2)
plt.plot(l_by_d,W_PRO)
plt.ylabel("W_pro")

plt.subplot(3,1,3)
plt.plot(l_by_d,W_Final)
plt.ylabel("W_f")
plt.xlabel("L/D")