__author__ = 'Fabio'
import shapefile
import utm
#r = shapefile.Reader("../dati/MSCities_Geo_Pts/MSCities_Geo_Pts")
#print r.bbox,"\n",r.numRecords
#fieldNames = [item[0] for item in r.fields[1:]]
#name10 = fieldNames.index(("NAME10"))
#for rec in enumerate(r.records()[:3]):
#    print (rec)[0]+1,": ",rec[1]
#counter = 0
#for rec in r.iterRecords():
#    counter +=1
#geom = r.shape(0)
#print geom.points

r = shapefile.Reader("../dati/NYC_MUSEUMS_LAMBERT/NYC_MUSEUMS_GEO")
w = shapefile.Writer(r.shapeType)
w.fields = list(r.fields)
w.records.extend(r.records())
for s in r.iterShapes():
    lon,lat = s.points[0]
    y,x,zone,band = utm.from_latlon(lat,lon)
    w.point(x,y)
w.save("../dati/NYC_MUSEUMS_LAMBERT/NYC_MUSEUMS_UTM")

rAddField = shapefile.Reader("../dati/NYC_MUSEUMS_LAMBERT/NYC_MUSEUMS_UTM")
wAddField = shapefile.Writer(rAddField.shapeType)
rAddField.fields = list(rAddField.fields)
wAddField.records.extend(rAddField.records())
wAddField.field("LAT","F",8,5)
wAddField.field("LON","F",8,5)
geo = shapefile.Reader("../dati/NYC_MUSEUMS_LAMBERT/NYC_MUSEUMS_GEO")
for i in range(geo.numRecords):
    lon,lat = geo.shape(i).points[0]
    w.records[i].extend([lat,lon])
w._shapes.extend(rAddField.shapes())
w.save("../dati/NYC_MUSEUMS_LAMBERT/NYC_MUSEUMS_UTM")
