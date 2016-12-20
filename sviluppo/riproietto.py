__author__ = 'Fabio'

import ogr
import osr
import os
import shutil

srcName = "../dati/NYC_MUSEUMS_LAMBERT/NYC_MUSEUMS_LAMBERT.shp"
tgtName = "../dati/NYC_MUSEUMS_LAMBERT/NYC_MUSEUMS_GEO.shp"

tgt_spatRef = osr.SpatialReference()
tgt_spatRef.ImportFromEPSG(4326)

driver = ogr.GetDriverByName("ESRI Shapefile")
src    = driver.Open(srcName,0)
srcLyr = src.GetLayer()

src_spatRef = srcLyr.GetSpatialRef()

if os.path.exists(tgtName):
    driver.DeleteDataSource(tgtName)

tgt = driver.CreateDataSource(tgtName)
lyrName = os.path.splitext(tgtName)[0]
tgtLyr = tgt.CreateLayer(lyrName,geom_type = ogr.wkbPoint)

featDef = srcLyr.GetLayerDefn()

trans = osr.CoordinateTransformation(src_spatRef,tgt_spatRef)

srcFeat = srcLyr.GetNextFeature()
while srcFeat:
    geom = srcFeat.GetGeometryRef()
    geom.Transform(trans)
    feature = ogr.Feature(featDef)
    feature.SetGeometry(geom)
    tgtLyr.CreateFeature(feature)
    feature.Destroy()
    srcFeat.Destroy()
    srcFeat = srcLyr.GetNextFeature()
src.Destroy()
tgt.Destroy()

tgt_spatRef.MorphToESRI()
prj = open(lyrName + ".prj","w")
prj.write(tgt_spatRef.ExportToWkt())
prj.close()
srcDbf = os.path.splitext(srcName)[0] + ".dbf"
tgtDbf = lyrName + ".dbf"
shutil.copyfile(srcDbf,".dbf")