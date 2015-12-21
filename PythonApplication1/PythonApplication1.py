
annee = input("""Annee de naissance:
""")
if 2015 - int(annee) > 17:
    print("majeur")
else:
    print("mineur")