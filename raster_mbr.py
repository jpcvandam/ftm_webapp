#de fysische dat voor de vergelijking gemeten berekend uit de rasters plukken en in een csv zetten

import os, sys
from raster import raster_q

locaties = []
x_coords = []
y_coords = []

#bestandspad = "/home/john/Documenten/Afstuderen_Acacia_water/Data/Noorderzijlvest-gegevens/Noorderzijlvest/DINO/Uitgepakt/Grondwaterstanden_Put/"
#os.chdir(bestandspad)

if len(sys.argv) == 2:
    lijst_locaties = sys.argv[1]
else:
    print "gebruik, ", sys.argv[0], " lijst_locaties"

    
with open(lijst_locaties, 'r') as f:
    line = f.readline()
    while line:
        words = [w.strip() for w in line.split(',')]
        locaties.append(words[0])
        x_coords.append(words[1])
        y_coords.append(words[2])
        line = f.readline()
f.close()
    
print locaties, x_coords, y_coords

of = open("/home/john/Documenten/Afstuderen_Acacia_water/Data/Noorderzijlvest-gegevens/Noorderzijlvest/DINO/fysische_gegevens.txt", 'w')
of.write("Locatie, x_coord, y_coord, berg, drainw, kwel, ontw\n")

bestandspad = "/home/john/ftm/ftm/ftm/data/"
for i in range(0, len(locaties)-1):
    berg = raster_q(bestandspad + "bergcoef-nzv.tif", str(x_coords[i]), str(y_coords[i])).rstrip('\r\n')
    drainw = raster_q(bestandspad + "drainw-nzv.tif", str(x_coords[i]), str(y_coords[i])).rstrip('\r\n')
    kwel = raster_q(bestandspad + "kwel-nzv.tif", str(x_coords[i]), str(y_coords[i])).rstrip('\r\n')
    ontw = raster_q(bestandspad + "ontwbas-nzv.tif", str(x_coords[i]), str(y_coords[i])).rstrip('\r\n')
    of.write('%s, %s, %s, %s, %s, %s, %s\n' % (locaties[i], x_coords[i], y_coords[i], berg, drainw, kwel, ontw))
of.close()    

