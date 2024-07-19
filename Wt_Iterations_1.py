"""
Weight Estimation Script
Inputs from Historical Data and Design Requirements
"""
#Import
import numpy as np
import matplotlib.pyplot as plt
#Defining Variables
"""
Wt0 = float(input("Ideal Total Weight of UAV in kg: "))
E = float(input("\nIdeal Endurance of UAV in minutes: "))
R = float(input("\nIdeal Range of UAV in km: "))
V0 = float(input("\nIdeal cruise velocity in m/s: "))
Hc = float(input("\nIdeal cruise altitude in m from MSL: "))
Wpl = float(input("\nPayload weight in kg: "))
L_by_D = float(input("\nL/D: "))
SED = float(input("\nSpecific Energy Density in Wh/kg: "))
Wst_by_Wt0 = float(input("\nStructural Weight Fraction: "))
Wpro_by_Wt0 = float(input("\nPropulsion Weight Fraction: "))
Wt1=0
"""

Wt0 = float(20)
E = float(2.2)
R = float(110)
V0 = float(30)
Hc = float(800)
Wpl = float(6)
L_by_D = np.arange(10,16,0.5)
SED = float(170)
Wst_by_Wt0 = float(0.3)
Wpro_by_Wt0 = float(0.08)
Wt1=float(0)

#Arrays for data collection
Wt0_arr=np.empty(0,dtype=float)
Wb_arr=np.empty(0,dtype=float)

print("Code Started!\n")
#Getting Battery Weight from Weight Equation
#Eqs for Step 1

#Iterating Variables
WT0 = float(5)
i=0
for x in L_by_D:
    while abs(WT0-Wt1)>pow(10,-14):
        WT0 = Wt0
        PR = (WT0*9.81*V0)/(L_by_D[i])
        ER = PR*E
        Wb = ER/SED
        Wb_by_Wt0 = Wb/WT0
        Wt0 = Wpl/(1-(Wb_by_Wt0+Wst_by_Wt0+Wpro_by_Wt0))
        Wt1 = WT0
    Wt0_arr=np.append(Wt0_arr,Wt0)
    Wb_arr=np.append(Wb_arr,Wb)
    
    i=i+1
    
fig, plt1=plt.subplots()
plt1.plot(L_by_D,Wb_arr)
plt1.plot(L_by_D,Wt0_arr)

print("\nWeight of battery is iterated and came out to be "+ str(Wb) +" kg\n")
print("step 1 complete")

print("\nIterating for the propulsion fraction by choosing a propulsion unit\n")
print("Select the powerplant as per the energy required\nEnergy required is "+ str(PR) +" J\n")

#Motor_Spec = str(input("Type in the motor name selected\n"))
#Wpro = float(input("Enter weight of motor: "))
Motor_Spec = str("AT5330")
Wpro = float(0.9)
print("weight of the AT5330 T-motor chosen for the UAV is 900 grams\n")

Wpro_by_Wt0 = Wpro/Wt0

Wt0 = Wpl/(1-(Wb_by_Wt0+Wst_by_Wt0+Wpro_by_Wt0))
print(Wt0)

#Init the while loop
i=0
WT0=Wt0
for x in L_by_D:
    
    while abs((WT0-Wt1))>pow(10,-14):
        PR = (WT0*9.81*V0)/(L_by_D[i])
        ER = PR*E
        Wb = ER/SED
        Wb_by_Wt0 = Wb/WT0
        Wt0 = Wpl/(1-(Wb_by_Wt0+Wst_by_Wt0+Wpro_by_Wt0))
        Wt1 = Wt0
    print("Total weight of the UAV is "+str(Wt0)+" kg\n")
    Wt0_arr=np.append(Wt0_arr,Wt0)
    Wb_arr=np.append(Wb_arr,Wb)
    
    i=i+1
