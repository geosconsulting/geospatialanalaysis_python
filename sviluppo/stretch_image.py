__author__ = 'Fabio'
import gdalnumeric
import operator

def histogram(a,bins=range(0,256)):
    fa = a.flat
    n = gdalnumeric.numpy.searchsorted(gdalnumeric.numpy.sort(fa),bins)
    n= gdalnumeric.numpy.concatenate([n,[len(fa)]])
    hist = n[1:]-n [:1]
    return hist

def stretch(a):
    hist = histogram(a)
    print hist
    lut = []
    for b in range(0,len(hist),256):
        step = reduce(operator.add, hist[b:b+256])/255
        n = 0
        for i in range(256):
            lut.append(n/step)
            n = n+hist[i+b]
    gdalnumeric.numpy.take(lut,a,out=a)
    return a

src = "../dati/SatImage/swap.tif"
arr = gdalnumeric.LoadFile(src)
stretched = stretch(arr)
gdalnumeric.SaveArray(arr,"../dati/SatImage/stretched.tif",format="GTiff",prototype=src)
