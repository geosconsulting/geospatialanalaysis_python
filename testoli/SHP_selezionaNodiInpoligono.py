'''
Created on Mar 20, 2014
@author: lanalfa
'''
from osgeo import ogr

inFilePoligoni = 'D:\\states.shp'
inDriver = ogr.GetDriverByName("ESRI Shapefile")
inDataPoligoni = inDriver.Open(inFilePoligoni,0)
inLayerPoligoni = inDataPoligoni.GetLayer()

inFilePunti = 'D:\\dotti_stati.shp'
inDataPunti = inDriver.Open(inFilePunti,0)
inLayerPunti = inDataPunti.GetLayer()

featureCount = inLayerPunti.GetFeatureCount()
#print featureCount

for feature in inLayerPoligoni:
    if feature.GetField("STATE_NAME")=='North Dakota':
        geom = feature.GetGeometryRef()
        wkt = geom.ExportToWkt()

inLayerPunti.SetSpatialFilter(ogr.CreateGeometryFromWkt(wkt))

for feature in inLayerPunti:
    print feature.GetField("nomi")
   
inDataPoligoni.Destroy()
inDataPunti.Destroy()
