# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 09:12:22 2022

@author: gen
"""

from scipy.integrate import solve_ivp # Recommended initival value problem solver
from scipy.interpolate import interp1d # 1D interpolation
from scipy.optimize import brentq # Root finding method in an interval
exponential_decay = lambda t, y: -0.5 * y # dy/dt = f(t, y)
t_span = [0, 10] # Interval of integration
y0 = [2] # Initial state: y(t=t_span[0])=2
desired_answer = 0.59
sol_ode = solve_ivp(exponential_decay, t_span, y0) # IVP solution
f_sol_ode = interp1d(sol_ode.t, sol_ode.y) # Build interpolated function
brentq(lambda x: f_sol_ode(x) - desired_answer, t_span[0], t_span[1])