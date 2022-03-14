# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 13:37:03 2022

@author: gen
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
#from sklearn.metrics import matthews_corrcoef
# X is the 10x10 Hilbert matrix
X = 1. / (np.arange(1, 11) + np.arange(0, 10)[:, np.newaxis])
#print(X[:,0])
#print(X[:,1])
#print( 1. / (np.arange(1, 11) ))
y = np.ones(10)
R1 = np.corrcoef(X)
#print(R1)
# #############################################################################
# Compute paths
 
plt.imshow(R1,vmin=0.8,vmax=1)
plt.colorbar()
plt.show()


n_alphas = 200
alphas = np.logspace(-10, -2, n_alphas)

coefs = []
for a in alphas:
    ridge = linear_model.Ridge(alpha=a, fit_intercept=False)
    ridge.fit(X, y)
    coefs.append(ridge.coef_)

# #############################################################################
# Display results

"""ax = plt.gca()

ax.plot(alphas, coefs)
ax.set_xscale('log')
ax.set_xlim(ax.get_xlim()[::-1])  # reverse axis
plt.xlabel('alpha')
plt.ylabel('weights')
plt.title('Ridge coefficients as a function of the regularization')
plt.axis('tight')
plt.show()"""