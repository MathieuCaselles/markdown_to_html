import os
import glob

ma_liste = os.listdir("conversion")
ma_liste_2 = glob.glob("conversion/*.txt")

# with open("conversion/mon_test.md", "a") as fichier:
  #  fichier.write("\nHello World")


with open("conversion/mon_test.md", "r") as fichier:
    mon_fichier = fichier.read()
    print(mon_fichier)


with open("convertit/mon_nouveau_test.md", "x") as fichier:
    fichier.write(mon_fichier)

with open("convertit/mon_nouveau_test.md", "r") as fichier:
    mon_fichier = fichier.read()
    print(mon_fichier)