# import biblio
# json pour lecture fichier -- dictionnaire 
# pandas pour lecture maninulation des donnes ( tabulaires)

import json
import pandas as pd

# ouverture fichier depuis ingestion en lecture, r --> read
with open("data/raw/products_raw.json", "r") as f:

    # transformation du fichier json en format exploitable en Python
    data = json.load(f)

# data étant un dictionnaire, je récupère les infos de la clé 'products'
products = data['products']

# data est un dictionnaire
# products est une liste contenant des dictionnaires
#print(type(data))
#print(type(products))
#print(products)

# transformer le fichier json en DF ( lecture tabulaire)
df = pd.DataFrame(products)

# Garder uniquement les colonnes utiles pour l'annalyse sur dashboard interactif
simple_cols = ["id","title","category","price","discountPercentage","rating","stock","brand","availabilityStatus","minimumOrderQuantity"]

df_clean = df[simple_cols]

# remplacement des 62 valeurs manquantes par 'unknown'
df_clean['brand'] = df_clean['brand'].fillna('unknown')

# sauvegarde en CSV avec reset index
df_clean.to_csv("data/processed/products_clean.csv", index=False)

# verification
print(df_clean.sample(10))