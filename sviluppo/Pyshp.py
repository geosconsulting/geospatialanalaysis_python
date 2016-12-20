__author__ = 'Fabio'

import shapefile
shp = shapefile.Reader("../dati/point/point")

for feature in shp.shapeRecords():
    point = feature.shape.points[0]
    rec = feature.record[0]
    print point[0],point[1],rec
