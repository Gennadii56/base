# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 13:53:40 2022

@author: gen
"""

base=8
x=int(input())
while x > 0:
    digit = x % base
    print(digit, end='')
    x//=base
