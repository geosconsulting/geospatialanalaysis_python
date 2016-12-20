'''
Created on 17/feb/2014
@author: Fabio
'''

from osgeo import ogr
shp= ogr.Open("../dati/point/point.shp")
layer= shp.GetLayer()
feature = layer.GetNextFeature()
for feature in layer:
    geometry = feature.GetGeometryRef()
    print geometry.GetX(),geometry.GetY(),feature.GetField("FIRST_FLD")