'''
Created on Mar 20, 2014
@author: lanalfa
'''
import ogr,gdal

vector_fn = 'D:\\test.shp'

pixel_size=25
NoData_Value = 255

source_ds = ogr.Open(vector_fn)
source_layer = source_ds.GetLayer()
source_srs = source_layer.GetSpatialRef()
x_min,x_max,y_min,y_max = source_layer.GetExtent()

x_res = int((x_max-x_min)/pixel_size)
y_res = int((y_max-y_min)/pixel_size)

target_ds = gdal.GetDriverByName('MEM').Create('', x_res, y_res, gdal.GDT_Byte)
target_ds.SetGeoTransform((x_min, pixel_size, 0, y_max, 0, -pixel_size))
band = target_ds.GetRasterBand(1)
band.SetNoDataValue(NoData_Value)

# Rasterize
gdal.RasterizeLayer(target_ds, [1], source_layer, burn_values=[1])

# Read as array
array = band.ReadAsArray()
print array