# Importation des bibliothèques pandas et csv
import csv
import pandas as pd
from collections import defaultdict

# Nom du fichier CSV à traiter
nom_fichier = "order_shipment.csv"

# Lecture du fichier CSV dans un DataFrame
dataframe = pd.read_csv(nom_fichier)

# Conversion de la colonne 'date_order' en datetime
dataframe['date_order'] = pd.to_datetime(dataframe['date_order'])

# Comptage du nombre de dates uniques pour chaque 'Order ID'
date_counts = dataframe.groupby('Order ID ')['date_order'].nunique()

# Sélection des 'Order ID' avec exactement 2 dates uniques
order_ids_with_two_dates = date_counts[date_counts == 2].index

# Affichage des 'Order ID' avec deux dates uniques
print(order_ids_with_two_dates)

# Affichage du nombre de 'Order ID' avec deux dates uniques
print(len(order_ids_with_two_dates))


# Ouverture du fichier CSV d'origine avec le module csv
data = []
with open('order_shipment.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(row)

# Création d'un dictionnaire defaultdict pour regrouper les dates par 'Order ID'
order_id_dict = defaultdict(list)

# Remplissage du dictionnaire avec les dates associées à chaque 'Order ID'
for row in data:
    order_id = row['Order ID ']
    order_date = row['date_order']
    order_id_dict[order_id].append(order_date)

# Boucle pour parcourir le dictionnaire et vérifier les 'Order ID' avec plus d'une date
a = 0
for order_id, dates in order_id_dict.items():
    if len(dates) > 1:
        if len(set(dates)) > 1:
            print(f"L'Order ID {order_id} a des commandes à des dates différentes : {', '.join(dates)}")
            a = a + 1

# Affichage du nombre d'Order ID avec plus d'une date
print(a)
