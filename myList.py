# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 21:29:54 2022

@author: gen
"""
"""Li=[0]*11
for i in range (9):
    print(i)
    Li[i] = i
print(Li)"""

import numpy as np
# import array as arr
F=[0]*10
print(F)
#Generate 100 random numbers between 0 and 10
rng = np.random.default_rng(12345)
N = rng.integers(low=0, high=10, size=100)
print(N)
NN=len(N)
print(NN)
for i in range(NN):
   F[N[i]] = F[N[i]] + 1
print(F)

    
    
    