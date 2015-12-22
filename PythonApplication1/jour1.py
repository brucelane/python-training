"""
commentaire
compteur = 0
while compteur <= 10:
    print(compteur)
    compteur = compteur + 1

reponse = None

# 
# while reponse != 'stop':
#    reponse = input('g')

import random
nombre = random.randint(0, 10)
print(nombre)
while reponse != nombre:
    reponse = int(input("devine?"))

couleurs = ["rouge", "jaune", "bleu"]
len(couleurs)
couleurs.append("vert")
len(couleurs)
print(couleurs[-1]) #negatif -1 dernier element
reponse = None
while reponse != 'stop':
    reponse = input("pref")
    couleurs.append(reponse)

couleurs.pop()
print(couleurs)

import random
reps = []
reponse = None
nombre = random.randint(0, 10)
print(nombre)
while reponse != nombre:
    reponse = int(input("devine?"))
    reps.append(reponse)

reps.pop()
print(reps)
couleurs = ["rouge", "jaune", "bleu"]
print(couleurs)
for coul in couleurs:
    print(coul)

import random
reps = set()
reponse = None
nombre = random.randint(0, 10)
print(nombre)
while reponse != nombre:
    reponse = int(input("devine?"))
    reps.add(reponse)
#reps.remove(1)
for i in reps:
    print (i)


def additioner(a,b):
    return a+b
resultat = additioner(4,8)
print(resultat)


couleurs = ["rouge", "jaune", "bleu"]
def affliste(iterable):
    resultat = ""
    for i in iterable:
        resultat += str(i) + "\n"
    return resultat

res = affliste(couleurs)
print(res)
"""

def sondage(question, mot_arret):
    reps = set()
    reponse = ""
    while reponse != mot_arret:
        reponse = input(question)
        reps.add(reponse)
    reps.remove(mot_arret) 
    return reps

res = sondage("preferee?","assez")
print(res)

