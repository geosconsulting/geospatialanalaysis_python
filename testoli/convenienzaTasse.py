'''
Created on Mar 21, 2014
@author: lanalfa
'''

pIT = 50.59/100 
pUK = 57.28/100
sIT = 48000
sUK = 50000*1.2
cIT = 31 * 39.4
cUK = 31 * 50.6

Italia      = ((pIT * sIT/12)-cIT)*12 
Inghilterra = ((pUK * sUK/12)-cUK)*12

print Inghilterra - Italia

