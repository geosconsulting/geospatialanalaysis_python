'''
Created on Mar 20, 2014
@author: lanalfa
'''
import psycopg2

try:
    conn = psycopg2.connect("dbname=grid user=postgres password=GIS")    
except:
    print "Errore connessione!!"
    
cur = conn.cursor()

try:
    cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
    cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)",(100, "abc'def"))
except:
    print "Inserimento non riuscito"
    
cur.execute("SELECT * FROM test;")
cur.fetchone()    

conn.commit()    

cur.close()
conn.close()