'''
Created on Mar 20, 2014
@author: lanalfa
'''

import ogr

ds = ogr.Open('map.osm')
layer = ds.GetLayer(1) # layer 1 for ways

nameList = []
for feature in layer:
    if feature.GetField("highway") != None:  # only streets
        name = feature.GetField("name")
        if name != None and name not in nameList: # only streets that have a name and are not yet in the list
            nameList.append(name)

print nameList