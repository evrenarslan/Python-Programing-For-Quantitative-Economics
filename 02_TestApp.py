#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 19:11:28 2022

@author: Evren Arslan
"""

import numpy as np
import matplotlib.pyplot as plt

# Tekrar aynı random rakamları yaratmak için seed kullanacağız

np.random.seed(368546)

# Compute pie slices

N=20
Theta=np.linspace(0.0, 2*np.pi,N,endpoint=False)
radii=10*np.random.rand(N)
width=np.pi/4*np.random.rand(N)
colors=plt.cm.viridis(radii/10.)

ax=plt.subplot(111, projection='polar')
ax.bar(Theta,radii,width=width,bottom=0.0,color=colors,alpha=0.5)

plt.show()

# Random graph

rlist=np.random.randn(100)
plt.plot(rlist)
plt.show()

# Interest rate graph 

r=0.025 # Interest rate
T=50 # End date
b=np.empty(T+1) # Create a empty numpy array
b[0]=10 # Initial balance

for t in range(T):
    b[t+1]=(1+r)*b[t]
    
plt.plot(b,label="Bank Balance")
plt.legend()
plt.show()

# Başta boş dahi olsa bir array yaratmak ve o değişken için memory üzerinde
# yer ayırmak anlamına gelir. Buda append ederken performansa olumlu etkisi olur.