# Importation des bibliothèques pandas et csv
import csv
import pandas as pd

# Nom du fichier CSV à traiter
nom_fichier = "order_shipment.csv"

# Lecture du fichier CSV dans un DataFrame
dataframe = pd.read_csv(nom_fichier)

# Conversion des colonnes 'Order Year', 'Order Month', et 'Order Day' en une colonne 'date_order'
# qui représente la date complète au format 'dd/mm/YYYY'
dataframe['date_order'] = pd.to_datetime(dataframe[[' Order Year ', ' Order Month ', ' Order Day ']].astype(str).agg('-'.join, axis=1), format='%Y-%m-%d')

# Formatage de la colonne 'date_order' pour qu'elle ait le format 'dd/mm/YYYY'
dataframe['date_order'] = dataframe['date_order'].dt.strftime('%d/%m/%Y')

# Affichage du DataFrame résultant avec la colonne 'date_order' modifiée
print(dataframe['date_order'])

# Nom du fichier où le DataFrame modifié sera enregistré
nom_fichier_modifie = "order_shipment.csv"

# Enregistrement du DataFrame modifié dans un nouveau fichier CSV
# avec l'argument index=False pour ne pas inclure l'index des lignes dans le fichier résultant
dataframe.to_csv(nom_fichier_modifie, index=False)
