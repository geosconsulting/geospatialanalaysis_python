__author__ = 'Fabio'
from shapely import wkt, geometry
wktPoly = "POLYGON((0 0,4 0,4 4,0 4,0 0))"
poly = wkt.loads(wktPoly)
a1 = poly.area
buf = poly.buffer(5.0)
a2 = buf.area

print buf.difference(poly).area

