#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 19:43:19 2022

@author: Evren Arslan
Task: alpha=0.9-T=200-R:Rand(T)- X0=0 için Xt+1=alpha*Xt+Rt  grafiğini çizdirelim.
"""
import numpy as np
import matplotlib.pyplot as plt

Alpha=0.9
T=200

R=np.random.rand(T)

arrayT=np.empty(T+1)
arrayT[0]=0

for t in range(T):
    arrayT[t+1]=Alpha*arrayT[t]+R[t]
plt.plot(arrayT, label="Exercise 1")
plt.legend()
plt.show()



