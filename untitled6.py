# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 13:09:58 2022

@author: gen
"""

# mygenerator = (x*x for x in range(3))
# for i in mygenerator :
#     print(i)
    
# for i in mygenerator :
#     print(i)
    
# print(mygenerator)

def createGenerator() :
    mylist = range(3)
    for i in mylist :
        yield i*i


mygenerator = createGenerator() # создаём генератор
print(mygenerator) # mygenerator является объектом!

for i in mygenerator:
    print(i)