import gdalnumeric

#Input File
src = "../dati/islands/islands.tif"

#Output
tgt = "../dati/islands/islands_classified.jpg"

srcArr = gdalnumeric.LoadFile(src)

classes = gdalnumeric.numpy.histogram(srcArr,bins=2)[1]
print classes

#Color look-up table (LUT) - must be len(classes)+1.
#Specified as R,G,B tuples
lut = [[255,0,0],[0,0,0],[255,255,255]]

start = 1

rgb = gdalnumeric.numpy.zeros((3, srcArr.shape[0], srcArr.shape[1],),gdalnumeric.numpy.float32)

# Process all classes and assign colors
for i in range(len(classes)):
    mask = gdalnumeric.numpy.logical_and(start <= srcArr, srcArr <= classes[i])
    for j in range(len(lut[i])):
        rgb[j] = gdalnumeric.numpy.choose(mask, (rgb[j], lut[i][j]))
    start = classes[i]+1

# Save the image
gdalnumeric.SaveArray(rgb.astype(gdalnumeric.numpy.uint8), tgt, format="GTIFF",prototype=src)