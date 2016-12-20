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

print extent

ring = ogr.Geometry(ogr.wkbLinearRing)
ring.AddPoint(extent[0],extent[2])
ring.AddPoint(extent[1],extent[2])
ring.AddPoint(extent[1],extent[3])
ring.AddPoint(extent[0],extent[2])
poly = ogr.Geometry(ogr.wkbPolygon)
poly.AddGeometry(poly)

outShapefile = "d:\\states_extent.shp"
outDriver =  ogr.GetDriverByName("ESRI Shapefile")

if os.path.exists(outShapefile):
    outDriver.DeleteDataSource(outShapefile)

outDataSource = outDriver.CreateDataSource(outShapefile)
outLayer = outDataSource.CreateLayer("states_extent",geom_type=ogr.wkbPolygon)

idField = ogr.FieldDefn("id",ogr.OFTInteger)
outLayer.CreateField(idField)

featureDefn = outLayer.GetLayerDefn()
feature = ogr.Feature(featureDefn)
feature.SetGeometry(poly)
feature.SetField("id",1)
outLayer.CreateFeature(feature)

inDataSource.Destroy()
outDataSource.Destroy()