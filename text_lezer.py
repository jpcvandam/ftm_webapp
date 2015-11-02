def meteo_lezen(nummer_meteostation):
	stationsnummer=[]
	yyyymmdd=[]
	dr=[]
	rh=[]
	rhx=[]
	ev24=[]
	with open('data/METEO'+ str(nummer_meteostation) + '.TXT', 'r') as fileinput:
	    for _ in xrange(20):
			next(fileinput)
	    for line in fileinput:
			stationsnummer.append(str(line[2:5]))
			yyyymmdd.append(str(line[6:14]))
			#print line[6:14]
			dr.append(int(line[16:20]))
			#print line[16:20]
			rh.append (int(line[22:26]))
			#print line[22:26]
			rhx.append (int(line[27:32]))
			#print line[27:32]
			ev24.append (int(line[51:56]))
			#print line[51:56]
	fileinput.close()
	return stationsnummer, yyyymmdd, dr, rh, rhx, ev24

nummer_meteostation=215
print meteo_lezen(nummer_meteostation)[0]