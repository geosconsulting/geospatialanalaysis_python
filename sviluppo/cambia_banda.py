__author__ = 'Fabio'
import gdalnumeric

src = r"D:\workspace\geospatialAnalisys\dati\SatImage\SatImage.tif"
arr = gdalnumeric.LoadFile(src)

gdalnumeric.SaveArray(arr[[2,0,1],:],"../dati/SatImage/swap_201.tif",format="GTiff",prototype=src)