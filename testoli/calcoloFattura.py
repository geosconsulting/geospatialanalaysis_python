'''
Created on 17/feb/2014
@author: Fabio
'''
class calcolo_fattura:
    IVA = 0.2
    INARCASSA= 0.04

    def calcoloIVA(self,imp):
        imponbileCalcolato = imp * self.IVA
        return (imp + imponbileCalcolato)

    def calcoloINARCH(self,imp,calc):
        inarcassaCalcolato = calc * self.IVA
        return imp+ inarcassaCalcolato

calcolo1000 = calcolo_fattura()
calcolato = calcolo1000.calcoloIVA(1000.0)
#print calcolato
print calcolo1000.calcoloINARCH(calcolato,calcolato)