'''
Created on Feb 28, 2014
@author: lanalfa
'''

import numpy as np

laLista = [12,22,34,11,56,78]
print laLista[3:]
print laLista[:2]

laLista1 = [[12,22,34,11,56,78],[33,1,87,23,22,99]]
print laLista1[1:]
print laLista1[:2]


a = np.array([1,4,5,8,2,9],float)
print type(a)
laListaDalloArray = a.tolist()
print type(laListaDalloArray)
print a[1:3]

b = np.array(laLista1,float)
print b[1,:]
print b[:,2]

#prima serie
illo= b[0,:]

#seconda serie
illa= b[1,:]
print b.shape

dTrasposto = b.transpose()
print b
print dTrasposto

cComeBAppiattito = b.flatten()
print cComeBAppiattito

c = np.array([3,24,11,28,22,66],float)
eConcatenatoDaAltriArray = np.concatenate((a,c))
print eConcatenatoDaAltriArray

arrayiuccio = np.arange(5,dtype=float)
print arrayiuccio

arrayiuccioTuttiZeri = np.zeros(7,dtype=int)
print arrayiuccioTuttiZeri

comeBmaTuttiZeri = np.zeros_like(cComeBAppiattito)
comeBmaTuttiUno = np.ones_like(cComeBAppiattito)

print comeBmaTuttiZeri
print
print comeBmaTuttiUno
print
print
print np.identity(4, dtype=float)
print
print
print np.eye(4,k=1, dtype=float)

print a+c
print a-c
print a*c
print a/c
LaRadiceDellaMatrice= np.sqrt(c)
print LaRadiceDellaMatrice
print np.floor(LaRadiceDellaMatrice)
print np.ceil(LaRadiceDellaMatrice)
print np.rint(LaRadiceDellaMatrice)

print
print

for x in c:
    print x

print
print
   
print a.sum()
print b.sum()
print b.mean() 
print b.std()
print b.min()
print b.max()
print b.argmin()
print b.argmax()

#a.sort()
#print a

print np.where(a>4)

g = np.array([[6,4],[5,9]],int)
sel = (g>=6)
print g[sel]

print g[np.logical_and(g > 5, g < 9)]

h = np.array([2,4,6,8],float)
j = np.array([0,0,1,3,2,1],int)
print h[j] 
h.take(j,axis=0)

k = np.array([[0,0],[1,1]],float)
l = np.array([0,2,2],int)
buzzolo = k.take(l)
print buzzolo

m = np.array([0, 1, 2, 3, 4, 5], float)
print m 
m.put([0, 3], 5)
print m

n = np.array([[4, 2, 0], [9, 3, 7], [1, 2, 1]],float)
print n
print np.linalg.det(n)