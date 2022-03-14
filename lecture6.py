# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 10:59:14 2022

@author: gen
"""

def insert_sort(A):
    """ сортировка вставками """
    N=len(A)
    for top in range (1, N):
        k=top
        while k>0 and A[k-1] > A[k]:
            A[k], A[k-1]=A[k-1], A[k]
            k -= 1

def test_sort(sort_algo):
    print("Тестируем: ", sort_algo.__doc__)
    A=[4, 2, 5, 1, 3]
    A_sorted=list(range(1,6))
    sort_algo(A)
    print("Ok" if A==A_sorted else "Fail")
    
#if __name__=="__main__"
test_sort(insert_sort)