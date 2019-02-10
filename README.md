# Convertisseur de fichiers markdown en fichier html  

Ce programme permet de convertir des fichiers markdown en fichiers html.  

## Comment l'utiliser ?

Rendez-vous dans le dossier où vous avez téléchargé le programme puis faites Shift + Clic Droit et cliqez sur « Ouvrir la fenêtre Powershell ici».

![alt text](https://github.com/MathieuCaselles/markdown_to_html/blob/master/screen_tuto/1.png)  

Une fois à l'intérieur écrivez :

    python convertisseur_markdown_html.py --input-directory <chemin du dossier contenant le(s) fichier(s) markdown à convertir> --output-directory <chemin du dossier où seront placés les fichiers convertit>


Vous pouvez aussi écrire :

    python convertisseur_markdown_html.py -i <chemin du dossier contenant le(s) fichier(s) markdown à convertir> -o <chemin du dossier où seront placés les fichiers convertit>

Vous ne conaissez pas le chemin de vos dossiers ? Pour le connaitre il suffit d'aller dans votre dossier auquel vous souhaiter connaître le chemin puis de cliquer dans la barre des dossiers au dessus:

![alt text](https://github.com/MathieuCaselles/markdown_to_html/blob/master/screen_tuto/2.png)  

IL ne vous reste plus qu'à copier coller le chemin dans le powershell ! (faites un clic droit dans le powershell pour coller)  
  
Cela devrait donner quelque chose qui resemble à ça :

![alt text](https://github.com/MathieuCaselles/markdown_to_html/blob/master/screen_tuto/3.png)

Si vous préférez vous pouvez aussi créer 2 dossiers dans le dossier où si situe le programme. Par exemple un dossier «conversion» ou se situra tous vos fichiers md et un dossier «convertit» où se situera les fichiers convertit. Comme cela vous aurez juste à écrire:

    python convertisseur_markdown_html.py -i conversion -o convertit

J'ai d'ailleurs laissé un dossier conversion avec de simples fichiers markdown pour tester la convertion. Vous y trouverez aussi un fichier txt qui n'est donc pas en md et vous verrez que cela ne pose pas de problèmes au programme ! Il ignore tout simplement tous les fichier qui ne sont pas en md ! Comme ça pas besoin de trier vos fichiers md des autres fichiers !

## Options Supplémentaire:

Il existe 2 options sipplémentaire: achtung et kikoo_lol.  

achtung permet de rendre de rendre le texte plus compréhensible aux allemands en suivant ces règles : <https://linuxfr.org/nodes/108129/comments/1642666>  
Pour l'utiliser il suffit de rajouter -a ou --achtung sans aucune précision supplémentaire.  
  
kikoo_lol permet de rajouter aléatoirement des « kikoo », « lol », « mdr », « ptdr » dans le texte.
Pour l'utiliser il suffit de rajouter -k ou --kikoo_lol sans aucune précision supplémentaire.

## Dernière chose :

Si vous oubliez comment cela fonctionne vous pouvez taper : 

    python convertisseur_markdown_html.py --help

ou taper :

    python convertisseur_markdown_html.py -h

Cela vous rappellera quels sont les paramètres à utiliser et comment les utiliser !
