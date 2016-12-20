'''
Created on 12/gen/2014

@author: Fabio
'''
import struct
f=open("../dati/hancock.shp","rb")
f.seek(36)
# print(struct.unpack("<d",f.read(8)))
# print(struct.unpack("<d",f.read(8)))
# print(struct.unpack("<d",f.read(8)))
# print(struct.unpack("<d",f.read(8)))
print(struct.unpack("<dddd",f.read(32)))
