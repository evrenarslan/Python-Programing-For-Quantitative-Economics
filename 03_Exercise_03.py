#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 21:39:14 2022

@author: Evren Arslan
Task: alpha=[0.0,0.8,0.98]-T=200-R:Rand(T)- X0=0 için Xt+1=alpha*Xt+Rt  grafiğini çizdirelim.
For absolute values
"""
import numpy as np
import matplotlib.pyplot as plt

alp=[0.0,0.8,0.98]
T=200

R=np.random.randn(T)
arrayT=np.empty(T+1)


for a in alp:
    arrayT[0]=0
    for t in range(T):
        arrayT[t+1]=a*np.abs(arrayT[t])+R[t]
    etiket="Seri_"+str(i)
    plt.plot(arrayT, label=etiket)
plt.legend()
plt.show()
