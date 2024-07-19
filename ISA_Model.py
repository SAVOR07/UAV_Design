# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 17:59:33 2024

@author: SAVOR
"""

#Density Calculator at an altitude script

#Mathematical Model for Design of Fixed Wing UAVs
#As this model is for Fixed wing UAVs, need not to consider the geometric and geopotential altitude delta, approximately same can be considered.
#Imports
import math as m

#Input
#Must need the altitude at which the UAV is supposed to be cruising, accordingly temp, pressure & density parameters can be calculated using the model.
print("This is a Mathematical Model for getting the atmospheric values at an altutude h\nPlease note that the units are as follows:\nAltitude in meters\nPressure is in K-Pa\nDensity is in kg/cu m\n")

#Inputs:
h = float(input("Enter the altitude of level flight(Cruise) in meters: \n"))
P = float()
T = float()
rho = float()

#Standard values:
def ISA_Model(h):
    
    
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
        print("\nTemperature: "+str(round(T,4))+" °C\n")
        print("Pressure: "+str(round(P,4))+" K-Pa\n")
        print("Density: "+str(round(rho,4))+" Kg/cu m\n")
        
        return ()