'''
Created on Mar 4, 2014
@author: lanalfa
'''

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print a+b,a-b,a*b,a/b
print a.min(),a.max(),b.min(),b.max()
print np.shape(a),np.shape(b)