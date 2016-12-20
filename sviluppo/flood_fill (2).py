__author__ = 'fabio.lana'
import numpy as np
from linecache import getline

def floodFill(c,r,mask):
    filled = set()
    fill = set()
    fill.add((c,r))
    width = mask.shape[1]-1
    height = mask.shape[0]-1
    flood = np.zeros_like(mask, dtype = np.int8)
    while fill:
        x,y = fill.pop()
        if y == height or x == width or x<0 or y<0:
            continue
        if mask[y][x]==1:
            flood[y][x]=1
            filled.add((x,y))
            west = (x-1,y)
            east = (x+1,y)
            north = (x,y-1)
            south = (x,y+1)
            if not west in filled:
                fill.add(west)
            if not east in filled:
                fill.add(east)
            if not north in filled:
                fill.add(north)
            if not south in filled:
                fill.add(south)
    return flood

source = "C:/Users/Fabio/PycharmProjects/geospatialAnalisys/dati/FloodFill/terrain.asc"
target = "flood.asc"

print "Opening image...."
img = np.loadtxt(source, skiprows= 6)
print "Image opened"

a = np.where(img<70, 1, 0)
print "Image masked"

hdr = [getline(source,i) for i in range(1,7)]
values = [float(h.split(" ")[-1].strip()) for h in hdr]
cols, rows, lx, ly, cell, nd = values
xres = cell
yres = cell * -1

sx = 2582
sy = 2057

print "Beginning flood fill"
fld = floodFill(sx, sy, a)
print "Finished Flood fill"

header = ""
for i in range(6):
    header += hdr[i]

print "Saving grid...."

with open(target, "wb") as f:
    f.write(header)    
    np.savetxt(f,fld,fmt = "%1i")
print "Done!"