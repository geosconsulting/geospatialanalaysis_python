'''
Created on Mar 20, 2014
@author: lanalfa
'''
from osgeo import ogr
import os

inShapeFile = 'D:\\data_dir\\data\\shapefiles\\states.shp'
inDriver = ogr.GetDriverByName("ESRI Shapefile")
inDataSource = inDriver.Open(inShapeFile,0)
inLayer = inDataSource.GetLayer()
extent = inLayer.GetExtent()

geomcol = ogr.Geometry(ogr.wkbGeometryCollection)
for feature in inLayer:
    geomcol.AddGeometry(feature.GetGeometryRef())

convexhull = geomcol.ConvexHull()

outShapeFile = 'D:\\states_convexhull.shp'
outDriver =  ogr.GetDriverByName("ESRI Shapefile")

if os.path.exists(outShapeFile):
    outDriver.DeleteDataSource(outShapeFile)

outDataSource = outDriver.CreateDataSource(outShapeFile)
outLayer = outDataSource.CreateLayer("states_convexhull",geom_type=ogr.wkbPolygon)

idField = ogr.FieldDefn("id",ogr.OFTInteger)
outLayer.CreateField(idField)

featureDefn = outLayer.GetLayerDefn()
feature = ogr.Feature(featureDefn)
feature.SetGeometry(convexhull)
feature.SetField("id",1)
outLayer.CreateFeature(feature)

inDataSource.Destroy()
outDataSource.Destroy()