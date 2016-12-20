'''
Created on Mar 20, 2014
@author: lanalfa
'''
import psycopg2
import csv

try:
    conn = psycopg2.connect("dbname=gas_elec_ntwk port=5433 user=postgres password=GIS")    
except:
    print "Errore connessione!!"
    
cur = conn.cursor()
#cur.execute("SELECT objectid,id,easting,northing,type_id FROM nodes")
cur.execute('SELECT "SUB_ID","SUB_NAME","MAX_VOLT","NUM_LINES","PLATTS_ID" FROM electrical.cross_substation;')
recordsContenuti = cur.fetchall()

with open('nodi.csv', 'wb') as csvfile:
    csvwriter = csv.writer(csvfile,delimiter=',',quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    csvwriter.writerow(['SUB_ID,SUB_NAME,MAX_VOLT,NUM_LINES,PLATTS_ID'])
    for record in recordsContenuti:
        csvwriter.writerow(record)

cur.close()
conn.close()