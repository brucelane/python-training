"""
u"chaine" unicode en python2, inutile en python3 car tout est unicode

#any(l.startswith('#') in l for l in open('/etc/fstab')

import collections
collections.OrederedDict()

dictionnaire
import colorama
from colorama import init
init()
"""
import colorama
from colorama import init, Fore, Back, Style
init()

scores={}
#scores["yo"] = 1
f = open('/home/bruce/Bureau/apero.csv')
header = f.readline()
for row in f:
    ligne = row.split(',')
    nom = ligne[1]
    compte = int(ligne[2])
    if nom in scores:
        scores[nom] += compte
    else:
        scores[nom] = compte

list(scores.items())
max = 0
sborratch = ""
for personne, bieres in scores.items():
    print("- %s: %s" % ( personne, bieres))
    if bieres > max:
    	max = scores[personne]
    	sborratch = personne

print(Style.BRIGHT + Fore.GREEN + "Et le plus sborratch est " )
print(Fore.RED + " %s" % sborratch)
print("...")