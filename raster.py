#script om een raster met GDAL te bevragen
#auteur: John van Dam
#Datum: 15 september 2015

import subprocess

def raster_q(bestand, x1, y1):
    waarde = subprocess.check_output(["gdallocationinfo","-valonly","-geoloc", bestand, x1, y1])
    return waarde



