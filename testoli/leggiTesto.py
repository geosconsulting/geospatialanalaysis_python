'''
Created on Feb 28, 2014
@author: lanalfa
'''

ilFile = open('../dati/testoDaLeggere.txt',"r")

ilFile.seek(6)

for linea in ilFile:
    print ilFile.tell()
    print linea


