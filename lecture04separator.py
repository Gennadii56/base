# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 07:37:33 2022

@author: gen
"""
from myMax2 import max2
def hello_separated(name="World", separator="-"):
    print("Hello", name, sep=separator)
    
#hello_separated(separator="****", name="John")
hello_separated()

print(max2("ag","agf"))

def max3(x, y, z):
    return max2(x, max2(y, z))

m3=max3(5, 2, 7.1)
print(m3)