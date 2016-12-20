'''
Created on Mar 13, 2014
@author: lanalfa
'''

x = [{1,2,3},{2,3,4},{3,4,5}]
y = [{6,7,4},{9,6,7},{3,4,5}]

print set.intersection(*x)
print set.difference(x[0],x[2])
print set.union(*x)
