from osgeo import gdal
import matplotlib.pyplot as plt
import numpy as np

f = gdal.Open("C:\\Users\\carlosj\\Documents\\Hyperspectral\\Datasets\\AVIRIS\\f180625t01p00r09rdn_e\\f180625t01p00r09rdn_e_sc01_ort_img")

ptspecs = []

pts = [[208, 2815], [615, 2700]]

for pt in pts:
    ptspecs.append([])

#224 bands
for i in range(1, 225):
    print "Processing band", i
    band = f.GetRasterBand(i)
    arr = band.ReadAsArray()
    for i, pt in enumerate(pts):
        thisval = arr[pt[1]+5000][pt[0]]
        print "Point ", i, thisval
        ptspecs[i].append(thisval)
        
print ptspecs