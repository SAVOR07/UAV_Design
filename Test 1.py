# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 01:25:05 2024

@author: SAVOR

import numpy as np
  
b = np.empty(0, dtype = float) 
print("Matrix b : \n", b) 

arr = np.array([1,2,3,47,1,0,2])
arr=np.append(arr, 4)
print(arr)

import numpy as np

M = np.arange(10,16,0.4)
print(M)
i=0
for x in M:
    print (M[i])
    i=i+1"""
    
import numpy as np
import matplotlib.pyplot as plt

a=float(9)
b=float(15)
c=float(1)
arr=np.empty(0,dtype=float)
ar=np.empty(0,dtype=float)

L_by_D = np.arange(10,16,1)
i=0
for x in L_by_D:
    while (abs(a-b))>pow(10,-2):
        b=b-c
        d=L_by_D[i]
        a=L_by_D[i]
        print(b)
        print(L_by_D[i])
    
    print(L_by_D[i])
    arr=np.append(arr,b)
    ar=np.append(ar,d)
    a=float(9)
    b=float(15)
    i=i+1

print(arr)

fig, plot1 = plt.subplots()
plot1.plot(L_by_D,arr)
plot1.plot(L_by_D,ar)
plot1.set_xlabel("L/D")
plot1.set_ylabel("a & b")
plt.show()