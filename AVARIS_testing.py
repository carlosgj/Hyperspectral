from osgeo import gdal
import matplotlib.pyplot as plt
import numpy as np

f = gdal.Open("C:\\Users\\carlosj\\Documents\\Hyperspectral\\Datasets\\AVIRIS\\f180625t01p00r09rdn_e\\f180625t01p00r09rdn_e_sc01_ort_img")

rband = f.GetRasterBand(200)
rarr = rband.ReadAsArray()

gband = f.GetRasterBand(100)
garr = gband.ReadAsArray()

bband = f.GetRasterBand(10)
barr = bband.ReadAsArray()

#rarr = rarr.astype(float)
#garr = garr.astype(float)
#barr = barr.astype(float)

rarr /= 2
garr /= 2
barr /= 2

rarr += 25
garr += 25
barr += 25

rarr *= 4
garr *= 2

print "Red: ", np.amin(rarr), np.amax(rarr)
print "Green: ", np.amin(garr), np.amax(garr)
print "Blue: ", np.amin(barr), np.amax(barr)

array = np.stack([rarr, garr, barr], axis=-1)

array = array[5000:10000]

array = array.astype(float)

array /= 32768.

array *= 10

print "Maximum array value: ", np.amax(array)
print "Minimum array value: ", np.amin(array)


print array.shape
#print array 

plt.imshow(array)
plt.show()
#plt.savefig("C:\\Users\\carlosj\\Documents\\Hyperspectral\\Datasets\\EO1H0410362011024110KF_1T\\test.tif", transparent=True, frameon=False)