'''
Created on Feb 24, 2014
@author: lanalfa
'''
import glob
import shapefile

files = glob.glob("../dati/tiled_footprints/footprints_*shp")
w = shapefile.Writer()
r = None
for f in files:
    r = shapefile.Reader(f)
    w._shapes.extend(r.shapes())
    w.records.extend(r.records())
w.fields = list(r.fields)
w.save("../dati/tiled_footprints/Merged")
