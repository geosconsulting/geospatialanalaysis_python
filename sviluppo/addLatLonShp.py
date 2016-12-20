__author__ = 'Fabio'
import shapefile
import utm
r = shapefile.Reader("../dati/NYC_MUSEUMS_LAMBERT/NYC_MUSEUMS_UTM")
w = shapefile.Writer(r.shapeType)
r.fields = list(r.fields)
w.records.extend(r.records())
wAddField.field("LAT","F",8,5)
wAddField.field("LON","F",8,5)
geo = shapefile.Reader("../dati/NYC_MUSEUMS_LAMBERT/NYC_MUSEUMS_GEO")
for i in range(geo.numRecords):
    lon,lat = geo.shape(i).points[0]
    w.records[i].extend([lat,lon])
w._shapes.extend(rAddField.shapes())
w.save("../dati/NYC_MUSEUMS_LAMBERT/NYC_MUSEUMS_UTM")
