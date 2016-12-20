'''
Created on Mar 19, 2014
@author: lanalfa
'''

import os
import sys

print os.getcwd()
print sys.version
print sys.getwindowsversion()

print dir()

import operazioni as ca

print ca.somma(12,4)
print ca.sottrazione(12,4)
print ca.divisione(12,4)
print ca.moltiplicazione(12,4)

a,b=5,0

try:
    print a/b
except:
    print "non si puo dividere per 0"

euro = [2.5,3.7,20.9]
dollaro = [x*1.3 for x in euro if x>5.0]
print dollaro

y = [1,2,3,4]
dictComp={z:z+100 for z in y if z>2}
print dictComp

def func(lista,num):
    lista.append(10)
    num = num + 3
    return lista,num

x = [1,2]
y=4

print func(x,y)

def func1(lista1,num1):    
    lista2=[]
    for elem in lista1:
        elem = elem + num1
        lista2.append(elem)        
    return lista2

x1 = [10,15,20]
y1 = 12

print func1(x1,y1)