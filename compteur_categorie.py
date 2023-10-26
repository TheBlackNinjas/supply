# Importation du module csv

import csv

# Ouverture du fichier CSV en mode lecture
with open('order_shipment.csv', 'r') as csvfile:
    # Création d'un lecteur CSV
    reader = csv.reader(csvfile)

    # Ignorer la première ligne (en-tête)
    next(reader)

    # Création d'un dictionnaire pour stocker le nombre d'occurrences de chaque catégorie
    category_count = {}

    # Parcours des lignes du fichier CSV
    for row in reader:
        # Extraction de la catégorie de la ligne à l'index 9
        category = row[9]

        # Vérification si la catégorie est déjà présente dans le dictionnaire
        if category in category_count:
            # Si oui, incrémentation du compteur
            category_count[category] += 1
        else:
            # Sinon, ajout de la catégorie au dictionnaire avec un compteur initial de 1
            category_count[category] = 1

# Parcours du dictionnaire des catégories et de leur nombre d'occurrences
for category, count in category_count.items():
    # Affichage de la catégorie et du nombre d'occurrences
    print(f"Catégorie : {category}, Nombre d'occurrences : {count}")
