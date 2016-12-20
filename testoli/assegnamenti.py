'''
Created on Mar 21, 2014
@author: lanalfa
'''
index = 0
fruit = 'banana'
while index<len(fruit):
    letter = fruit[index]
    print letter
    index = index + 1
    
prefixes = 'JKLMNOPQ'
suffix = 'ack'

print fruit[2:6]

print

for letter in prefixes:
    if letter=='Q':
        print 'Qu' + suffix
    elif letter == 'O':
        print letter + 'ak'
    else:  
        print letter + suffix


def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

print

indice = find('fabio','x')
if (indice!=-1):
    print "La lettera e' " + str(indice)
else:
    print "Lettera non trovata"
    
index = fruit.find("n")
print index