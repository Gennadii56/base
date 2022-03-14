# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 13:12:25 2022

@author: gen
"""

def factorial(n):
    assert n >= 0, "отрицат!"
    if n == 0:
        return 1
    print(n)
    #(factorial(n - 1))
    return factorial(n - 1) * n
    #print(n)
    # print(n , end='---')
    # return n * factorial(n - 1)

print(factorial(6))