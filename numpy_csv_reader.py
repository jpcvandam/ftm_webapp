import numpy as np
#variabelen
nummer_meteostation = 310
for i in [nummer_meteostation]:
    meteobestand_in = 'data/Waterbalans_METEO'+str(i)+'.csv'
    meteo = np.genfromtxt (meteobestand_in, delimiter=",")
datum = meteo[:,0]
neerslag = meteo[:,1]
neerslag2 = meteo[:,2]

print datum, neerslag, neerslag2