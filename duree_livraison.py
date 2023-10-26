# Importation des bibliothèques pandas et csv
import csv
import pandas as pd

# Nom du fichier CSV à traiter
nom_fichier = "order_shipment.csv"

# Lecture du fichier CSV dans un DataFrame
dataframe = pd.read_csv(nom_fichier)

# Conversion des colonnes 'date_order' et 'date_ship' en objets datetime
dataframe['date_order'] = pd.to_datetime(dataframe['date_order'])
dataframe['date_ship'] = pd.to_datetime(dataframe['date_ship'])

# Calcul du temps de traitement Commande-Livraison en jours
dataframe['Temps de traitements Commande-Livraison (Jours)'] = (dataframe['date_ship'] - dataframe['date_order']).dt.days

# Filtrage des lignes où le temps de traitement est supérieur ou égal à zéro (pour éviter les valeurs négatives)
dataframe = dataframe[dataframe['Temps de traitements Commande-Livraison (Jours)'] >= 0]

# Affichage du DataFrame résultant avec les modifications
print(dataframe)

# Nom du fichier où le DataFrame modifié sera enregistré
nom_fichier_modifie = "order_shipment.csv"

# Enregistrement du DataFrame modifié dans un nouveau fichier CSV
# avec l'argument index=False pour ne pas inclure l'index des lignes dans le fichier résultant
dataframe.to_csv(nom_fichier_modifie, index=False)
