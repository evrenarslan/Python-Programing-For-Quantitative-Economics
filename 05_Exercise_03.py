#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 23:17:51 2022

@author: Evren Arslan

Write a function that takes a string as an argument and returns the number of 
capital letters in the string.
Hint: 'foo'.upper() returns 'FOO'
"""
def f_upper(kelime):
    count=0
    for letter in kelime:
        if letter==letter.upper() and letter.isalpha():
            count+=1
    return count

print(f_upper("Evren Arslan"))

print(f_upper("Evren ArslaN"))

print(f_upper("Evren ArslaN 35"))
