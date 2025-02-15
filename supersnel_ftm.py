import os
import numpy as np
import matplotlib.pyplot as plt
import pylab
import datetime
import matplotlib.dates as mdates
import subprocess


def FTM(opdrachtparameters, meteo, naam):
    spam = subprocess.check_output(["./FTM", opdrachtparameters, meteo, naam])
    return spam


def supersnel_ftm(x2, y2):
    #varabelen
    werkdirectory = '/home/john/ftm/ftm/ftm/data'
    naam = str(x2)+'_'+str(y2)
    meteobestand = 'METEO280.txt'

    os.chdir(werkdirectory)

    array_bergingscoefficient = np.array([float(raster_q("/home/john/ftm/ftm/ftm/data/bergcoef-nzv.tif", x, y))])
    array_drainweerstand = np.array([float(raster_q("/home/john/ftm/ftm/ftm/data/drainw-nzv.tif", x, y))])
    array_qbot = np.array([float(raster_q("/home/john/ftm/ftm/ftm/data/kwel-nzv.tif", x, y))])
    array_hgem = np.array([float(raster_q("/home/john/ftm/ftm/ftm/data/ontwbas-nzv.tif", x, y))])




    output_file = open(naam + 'invoer.txt', 'w')
    line = '%s\n' % ("#runn        al     hgem  drainw    berg    qbot  ")
    unicode_line = line.encode('utf-8')
    output_file.write(unicode_line)
    runn = 1
    al = 365
    hgem = float(raster_q("/home/john/ftm/ftm/ftm/data/ontwbas-nzv.tif", x, y)) * -1
    drainw = float(raster_q("/home/john/ftm/ftm/ftm/data/drainw-nzv.tif", x, y))
    berg = float(raster_q("/home/john/ftm/ftm/ftm/data/bergcoef-nzv.tif", x, y))# f['bergcoef10'] / 100
    qbot = float(raster_q("/home/john/ftm/ftm/ftm/data/kwel-nzv.tif", x, y)) #f['kwel10'] / 10
    line = '%8.0f%8.0f%8.0f%8.0f%8.3f%8.3f\n' % (runn,al,hgem,drainw,berg,qbot)
    unicode_line = line.encode('utf-8')
    output_file.write(unicode_line)    
    output_file.close()

    FTM(naam + 'invoer.txt', meteobestand, naam)


    # GHG en GLG uit textbestand halen 
    fileinput = open(naam + 'gwlstatistics.txt', 'r')
    fileinput.readline()
    fileinput.readline()
    #for line in fileinput:
    #print fileinput.read(4),
    fileinput.read(4),
    GHG = fileinput.read(8)
    fileinput.readline()
    fileinput.readline()
    fileinput.read(4),
    GLG = fileinput.read(8)
    fileinput.close()


    fileinput = open(naam + 'gwl.txt', 'r')
    #print(fileinput.readline()),
    #print(fileinput.readline())
    fileinput.readline()
    fileinput.readline()

    #print fileinput.readline(8),
    dagList = [] 
    maandList = []
    jaarList = []
    datumList = []
    gwstList = []
    GHGList = []
    GLGList = []
    for line in fileinput:
         dagList.append(int(line[0:2]))

         if int(line[6:8]) < 20:
             jaarList.append(int(line[6:8])+2000)
         else:
            jaarList.append(int(line[6:8])+1900)
         if int(line[6:8]) < 20:
             datum = datetime.date(int(line[6:8])+2000,int(line[3:5]),int(line[0:2]))         
         else:
             datum = datetime.date(int(line[6:8])+1900,int(line[3:5]),int(line[0:2]))
         datumList.append(datum)
         gwstList.append(float(line[9:16]))
         GHGList.append(float(GHG))
         GLGList.append(float(GLG))
    fileinput.close()

    #print gwstList
    # x and y definieren
    x = datumList
    ygrwst = gwstList
    yGHG = GHGList
    yGLG = GLGList
    
    # Create plots with pre-defined labels.
    plt.plot(x, ygrwst, 'b', label='Grondwaterstand')
    plt.plot(x, yGHG, 'r', label='GHG')
    plt.plot(x, yGLG, 'g', label='GLG')

    plt.legend(loc='lower center', shadow=True, fontsize='x-large')
)

# Titels definieren
    plt.xlabel('Tijd')
    plt.ylabel('Grondwaterstand (cm t.o.v. mv)')
    plt.title('Tijdstijghoogtelijn')
    plt.grid(True)
# without the line below, the figure won't show
    plotnaam='Grondwaterstanden_'+str(x2)+'_'+str(y2)+'.png'
    pylab.savefig(bestandspad + plotnaam, bbox_inches='tight')
    pylab.close()

    return plot(bestandspad_plot, x2, y2)

