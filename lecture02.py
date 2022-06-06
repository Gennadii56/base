# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 12:15:56 2022

@author: gen
"""

flag=False
N=int(input())
print(N)

for i in range(N):
    x=int(input())
    flag=(x%10==0)or flag
    print(flag)
    