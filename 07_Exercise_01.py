#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 23:14:29 2022

@author: Evren Arslan

"""
import numpy as np
import matplotlib.pyplot as plt


class Consumer:
    
    def __init__(self,w):
        "Initialize consumer with w dollars of wealth"
        self.wealth=w
    
    def earn(self,y):
        "The consumer earns y dollars"
        self.wealth += y
    
    def spend(self,x):
        "The consumer spends x dollars if feasible"
        new_wealth=self.wealth-x
        if new_wealth<0:
            print("Insufficent funds")
        else:
            self.wealth=new_wealth
    
    