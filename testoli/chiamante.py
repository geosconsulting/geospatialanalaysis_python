'''
Created on 17/feb/2014
@author: Fabio
'''
from testoli import chiamata

laMiaBici = chiamata.bicicletta("rossa",61,10,2)
laMiaBici2 = chiamata.bicicletta("nera",56,9,3)

def stampaCaratteristiche(bici):
    print bici.colore
    print bici.moltipliche
    print bici.paccoPignoni

stampaCaratteristiche(laMiaBici)
stampaCaratteristiche(laMiaBici2)
