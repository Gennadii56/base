# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 09:22:55 2022

@author: gen
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
  
ci = [0.01, 0., 0., 0.0156613949, 0.00237, 0.]
 
def func(c, t):
    a, A, b, B, d, D = c
    #a, b, d, A, B, D = c # Correct order of arguments?
    p2 = np.pi ** 2
    n = np.linalg.norm([a, b, d])
    q = (n - 3 / 4) / n
    res = [A, -4 * p2 * q * a, B, -4 * p2 * q * b, D, -4 * p2 * q * d - p2]
    return res
     
  
def solver(t, pinit):
    return odeint(func, pinit, t)
  
  
time = np.arange(0, 500.0, 0.01)
solution = solver(time, ci)
plt.plot(solution[:,0], solution[:,2])
plt.show()