#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 18:30:53 2022

@author: Evren Arslan
"""
from sympy import Symbol

x,y=Symbol("x"),Symbol("y") # x ve y'nin değişken gibi değil cebir sembolleri gibi davranmasını sağlar

print("*******************************")
print(x+x+x+y+y)

# Cebir ifadeleri üzerinde operasyon yapabiliriz.

expression=(x+y)**2

print("*******************************")
print(expression.expand())
print("*******************************")

# Polinom çözümü yapılabilir.

from sympy import solve

denklem=x**2+x+2
cozum=solve(denklem)

print(cozum)
print("*******************************")

# limit, türev ve integral hesabı yapılabilir.

from sympy import limit, sin, diff

print(limit(1/x,x,0))
print("*******************************")

print(limit(sin(x)/x,x,0))
print("*******************************")

print(diff(sin(x),x))
print("*******************************")