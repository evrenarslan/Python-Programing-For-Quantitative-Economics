#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:23:28 2022

@author: Evren Arslan
Task: Calculate pi use montecarlo method
"""
import numpy as np

n=10000000

count=0
for i in range(n):
    u,v =np.random.uniform(),np.random.uniform()
    d=np.sqrt((u-0.5)**2+(v-0.5)**2)
    if d<0.5:
        count+=1
    area_estimate=count/n
print(area_estimate*4)
