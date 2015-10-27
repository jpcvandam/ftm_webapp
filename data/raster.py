#script om een raster met GDAL te bevragen
#auteur: John van Dam
#Datum: 15 september 2015

import subprocess

def raster_q(bestand, x1, y1):
    waarde = subprocess.check_output(["gdallocationinfo","-valonly","-geoloc", bestand, x1, y1])
    return waarde


x= "6.5108"
y= "53.3847"



print raster_q("/home/john/ftm/ftm/ftm/data/Bergingscoefficient1.tif", x, y)
print raster_q("/home/john/ftm/ftm/ftm/data/Drainageweerstand1.tif", x, y)
print raster_q("/home/john/ftm/ftm/ftm/data/Kwel-kk-nz1.tif", x, y)
print raster_q("/home/john/ftm/ftm/ftm/data/Ontwateringsbasis1.tif", x, y)
