'''
Created on Mar 19, 2014
@author: lanalfa
'''

class persona:
    nome        = ''
    cognome     =''
    indirizzo   = ''

    def cambia_indirizzo(self,s):
        self.indirizzo = s

    def stampa(self):
        print self.nome,self.cognome,self.indirizzo
        
class studente(persona):
    scuola = ''
    
    def setta_scuola(self,sc):
        self.scuola=sc
        
    def stampa(self):                    
        print self.nome,self.cognome,self.indirizzo,self.scuola
    

p1 = persona()
p1.nome='Fabio'
p1.cognome='Lana'
p1.indirizzo='Via Corta'

p1.cambia_indirizzo("Via Lunga")
p1.stampa()

s1 = studente()
s1.nome='Vittoria'
s1.cognome='Lana'
s1.indirizzo='Via Carlo Follini'
s1.setta_scuola("Calderini Tuccimei")

s1.stampa()

for x in range(1,11):
    print repr(x).rjust(2),repr(x*x).rjust(3),
    print repr(x*x*x).rjust(4)

print
import math
print math.pi

print
f = open("pippo.txt")
#print f.read()
#print f.readline()
#print f.readline()

#for line in f:
    #print line,
#print list(f)

print f.readlines()
import json

json.dump([1,'simple','list'])


