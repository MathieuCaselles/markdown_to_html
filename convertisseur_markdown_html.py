import os
import argparse
import markdown2

# interface graphique

parser = argparse.ArgumentParser()
parser.add_argument(
    "-i",
    "--input-directory",
    help="Le dossier avec les fichier markdown à convertir",
    type=str,
)
parser.add_argument(
    "-o", 
    "--output-directory", 
    help="Le dossier de destination", 
    type=str
)

arg = parser.parse_args()

if arg.input_directory == None or arg.output_directory == None:
    print("IL vous manque quelque chose: Utilisez --help ou sinon vous pouvez aussi vous référer au readme")

else:
    dossier_1 = arg.input_directory

    dossier_2 = arg.output_directory

# Gestion des fichier dans dossier

debut_html = "<!DOCTYPE html>\n\n<html>\n\n<head>\n\n\t<meta charset='utf-8'/>\n\t<title>"+ "Fichier convertit" +"</title>\n\n</head>\n\n<body>\n\n"
fin_html = "\n\n</body>\n\n</html>"

with open(dossier_1, "r") as fichier:
    mon_fichier = fichier.read()


with open(dossier_2, "x") as fichier:
    fichier.write(debut_html)
    fichier.write(mon_fichier)
    fichier.write(fin_html)

with open(dossier_2, "r") as fichier:
    mon_fichier = fichier.read()

print("Conversion réussis !")

# convertion


