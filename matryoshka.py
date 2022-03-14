# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 12:00:22 2022

@author: gen
"""

def matryoshka(n):
    if n==1:
        print("матр1")
    else:
        print("ВЕРХматр" , n)
        print(n)
        matryoshka(n-1)
        print("НИЗматр" , n)
        print(n)
        

matryoshka(5)

print(matryoshka)