__author__ = 'Fabio'
import operator
import gdal,gdalnumeric,osr
import shapefile
import Image,ImageDraw

raster = "../dati/SatImage/stretched.tif"
shp = "hancock"
output = "../dati/SatImage/clip.tif"

def imageToArray(i):
    a=gdalnumeric.numpy.fromstring(i.tostring(),'b')
    a.shape = i.im.size[1],i.im.size[0]
    return a

def world2Pixel(geoMatrix,x,y):
    ulX = geoMatrix[0]
    ulY = geoMatrix[3]
    xDist = geoMatrix[1]
    yDist = geoMatrix[5]
    rtnX = geoMatrix[2]
    rtnX = geoMatrix[4]
    pixel = int((x-ulX)/xDist)
    line = int((ulY-y)/xDist)
    return pixel,line

srcArray = gdalnumeric.LoadFile(raster)
srcImage = gdal.Open(raster)
geoTrans = srcImage.GetGeoTransform()

r = shapefile.Reader("../dati/%s.shp" % shp)
minX,minY,maxX,maxY = r.bbox
ulX,ulY = world2Pixel(geoTrans,minX,maxY)
lrX,lrY = world2Pixel(geoTrans,maxX,minY)

pxWidth = int(lrX-ulX)
pxHeight = int(lrY-ulY)

clip = srcArray[:,ulY:lrY,ulX:lrX]

geoTrans = list(geoTrans)
geoTrans[0] = minX
geoTrans[3] = minY

# Map points to pixels for drawing the county boundary # on a blank 8-bit, black and white, mask image.
pixels = []
for p in r.shape(0).points:
    pixels.append(world2Pixel(geoTrans,p[0],p[1]))
rasterPoly = Image.new("L",(pxWidth, pxHeight), 1)
# Create a blank image in PIL to draw the polygon.
rasterize = ImageDraw.Draw(rasterPoly)
rasterize.polygon( pixels, 0)
# Convert the PIL image to a NumPy array
mask = imageToArray( rasterPoly)
# Clip the image using the mask
clip = gdalnumeric.numpy.choose( mask, (clip, 0)). astype( gdalnumeric.numpy.uint8)
# Save ndvi as tiff
gdalnumeric.SaveArray(clip, output, format ="GTiff", prototype = raster)
