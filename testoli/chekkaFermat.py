'''
Created on Mar 20, 2014
@author: lanalfa
'''
import math

def check_fermat(a,b,c,n):
    if n>2:
        latoSinistro = math.pow(float(a),float(n)) + math.pow(float(b),float(n)) 
        latoDestro = math.pow(float(c), float(n))
        print latoSinistro,latoDestro
        if latoSinistro==latoDestro:
            print "Holy smokes, Fermat was wrong!"
        else:
            print "No, that doesn’t work."

a = raw_input("Inserisci a\n")
b = raw_input("Inserisci b\n")
c = raw_input("Inserisci c\n")
n = raw_input("Inserisci n\n")

check_fermat(a, b, c, n)