'''
Created on Feb 28, 2014
@author: lanalfa
'''
import gdalnumeric
import numpy as np


fonte = gdalnumeric.LoadFile("../dati/thermal/thermal.tif")
classi = np.histogram(fonte)

print classi