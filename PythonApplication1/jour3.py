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
maxb = 0
sborratch = ""
for personne, bieres in scores.items():
    print("- %s: %s" % ( personne, bieres))
    if bieres > maxb:
        maxb = scores[personne]
        sborratch = personne

print(Style.BRIGHT + Fore.GREEN + "Et le plus sborratch est " )
print(Fore.RED + " %s" % sborratch)
print("...")

#debug
# import pdb;pdb.set_trace() #freeze le prg avec un shell breakpoint
"""
class Animal: # pas snake_case dans ce cas 1e let maj
    #pass #fait rien
    def __init__(self, couleur, cri="raww"): #lancé auto à la creation
        print ("obj cree")
        self.couleur = couleur
        self.cri = cri
    def crier(self):
        print (self.cri)
    def __len__(self):
        return 4
    def __str__(self):
        return self.cri
        

lion = Animal("jaune") #instanciation
print(len(lion))
#print(lion.__dict__)
"""
zoo = []
for x in range(5):
    zoo.append(Animal("vert"))
"""
#Animal.crier(lion) ou mieux
lion.crier()
#class avec tab donne le code suivant
"""
class ClassName(object):
    docstring for ClassName
    def __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg = arg
        """
class Vehicule:
    def __init__(self, couleur, carburant=1): #lancé auto à la creation
        print ("parent cree")
        self.couleur = couleur
        self.carburant = carburant
    def coin(self):
        print (self.carburant)
    def __len__(self):
        return 42
    def __str__(self):
        return self.carburant
        

pijo = Vehicule("jaune") #instanciation
print(len(pijo))
class Moto(Vehicule):
    def __init__(self, couleur, carburant=2, roues=2): #lancé auto à la creation
        super().__init__(couleur,carburant)
        print ("enfant cree")
        #self.couleur = couleur
        #self.carburant = carburant


suzuki = Moto("noir")
suzuki.coin()

# generateurs (lisible une seule fois à chaque next)
nombres = [0,1,2,4]

carres = ( x*x for x in nombres if x % 2 == 0)
print(next(carres))
print(next(carres))

def toto():#pas une fct
    print('toto')
    yield 1 #exec puis attend next
    yield 2
    yield 3

gen = toto()
print(gen)
next(gen)
for x in gen:
    print(x)

def titi(nombres):
    for x in nombres:
        if x % 2 == 0:
            yield x * x

g = titi(nombres)
for x in g:
    print(x)

import os

def get_mot(dossier, lettre):
    for racine,dossiers, fichiers in os.walk(dossier):
        for fichier in fichiers:
            if os.path.join(dossier,fichier):
                print(os.path.join(dossier,fichier))
                fic = os.path.join(dossier,fichier)
                try:
                    with open(fic) as f:
                        for ligne in f:
                            for mot in ligne.split:
                                if lettre in mot:
                                    print(fichier)
                                    yield mot
                except OSError:
                    print("err")
                    pass


gn = get_mot('/tmp','e')
next(gn)
next(gn)

import  itertools
#itertools
#for mot in gn:
#    print(mot)