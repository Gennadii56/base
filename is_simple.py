# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 10:08:30 2022

@author: gen
"""
"""
def is_simple_number(x):
    #является ли число простым """
  
""" 
divisor = 2
    while divisor < x:
        if x%divisor == 0:
            return False
        divisor += 1
    return True   

def factorize_number(x):
    divisor = 2
    while x > 1:
        if x%divisor == 0:
            print(divisor)
            x //= divisor
        else:
            divisor +=1
            """
            
A=[1, 2, 5, 7, 0, -7, 8, -5]
B=[]
B=[(x**2 ) for x in A if x%2==0]
print(B)