# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 08:20:45 2022

@author: gen
"""


# def foo(x: str, y: int) -> str:  # добавил АННОТАЦИИ локальных переменных
#     x[0] = y        # меняет a !!!
#     x = [4, 5, 6]   # не меняет a !!!
#     # return(x)     # А ТАК меняет a !!!


# if __name__ == '__main__':  # добавил, чтобы то, что ниже, не выполнялось при импорте МОДУЛЯ
#     a = [1, 2, 3]
#     foo(a, 7)           # не меняет a !!!
#     # a=foo(a, 7)       # А ТАК меняет a !!!
#     # foo(y=7, x=a)     # именованные параметры !!!
#     print(a)

# def fo(x, y, z=0):        # параметр по умолчанию
#     result=100*x+10*y+z
#     return result


# z1=fo(3, 2, 1)
# print(fo(3, 2, 1))

# z2=fo(3, 2)
# print(fo(3, 2))

def bar(*args, named_parameter="FISH"):
    for arg in args:
       # print(arg)
        print(named_parameter, 'arg=', arg)


#bar([1, 2, 3,], 77, 'str___', 5)
bar('1', '2', 'qwerty', named_parameter='bar')
