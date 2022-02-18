#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 23:18:31 2022

@author: Evren Arslan

Write a function that takes two sequences seq_a and seq_b as arguments and 
returns True if every element in seq_a is also an element of seq_b, else False.
• By “sequence” we mean a list, a tuple or a string.
• Do the exercise without using sets and set methods.
"""
def f_check_eq(seq_a,seq_b):
    checkSubset=True
    for a in seq_a:
        if a not in seq_b:
            checkSubset=False
    return checkSubset 

print(f_check_eq([1, 2], [1, 2, 3]))
print(f_check_eq([1, 2, 3], [1, 2]))

