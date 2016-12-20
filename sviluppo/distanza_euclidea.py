__author__ = 'Fabio'
import math
x1=456456.23123582301
y1=1279721.064356426

x2 = 576628.34295886324
y2 = 1071740.3328161312

x_dist= x1-x2
y_dist= y1-y2
dist_sq = x_dist**2 + y_dist**2
distance = math.sqrt(dist_sq)
distance_km = distance/1000
print "%.2f e' la distanza in km" %(distance_km)

xrad1 = -90.212452861859035
yrad1 = 32.316272202663704
xrad2 = -88.952170968942525
yrad2 = 30.438559624660321
xrad_dist = math.radians(xrad1 - xrad2)
yrad_dist =  math.radians(yrad1 - yrad2)
distrad_sq = xrad_dist**2 + yrad_dist**2
distrad_deg = math.sqrt(distrad_sq)
print distrad_deg * 6371
