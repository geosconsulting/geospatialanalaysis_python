'''
Created on Mar 20, 2014
@author: lanalfa
'''
from osgeo import ogr
import os
import sys

DriverName = "ESRI Shapefile"
FileName = 'D:\\data_dir\\data\\shapefiles\\states.shp'

driver = ogr.GetDriverByName(DriverName)

if os.path.exists(FileName):
    dataSource = driver.Open(FileName,0)
    layer = dataSource.GetLayer()        
    numeroFeat = layer.GetFeatureCount()    

listaStati = []
for item in layer:
    listaStati.append(item.GetField("STATE_NAME"))
    
print listaStati

layer.SetAttributeFilter("SUB_REGION = 'Pacific'")

for illo in layer:
    print illo.GetField("STATE_NAME")

listaCampi = []
layerDefn = layer.GetLayerDefn()
for i in range(layerDefn.GetFieldCount()):
    nome = layerDefn.GetFieldDefn(i).GetName()
    listaCampi.append(nome)

import psycopg2
try:
    conn = psycopg2.connect("dbname=grid port=5432 user=postgres password=GIS")    
except:
    print "Errore connessione!!"
    
cur = conn.cursor()
cur.execute('select schema_name from information_schema.schemata;')
recordsContenuti = cur.fetchall()

listaSchemi = []
for record in recordsContenuti:  
    #print str(record)  
    if str(record)[2:4]=='pg':
        pass                
    elif str(record)[2:5]=='inf':  
        pass      
    else:
        listaSchemi.append(record)

cur1 = conn.cursor()
cur1.execute("SELECT * FROM information_schema.tables WHERE table_schema = 'public';")
listaTabelleSchema = cur1.fetchall()

listaTabelle = []
for tabella in listaTabelleSchema:
    #testoVerifica=str(tabella[2])[0:9]
    #print testoVerifica
    if str(tabella[2])[0:6]=='raster':
        pass                
    elif str(tabella[2])[0:9]=='geography':  
        pass 
    elif str(tabella[2])[0:8]=='geometry':  
        pass 
    elif str(tabella[2])=='spatial_ref_sys':  
        pass 
    else:
        listaTabelle.append(tabella[2]);
        #print tabella[2];
    
cur2 = conn.cursor()
stringa = "SELECT * FROM " + listaTabelle[5] + ";"
cur2.execute(stringa)
listaRecordsTabellaZero = cur2.fetchall()

#print listaRecordsTabellaZero

listaRecordTabella=[]
for recordTabella in listaRecordsTabellaZero:
    listaRecordTabella.append(recordTabella[3])
    #print recordTabella[3]

#print listaRecordTabella

cur.close()
conn.close()