__author__ = 'Fabio'

from owslib.wms import WebMapService
wms = WebMapService('http://localhost/geoserver/wms', version='1.1.1')
wms.identification.type
wms.identification.title
