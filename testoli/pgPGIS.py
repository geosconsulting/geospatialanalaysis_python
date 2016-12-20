'''
Created on Mar 20, 2014
@author: lanalfa
'''
import StringIO
import psycopg2
import ppygis

try:
    conn = psycopg2.connect("dbname=gas_elec_ntwk port=5433 user=postgres password=GIS")    
except:
    print "Errore connessione!!"
    
cur = conn.cursor()
#cur.execute("SELECT objectid,id,easting,northing,type_id FROM nodes")
cur.execute('SELECT * FROM electrical.cross_substation;')
recordsContenuti = cur.fetchall()

bufferaggio = StringIO.StringIO()
cur.copy_to(bufferaggio, 'nations_euro')
bufferaggio.seek(0)

#print bufferaggio.next()

# Print the data
for poly in bufferaggio:
    #print ppygis.Geometry.read_ewkb(poly.strip())
    if(poly != None):
        print ppygis.Geometry.read_ewkb(poly.strip())

cur.close()
conn.close()