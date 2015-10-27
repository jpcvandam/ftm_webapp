#statistiek van de ftm rasters
#auteur: John van Dam
#datum: 20 oktober 2015

import subprocess
import pandas as pd
import os


def raster_hist(bestand):
    waarde = subprocess.check_output(["gdalinfo", "-hist", bestand])
    return waarde


werkdirectory='/home/john/ftm/ftm/ftm/data'
os.chdir(werkdirectory)

ontw_hist = raster_hist("ontwbas-nzv.tif")
print ontw_hist, 'ontwateringsbasis'
drainw_hist = raster_hist("drainw-nzv.tif")
print drainw_hist, 'drainageweerstand'
kwel_hist = raster_hist("kwel-nzv.tif")
print kwel_hist, 'kwel'
berg_hist = raster_hist("bergcoef-nzv.tif")
print berg_hist, 'bergingscoefficient'
