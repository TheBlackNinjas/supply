# Importation des bibliothèques pandas et csv
import csv
import pandas as pd

# Nom du fichier CSV à traiter
nom_fichier = "order_shipment.csv"

# Lecture du fichier CSV dans un DataFrame
dataframe = pd.read_csv(nom_fichier)

# Vérification de l'existence de la colonne "Customer ID" dans le DataFrame
if " Customer ID " in dataframe.columns:
    # Conversion de la colonne "Customer ID" en chaînes de caractères (str)
    dataframe[" Customer ID "] = dataframe[" Customer ID "].astype(str)

    # Nom du fichier où le DataFrame modifié sera enregistré
    nom_fichier_modifie = "order_shipment.csv"

    # Enregistrement du DataFrame modifié dans un nouveau fichier CSV
    # avec l'argument index=False pour ne pas inclure l'index des lignes dans le fichier résultant
    dataframe.to_csv(nom_fichier_modifie, index=False)

# Affichage du type de données (dtype) de la colonne "Customer ID"
print(dataframe[" Customer ID "].dtypes)
