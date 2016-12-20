__author__ = 'Fabio'

from osgeo import ogr
driver = ogr.GetDriverByName('WFS')
wfs = driver.Open("WFS:http://geohub.jrc.ec.europa.eu/effis/ows")
for i in range(0, wfs.GetLayerCount()):
    layer = wfs.GetLayerByIndex(i)
    sr = layer.GetSpatialRef()
    print 'Layer: %s, Features: %s, SR: %s...' % (layer.GetName(), layer.GetFeatureCount(), sr.ExportToWkt()[0:50])
