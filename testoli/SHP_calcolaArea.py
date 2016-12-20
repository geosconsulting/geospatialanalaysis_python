'''
Created on Mar 20, 2014
@author: lanalfa
'''
from osgeo import ogr

inShapeFile = 'D:\\_Appoggio\\geo robba\\dati\\dati shp\\european_countries\\european_countries_export.shp'
inDriver = ogr.GetDriverByName("ESRI Shapefile")
inDataSource = inDriver.Open(inShapeFile,0)
inLayer = inDataSource.GetLayer()
extent = inLayer.GetExtent()

#numFeature = len(inLayer)
numFeature = inLayer.GetFeatureCount()

for indice in range(0,numFeature):
    feature = inLayer.GetFeature(indice)
    geometry = feature.GetGeometryRef()
    print "Area %.2f" % geometry.GetArea()

inDataSource.Destroy()
