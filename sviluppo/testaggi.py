__author__ = 'Fabio'

from geopy import geocoders
from geopy import distance
g = geocoders.GoogleV3()
place,(lat,lng) = g.geocode("Via Carlo Follini 12 Roma")
print "%s,%.5f,%.5f" % (place,lat,lng)
'''
_,jk = g.geocode("Jackson,MI")
_,bi = g.geocode("Biloxi,MI")
dist0 = distance.distance(jk,bi).kilometers
print (dist0)
distance.VincentyDistance.ELLIPSOID='NAD83'
dist = distance.VincentyDistance(jk,bi)
print (dist)
import utm
y = 479747.0453210057
x = 5377685.825323031
zone = 32
band = 'U'
print utm.to_latlon( y, x, zone, band)
print utm.from_latlon(lat,lng)
import osr
'''

for illo in range(10,101,25):
    print illo