# Importation des bibliothèques pandas et csv pour la manipulation de données CSV
import csv
import pandas as pd

# Nom du fichier CSV à traiter
nom_fichier = "inventaire.csv"

# Lecture du fichier CSV dans un DataFrame
dataframe = pd.read_csv(nom_fichier)

# Création d'une nouvelle colonne "Cout d_inventaire par nombre d_inventaire"
# en multipliant les valeurs des colonnes "Warehouse Inventory" et "Inventory Cost Per Unit"
dataframe['Cout d_inventaire par nombre d_inventaire'] = dataframe[' Warehouse Inventory '] * dataframe['Inventory Cost Per Unit']

# Affichage du DataFrame avec la nouvelle colonne calculée
print(dataframe)
