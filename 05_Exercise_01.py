#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 23:14:29 2022

@author: Evren Arslan

Part 1: Given two numeric lists or tuples x_vals and y_vals of equal length, 
compute their inner product using zip().
Part 2: In one line, count the number of even numbers in 0,…,99.
• Hint: x % 2 returns 0 if x is even, 1 otherwise.
Part 3: Given pairs = ((2, 5), (4, 2), (9, 8), (12, 10)), count the number of
pairs (a, b) such that both a and b are even.
"""

#Part 1
x_vals=[2,5,6,3,11]
y_vals=[8,4,2,3,7]

print(sum(x*y for x,y in zip(x_vals,y_vals)))

#Part 2
test=sum([x%2==0 for x in range(100)])
print(test)

#Part 3
pairs = ((2, 5), (4, 2), (9, 8), (12, 10))

ciftler=sum([x%2==0 and y%2==0 for x,y in pairs])
print("Çiftlerin sayısı=",ciftler)


