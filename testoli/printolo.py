'''
Created on Mar 18, 2014
@author: lanalfa
'''

a = 12
b = 3
print (a,b,(a-b))

'''valore = input('Inserisci valore:')
print(valore*valore)'''

vettorazzo = [
    'uno',
    'diceci',
    'pingue']

print(vettorazzo[1])

laprima,elaseconda = 12,334

print elaseconda

aStringola = "FabiozzoDaForli"

print aStringola[2:4]
print aStringola[2:]
print "ciao " + aStringola
print aStringola[-2:]

print aStringola.replace("ozzo", "azzo")
print aStringola.find("ozzo")
print aStringola.upper()

aListola = [2,6,'ciao',45]
print aListola[2]

aListolaSeconda = [12,46,'come come?',"e ti ricordo ancora"]

aListolaTerza = aListola + aListolaSeconda
print aListolaTerza
print aListolaTerza[6]

print len(aListolaTerza)
aListolaTerza.insert(6,"Uzoolooolo")

print aListolaTerza
print aListolaTerza[6]

print aListolaTerza.pop(2)

aListolaTerza.sort()
print aListolaTerza

erDizzio = {}
erDizzio = {'nomePadre':'Fabio','nomeMadre':'Patricia','nomeFiglia':'Vittoria','nomeNonna':'Fiorenza'}
print erDizzio
print erDizzio['nomeNonna']

print 'nomePadre' in erDizzio
print erDizzio.get('nomeMadre')
print erDizzio.values()
print erDizzio.keys()
print erDizzio.items()
print len(erDizzio)

eChiavi = erDizzio.keys()
eChiavi.sort()
print eChiavi

eChiaviValori = erDizzio.values()
eChiaviValori.sort()
print eChiaviValori

laTuplica = (21,62,32,48)
print laTuplica[3]
print laTuplica[1:]
print laTuplica[2]*2555

output = open('pippo.txt','w')
for itemmo in erDizzio:
    #print>>output, aListolaTerza
    print>>output,itemmo

'''colorred = "\033[01;31m{0}\033[00m"
colorgrn = "\033[1;36m{0}\033[00m"'''

output = open('pippo.txt','r')
testo = output.readline()
print testo
output.close()
    
spesa={'biscotti':3,'pane':1,'pasta':3,'legumi':1}
if spesa.get('pasta')>2:
    print 'Attenzione valore pasta:', spesa.get('pasta')
elif spesa.get('biscotti')>2:
    print 'Attenzione valore biscotti:', spesa.get('biscotti')
elif spesa.get('pane')>2:
    print 'Attenzione valore pane:', spesa.get('pane')
elif spesa.get('legumi')>2:
    print 'Attenzione valore legumi:', spesa.get('legumi')
else:
    print 'Tutto ok!'
    
for i in range(2):
    print "er numero",i
    
for lettera in 'HTML.it':
    if lettera == '.':
        #pass                     # non fa nulla
        print('Punto catturato')
        continue
    print('Lettera attuale: ',lettera)   
    
