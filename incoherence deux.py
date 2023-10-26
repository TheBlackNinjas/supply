# Importation de la bibliothèque pandas
import pandas as pd

# Lecture du fichier CSV 'order_shipment.csv' dans un DataFrame
df = pd.read_csv('order_shipment.csv')

# Sélection des lignes du DataFrame ayant la date la plus basse pour chaque 'Order ID'
# en utilisant la méthode idxmin() pour identifier l'index de la ligne ayant la date minimale
df = df.loc[df.groupby('Order ID ')['date_order'].idxmin()]

# Affichage du DataFrame résultant, contenant uniquement les lignes avec la date la plus basse
print(df)

# Affichage du nombre de lignes dans le DataFrame
print(len(df))

# Nom du fichier où le DataFrame modifié sera enregistré
nom_fichier_modifie = "order_shipment.csv"

# Enregistrement du DataFrame modifié dans un nouveau fichier CSV
# avec l'argument index=False pour ne pas inclure l'index des lignes dans le fichier résultant
df.to_csv(nom_fichier_modifie, index=False)
