# coding : utf-8

# Bonjour Jean-Hugues! Voici mon quatrième devoir sur les fameuses chroniques de Richard Martineau. 
# Vous trouverez ma démarche justifiée en #commentaires. Bonne lecture! Amélie :-) 

import csv, spacy
from collections import Counter
# Importation des fichiers nécessaires à la création du .csv

tal = spacy.load("fr_core_news_md")
# Importation du réseau neuronal

tal.Defaults.stop_words.add("y")
tal.Defaults.stop_words.remove("gens")
# Add terme vide voulu [y] et remove terme vide non voulu [gens]. 

martino = "martino.csv"
# Importation du fichier.csv.

f = open(martino)
chroniques = csv.reader(f)
# Ouverture du fichier.csv.

next(chroniques)
# Modification afin que le fichier ne prenne pas en compte la première ligne.

bigrams = []
    # Création d'une liste vide qui va me permettre de grouper les mots voulus ensemble.

for mots in chroniques:
# Création de la boucle qui permet d'imprimer toutes les données voulues, ici le caractère "3" qui correspond au texte des chroniques.
    doc = tal(mots[3])
    #for token in doc:
        #print(token.text)

    tokens = [token.text for token in doc if token.is_stop == False and token.is_punct == False]
    #print(tokens)
    # Conserver les tokens "faux", exclusion des mots vides de mes lemmes ET supression de la ponctuation.

    lemmes = [token.lemma_ for token in doc if token.is_stop == False and token.is_punct == False]
    #print(lemmes)
    # Lemmatisation du fichier. 

    for motsfreq in lemmes:
        for x,y in enumerate(lemmes[:-1]):
            if "islam" in motsfreq:
                bigrams.append("{} {}".format(lemmes[x],lemmes[x+1]))
            elif "musulm" in motsfreq:
                # Création des boucles me permettant de sélectionner le vocabulaire voulu dans les chroniques de Martineau.
                bigrams.append("{} {}".format(lemmes[x],lemmes[x+1]))
                # Append des lemmes à la liste vide "bigrams" préalablement créée.

freq = Counter(bigrams)
print(freq.most_common(50))
# Impression des 50 termes les plus fréquents dans les chroniques de Martineau.    

# Voici le résultat de mes précieux essais-erreurs. 

# Comme j'exécute mon code avec un ordinateur Windows (je suppose que le problème vient de là), j'éprouve quelques problèmes avec l'impression de mon script qui ne se déroule pas comme il le devrait (tel qu'expérimenté lors du dernier cours en classe).
# Lorsque je tente d'imprimer le tout c'est ce "charabia" qui s'affiche à chaque tentative: "UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 888: character maps to <undefined>".
# J'ai cherché sur de nombreux sites et essayé quelques manoeuvres pour me permettre de faire rouler mon script (que je n'ai pas gardées comme elles étaient toutes fausses ou infructueuses).
# La source qui me rapprochait le plus d'une conclusion pertinente était celle-ci : https://stackoverflow.com/questions/53954988/python-unicodedecodeerror-charmap-codec-cant-decode-byte-0x9d-in-position/53955085
# Selon cet extrait du site: "Update: the error "UnicodeDecodeError" already implies that python already tried to decode it with 'utf-8' but it failed. Therefore, using 'utf-8' is not an option.",
#   je comprends que l'erreur proviendrait du fameux "# coding : utf-8" qui débute chacun de nos codes. Je n'ai cependant aucune idée de la manière de procéder lors de ce genre d'erreur (mes sources trouvées ne donnant pas de solution).

# Pour ces raisons, il m'est assez ardu (en fait il m'est impossible) de vérifier si mon code s'exécute bien. 
# J'ai toutefois tenté de reproduire tout le code vu dans le dernier cours en classe en plus d'ajouter la variante de la boucle if/elif (méthode vue dans un cours antérieur) qui, je pense, me permet d'aller retirer les bonnes paires de mots.
# J'espère donc que j'arrive au résultat voulu. :-) 

