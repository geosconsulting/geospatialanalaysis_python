'''
Created on Mar 21, 2014
@author: lanalfa
'''

from geoserver.catalog import Catalog
import pprint

cat = Catalog("http://localhost:8080/geoserver/rest")

resources = cat.get_resources()
gliStores = cat.get_stores()
iWorkspaces = cat.get_workspaces()

for loWorkspace in iWorkspaces:
    print loWorkspace.name

print

for loStore in gliStores:
    print loStore.name

print
    
iLayers= cat.get_layers()

for ilLayer in iLayers:
    ilNomeLayer = ilLayer.name
    print ilNomeLayer
    
print 

for ilLayer in iLayers:
    ilNomeLayer = ilLayer.name
    if ilNomeLayer=='ports_eu':
        ilLayerSelezionatoRisorsa = cat.get_resource(ilNomeLayer)
        print ilLayerSelezionatoRisorsa.attributes
