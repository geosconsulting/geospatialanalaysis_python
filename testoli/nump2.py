'''
Created on Mar 4, 2014
@author: lanalfa
'''

import numpy as np

a = np.array([[4, 2, 0], [9, 3, 7], [1, 2, 1]],float)
vals,vecs = np.linalg.eig(a)

print vals
print vecs

b = np.array([[4, 2, 0], [9, 3, 7], [1, 2, 1]],float)
print b
print np.linalg.det(b)