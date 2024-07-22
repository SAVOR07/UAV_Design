# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 02:00:21 2024

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
L=len(AR)

#1D ARRAY
ar=np.zeros(L)
e=np.zeros(L)
k=np.zeros(L)

#2D ARRAY
wBYs=np.zeros((L,L))
CL_d=np.zeros((L,L))
S=np.zeros((L,L))
b=np.zeros((L,L))
Cr=np.zeros((L,L))
Ct=np.zeros((L,L))
CD_d=np.zeros((L,L))
CD0=np.zeros((L,L))

for j in range(L):
    e[j]=((1.78*(1-(0.045*(AR[j]**0.68))-0.64)))
    k[j]=1/(m.pi*e[j]*AR[j])
    
    for i in range(L):
        
        wBYs[j,i]=WbyS[i]
        CL_d[j,i]=(2*WbyS[i]*9.81)/(rho*(V**2))
        S[j,i]   = w/WbyS[i]
        b[j,i]   = m.sqrt(AR[j]*(S[j,i]))
        Cr[j,i]  = (2*(S[j,i]))/((b[j,i])*(1+TR))
        Ct[j,i]  = (Cr[j,i])*TR
        CD_d[j,i]= (CL_d[j,i])/(l_by_d)
        CD0[j,i] = CD_d[j,i]-((k[j])*(CL_d[j,i]*2))
        
#PLOTTING GRAPHS
fig, plot1= plt.subplots()

plt.subplot(4,1,1)
plt.plot(wBYs[1,:],CL_d[1,:], color='r', label='CL_design')

plt.subplot(4,1,2)
plt.plot(wBYs[1,:],S[1,:], color='g', label='Planform Area')

plt.subplot(4,1,3)
plt.plot(wBYs[1,:],CD_d[1,:], color='b', label='CD_design')

plt.subplot(4,1,4)
plt.plot(wBYs[1,:],CD0[1,:], color='y', label='CD0')

fig, plot2=plt.subplots()

plt.subplot(3,1,1)
plt.plot(wBYs[1,:],b[0,:], color='b', label='AR:4')
plt.plot(wBYs[1,:],b[1,:], color='r', label='AR:4.5')
plt.plot(wBYs[1,:],b[2,:], color='g', label='AR:5')
plt.plot(wBYs[1,:],b[3,:], color='b', label='AR:5.5')
plt.plot(wBYs[1,:],b[4,:], color='c', label='AR:6')
plt.plot(wBYs[1,:],b[5,:], color='m', label='AR:6.5')
plt.plot(wBYs[1,:],b[6,:], color='k', label='AR:7')
plt.plot(wBYs[1,:],b[7,:], color='w', label='AR:7.5')
plt.plot(wBYs[1,:],b[8,:], color='y', label='AR:8')
plt.plot(wBYs[1,:],b[9,:], color='w', label='AR:8.5')
plt.plot(wBYs[1,:],b[10,:], color='0.75', label='AR:9.')
plt.plot(wBYs[1,:],b[11,:], color='0.4', label='AR:9.5')


plt.subplot(3,1,2)
plt.plot(wBYs[1,:],Cr[0,:], color='b', label='AR:4')
plt.plot(wBYs[1,:],Cr[1,:], color='r', label='AR:4.5')
plt.plot(wBYs[1,:],Cr[2,:], color='g', label='AR:5')
plt.plot(wBYs[1,:],Cr[3,:], color='b', label='AR:5.5')
plt.plot(wBYs[1,:],Cr[4,:], color='c', label='AR:6')
plt.plot(wBYs[1,:],Cr[5,:], color='m', label='AR:6.5')
plt.plot(wBYs[1,:],Cr[6,:], color='k', label='AR:7')
plt.plot(wBYs[1,:],Cr[7,:], color='w', label='AR:7.5')
plt.plot(wBYs[1,:],Cr[8,:], color='y', label='AR:8')
plt.plot(wBYs[1,:],Cr[9,:], color='w', label='AR:8.5')
plt.plot(wBYs[1,:],Cr[10,:], color='0.75', label='AR:9.')
plt.plot(wBYs[1,:],Cr[11,:], color='0.4', label='AR:9.5')


plt.subplot(3,1,3)
plt.plot(wBYs[1,:],Ct[0,:], color='b', label='AR:4')
plt.plot(wBYs[1,:],Ct[1,:], color='r', label='AR:4.5')
plt.plot(wBYs[1,:],Ct[2,:], color='g', label='AR:5')
plt.plot(wBYs[1,:],Ct[3,:], color='b', label='AR:5.5')
plt.plot(wBYs[1,:],Ct[4,:], color='c', label='AR:6')
plt.plot(wBYs[1,:],Ct[5,:], color='m', label='AR:6.5')
plt.plot(wBYs[1,:],Ct[6,:], color='k', label='AR:7')
plt.plot(wBYs[1,:],Ct[7,:], color='w', label='AR:7.5')
plt.plot(wBYs[1,:],Ct[8,:], color='y', label='AR:8')
plt.plot(wBYs[1,:],Ct[9,:], color='w', label='AR:8.5')
plt.plot(wBYs[1,:],Ct[10,:], color='0.75', label='AR:9.')
plt.plot(wBYs[1,:],Ct[11,:], color='0.4', label='AR:9.5')

plt.show()