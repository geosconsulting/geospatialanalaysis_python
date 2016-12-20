'''
Created on 08/feb/2014

@author: Fabio
'''
import urllib
import zipfile
import StringIO
import struct

url = "https://geospatialpython.googlecode.com/files/hancock.zip"
cloudshape=urllib.urlopen(url)
memoryshape=StringIO.StringIO(cloudshape.read())
zipshape = zipfile.ZipFile(memoryshape)
cloudshp=zipshape.read("hancock.shp")
bbox=struct.unpack("<dddd",cloudshp[36:68])
print bbox