__author__ = 'Fabio'
from osgeo import gdal
raster = gdal.Open("../dati/SatImage/SatImage.tif")
print ("Bande :" + str(raster.RasterCount))
print ("Pixel in X :" + str(raster.RasterXSize))
print ("Pixel in Y :" + str(raster.RasterYSize))

from osgeo import gdalnumeric
srcArray = gdalnumeric.LoadFile("../dati/SatImage/SatImage.tif")
banda1 = srcArray[0]
gdalnumeric.SaveArray(banda1,"../dati/banda1Estratta.jpg",format="JPEG")