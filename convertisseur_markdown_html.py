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
    type=str,
)
parser.add_argument(
    "-a",
    "--achtung",
    help = "Activer l'option permet de rendre le texte plus compréhensible aux allemands",
    action = "store_true"
)


arg = parser.parse_args()

if arg.input_directory == None or arg.output_directory == None:
    print("IL vous manque quelque chose: Utilisez «python convertisseur_markdown_html.py -h» ou sinon vous pouvez aussi vous référer au readme")

else:
    dossier_1 = os.listdir(arg.input_directory)

    dossier_2 = arg.output_directory

# Structure de la page html en 2 parties.

debut_html = "<!DOCTYPE html>\n\n<html>\n\n<head>\n\n\t<meta charset='utf-8'/>\n\t<title>"+ "Fichier convertit" +"</title>\n\n</head>\n\n<body>\n\n"
fin_html = "\n\n</body>\n\n</html>"

# achtung

def achtung(texte):

    texte = texte.replace('s', 'z')
    texte = texte.replace('co', 'ko')
    texte = texte.replace('ca', 'ka')
    texte = texte.replace('cu', 'ku')
    texte = texte.replace('cc', 'k')
    texte = texte.replace('c ', 'k ')
    texte = texte.replace('c', 'z')
    texte = texte.replace('qu', 'k')
    texte = texte.replace('ph', 'f')
    texte = texte.replace('zz', 'z')
    texte = texte.replace('mm', 'm')
    texte = texte.replace('nn', 'n')
    texte = texte.replace('tt', 't')
    texte = texte.replace('rr', 'r')
    texte = texte.replace('co', 'ko')
    texte = texte.replace('ff', 'f')
    texte = texte.replace('ll', 'l')
    texte = texte.replace('pp', 'p')
    texte = texte.replace('bb', 'b')
    texte = texte.replace('dd', 'd')
    texte = texte.replace('gg', 'g')
    texte = texte.replace('kk', 'k')
    texte = texte.replace('ge', 'che')
    texte = texte.replace('gi', 'chi')
    texte = texte.replace('co', 'ko')
    texte = texte.replace('g', 'k')
    texte = texte.replace('b', 'p')
    texte = texte.replace('v', 'f')
    texte = texte.replace('zh', 'ch')
    texte = texte.replace('e ', ' ')

    return texte

# Gestion des fichier dans dossier

for fichier_a_convertir in dossier_1:

    if fichier_a_convertir.endswith('.md'):

        with open("conversion/" + fichier_a_convertir, "r") as fichier:
            mon_fichier = fichier.read()
        
        nouveau_nom = fichier_a_convertir.replace('.md', '')
        if arg.achtung:
            mon_fichier = achtung(mon_fichier)

        with open(dossier_2 + "/" + nouveau_nom + ".html", "x") as fichier:
            fichier.write(debut_html)
            fichier.write(markdown2.markdown(mon_fichier)) # markdown2.markdown() fait la conversion automatiquement ! C'est super tchité !
            fichier.write(fin_html)

print("Conversion réussis !")

