'''
Created on Feb 24, 2014
@author: lanalfa
'''
import shapefile
r = shapefile.Reader("../dati/MS_UrbanAnC10/MS_UrbanAnC10")
w = shapefile.Writer(r.shapeType)
w.fields = list(r.fields)

selection = []
for rec in enumerate(r.records()):
    print rec[15]
    if rec[1][15]<5000:
        selection.append(rec)
        
for rec in selection:
    w._shapes.append(r.shape(rec[0]))
    w.records.append(rec[1])

w.save("../dati/MS_UrbanAnC10/MS_Urban_Subset")
