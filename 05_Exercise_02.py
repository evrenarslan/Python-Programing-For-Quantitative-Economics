#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 23:16:34 2022

@author: Evren Arslan

Consider the polynomial

𝑝(𝑥) = 𝑎0 + 𝑎1 𝑥 + 𝑎2 𝑥 + ⋯ 𝑎𝑛 𝑥 = ∑ 𝑎𝑖 𝑥𝑖
𝑖=0
Write a function p such that p(x, coeff) that computes the value in  
given a point x and a list of coefficients coeff.
Try to use enumerate() in your loop.
"""

def p(x,coeff):
    return sum([a * x**i for i, a in enumerate(coeff)])

print(p(2,(2,4,6)))


