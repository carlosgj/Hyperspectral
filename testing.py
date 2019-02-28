from osgeo import gdal
import matplotlib.pyplot as plt
import numpy as np

dsr = gdal.Open("C:\\Users\\carlosj\\Documents\\Hyperspectral\\Datasets\\EO1H0410362011024110KF_1T\\EO1H0410362011024110KF_B070_L1T.TIF")
dsg = gdal.Open("C:\\Users\\carlosj\\Documents\\Hyperspectral\\Datasets\\EO1H0410362011024110KF_1T\\EO1H0410362011024110KF_B100_L1T.TIF")
dsb = gdal.Open("C:\\Users\\carlosj\\Documents\\Hyperspectral\\Datasets\\EO1H0410362011024110KF_1T\\EO1H0410362011024110KF_B150_L1T.TIF")

arrayr = dsr.ReadAsArray()
arrayg = dsg.ReadAsArray()
arrayb = dsb.ReadAsArray()

array = np.stack([arrayr, arrayg, arrayb], axis=-1)
print array.shape
print "Maximum array value: ", np.amax(array)
array = array / float(np.amax(array))
print array 

plt.imshow(array)
plt.show()
#plt.savefig("C:\\Users\\carlosj\\Documents\\Hyperspectral\\Datasets\\EO1H0410362011024110KF_1T\\test.tif", transparent=True, frameon=False)