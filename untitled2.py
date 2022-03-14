# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 08:48:18 2022

@author: gen
"""

# name = input("Как тебя зовут?")
# print(f"Привет, {name}")


# x=10
# while True:
#     x -= 1
#     if x <= 0:
#         break
#     print (x)
# print("that's all")

# x=10
# while x > 1:
#     x -= 1
#     print (x)
# print("that's all")

# for x in range(1,10,2):
#     print (x)

# x, y, z = 1, 2, 3
# x, y, z = z, x, y
# t = 1, 2, 3, 4, 5
# t2 = 5, 4, 3, 2, 1
# z = t*2
# a, b, *e = t2
# *a, d = e
# print(*t)
# print(*e)
# e[0] = 'abc'
# # t[0] = 33 TypeError: 'tuple' object does not support item assignment
# t = 'abcde', 2, 3, 4, 5
# print(*t)
# print(t[0])
# print(e[0])
# gen = 'Genn', 5
# gen.append(77)
 
s={'a', 'b', 'cc' }
s.add('c')
if 'd' in s:
    print('c' in s)
else:
    print('False')
    
for el in s:
    print(el)