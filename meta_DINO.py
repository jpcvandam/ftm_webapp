#auteur: John van Dam
#datum: 01-02-2016

#opbouw bestanden
#blok 1: titel en andere meuk, 6 regels, 1 witregel
#blok 2: verklaring woorden, 3 regels, 1 witregel
#blok 3: Beschrijving filters, variabel aantal regels, 2 witregels
#blok 4: de tijdreeks, variabele lengte DIT WIL IK INLEZEN

import os

os.chdir("/home/john/Documenten/Afstuderen_Acacia_water/Data/dino_gedeelte_NZV/Grondwaterstanden_Put")
infile = "B0*_1.csv" #bestandsnaam met eventueel een pad ervoor

for file in ["B03D0016001_1.csv", "B03D0016001_1.csv", "B03D0071001_1.csv", "B03G0090001_1.csv", "B03G0091001_1.csv", "B07A0021001_1.csv", "B07A0108001_1.csv", "B07A0112001_1.csv", "B07A0112002_1.csv", "B07A0120001_1.csv", "B07A0121001_1.csv", "B07A0122001_1.csv", "B07A0124001_1.csv", "B07A0125001_1.csv", "B07A0127001_1.csv", "B07A0128001_1.csv", "B07A0130001_1.csv", "B07A0131001_1.csv", "B07A0133001_1.csv", "B07A0134001_1.csv", "B07A0135001_1.csv", "B07A0136001_1.csv", "B07A0140001_1.csv", "B07A0142001_1.csv", "B07A0147001_1.csv", "B07A0924001_1.csv", "B07A0945001_1.csv", "B07A0945002_1.csv", "B07A0946001_1.csv", "B07A0947001_1.csv", "B07A0948002_1.csv", "B07A0949001_1.csv", "B07A0956001_1.csv", "B07A0957001_1.csv", "B07A0981001_1.csv", "B07A0982001_1.csv", "B07B0019001_1.csv", "B07B0019002_1.csv", "B07B0056001_1.csv", "B07B0119001_1.csv", "B07B0130001_1.csv", "B07B0131001_1.csv", "B07B0133001_1.csv", "B07B0135001_1.csv", "B07B0136001_1.csv", "B07B0137001_1.csv", "B07B0138001_1.csv", "B07B0139001_1.csv", "B07B0141001_1.csv", "B07B1108001_1.csv", "B07B1109001_1.csv", "B07E0029001_1.csv", "B07E0030001_1.csv", "B07E0031001_1.csv", "B07E0042001_1.csv", "B07E0084001_1.csv", "B07E0085001_1.csv", "B07E0087001_1.csv", "B07E0088001_1.csv", "B07E0089001_1.csv", "B07E0092001_1.csv", "B07E0094001_1.csv", "B07E0095001_1.csv", "B07E0097001_1.csv", "B07E0098001_1.csv", "B07E0101001_1.csv", "B07E1137001_1.csv", "B03D0071001_1.csv", "B03G0090001_1.csv", "B03G0091001_1.csv", "B07A0021001_1.csv", "B07A0108001_1.csv", "B07A0112001_1.csv", "B07A0112002_1.csv", "B07A0120001_1.csv", "B07A0121001_1.csv", "B07A0122001_1.csv", "B07A0124001_1.csv", "B07A0125001_1.csv", "B07A0127001_1.csv", "B07A0128001_1.csv", "B07A0130001_1.csv", "B07A0131001_1.csv", "B07A0133001_1.csv", "B07A0134001_1.csv", "B07A0135001_1.csv", "B07A0136001_1.csv", "B07A0140001_1.csv", "B07A0142001_1.csv", "B07A0147001_1.csv", "B07A0924001_1.csv", "B07A0945001_1.csv", "B07A0945002_1.csv", "B07A0946001_1.csv", "B07A0947001_1.csv", "B07A0948002_1.csv", "B07A0949001_1.csv", "B07A0956001_1.csv", "B07A0957001_1.csv", "B07A0981001_1.csv", "B07A0982001_1.csv", "B07B0019001_1.csv", "B07B0019002_1.csv", "B07B0056001_1.csv", "B07B0119001_1.csv", "B07B0130001_1.csv", "B07B0131001_1.csv", "B07B0133001_1.csv", "B07B0135001_1.csv", "B07B0136001_1.csv", "B07B0137001_1.csv", "B07B0138001_1.csv", "B07B0139001_1.csv", "B07B0141001_1.csv", "B07B1108001_1.csv", "B07B1109001_1.csv", "B07E0029001_1.csv", "B07E0030001_1.csv", "B07E0031001_1.csv", "B07E0042001_1.csv", "B07E0084001_1.csv", "B07E0085001_1.csv", "B07E0087001_1.csv", "B07E0088001_1.csv", "B07E0089001_1.csv", "B07E0092001_1.csv", "B07E0094001_1.csv", "B07E0095001_1.csv", "B07E0097001_1.csv", "B07E0098001_1.csv", "B07E0101001_1.csv", "B07E1137001_1.csv"]:

    with open(file, 'r') as fileinput:
        for line in fileinput:
            print line[13]
            
fileinput.close()