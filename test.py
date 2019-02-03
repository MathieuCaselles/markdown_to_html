import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input-directory", help="The file you want to convert", type = str)
parser.add_argument("-o", "--output-directory", help="The name of HTML file", type = str)

arg = parser.parse_args()


if arg.input_directory == None or arg.output_directory == None :
print("Vous ne savez pas comment ça marche ? Utilisez --help    Vous pouvez aussi vous référer au readme")

else:
    if arg.input_directory.endswith('.md'):
        md = arg.input_directory
    else:
        md = arg.input_directory + '.md'

    if arg.output_directory.endswith('.html'):
        html = arg.output_directory
    else:
        html = arg.output_directory + '.html'

print("Votre fichier dans le chemin " + md + " a bien été converti sur le chemin " + html + ".")