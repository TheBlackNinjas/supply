# Importation de la bibliothèque pandas pour la manipulation de données CSV
import pandas as pd
import csv
# Nom du fichier CSV à traiter
nom_fichier = "exécution.csv"

# Lecture du fichier CSV dans un DataFrame
dataframe = pd.read_csv(nom_fichier)

# Vérification de l'existence de la colonne " Warehouse Order Fulfillment (days) "
if " Warehouse Order Fulfillment (days) " in dataframe.columns:
    # Conversion de la colonne en chaînes de caractères (str)
    dataframe[" Warehouse Order Fulfillment (days) "] = dataframe[" Warehouse Order Fulfillment (days) "].astype(str)

    # Remplacement des points par des virgules dans la colonne
    dataframe[" Warehouse Order Fulfillment (days) "] = dataframe[" Warehouse Order Fulfillment (days) "].str.replace('.', ',')

    # Nom du fichier où le DataFrame modifié sera enregistré
    nom_fichier_modifie = "exécution.csv"

    # Enregistrement du DataFrame modifié dans un nouveau fichier CSV
    dataframe.to_csv(nom_fichier_modifie, index=False)

    # Message d'information sur l'enregistrement du fichier modifié
    print(f"Le fichier modifié a été enregistré sous '{nom_fichier_modifie}'.")
else:
    # Message en cas d'absence de la colonne recherchée
    print("La colonne 'Warehouse Order Fulfillment' n'a pas été trouvée dans le fichier " + nom_fichier + ".")

# Ouverture du fichier CSV d'origine en mode lecture avec le module csv
with open(nom_fichier, 'r') as fichier_csv:
    lecteur_csv = csv.reader(fichier_csv)

    # Lecture et affichage de chaque ligne du fichier CSV d'origine
    for ligne in lecteur_csv:
        print(ligne)
