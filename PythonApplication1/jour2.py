"""
print("%s/%s/%s" % (1,2,3) )
print("{trou1}: , {trou2}: ".format(trou1="true", trou2 ="bla") )
"""
phrase = 'Les poules du cure courent pour pondre'
for lettre in phrase:
    print(lettre) 
print(phrase[-1])
print(phrase[:16])
print(phrase[3:13])
print(phrase.split()) #liste
print(phrase.split()[1])
print("join() :", ";".join(["1","2","3"]))

age=17
nom = "j"
if age>18 or nom =="Juan": 
    print("M")
elif age == 18:
    print("=")
else: 
    print("m")

if 1 >3 and  1 in ["1","2","3"]:
    print("y")
t = tuple(range(10)) #pour ctx, non modifiable
print(t)
s = set(range(10)) #pour enlever les doublons, interessant pour rapidité de test si appartenance: ip dans blacklist par exemple
print(s & set([3, 5]))
print(s ^ set([3, 5]))
print(s)
nombres = list(range(10))
carres = [ nb * nb for nb in nombres if nb % 2 == 0] #liste en intension / comprehensive list
print(carres)

#valeur par défaut de b: 1)
def multiplier(a, b=1):
    res = a * b
    return res
print(multiplier(2) )

import datetime
def date(pattern = "%d/%m/%y"):
    d = datetime.datetime.now()
#    return d
    return ":" + pattern + "".format(d)

#print(date("%d"))
ll = list(enumerate("yo dude"))
print(ll)
#dictionnaire: hashmap en C ou java
#pas sliceable, il est mutable, indexable, iterable
# cle : valeur donccle unique
fruits = {"pomme":"rouge","banane":"jaune"}
print( fruits["banane"])
fruits["poire"] ="jaune"
print( fruits["poire"])
#idz = input(idz)

dicton = "plus un arbre est grand, plus il y a d'oiseaux pour chier dessus"
dictionair = {}
for l in dicton:
    lettre = l.strip()
    if lettre:
        if lettre in dictionair:
            dictionair[lettre] += 1
        else:
            dictionair[lettre] = 1

print(dictionair)
