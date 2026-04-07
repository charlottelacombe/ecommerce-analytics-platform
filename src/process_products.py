# import biblio
# json pour lecture fichier -- dictionnaire 
# pandas pour lecture manipulation des donnees (tabulaires)

import json
import pandas as pd


# fonction principale contenant tout le traitement
# permet de controler quand le script est lancé (ex: Airflow)
def run():

    # ouverture fichier depuis ingestion en lecture, r --> read
    with open("data/raw/products_raw.json", "r") as f:

        # transformation du fichier json en format exploitable en Python
        data = json.load(f)

    # data étant un dictionnaire, je récupère les infos de la clé 'products'
    products = data['products']

    # transformer le fichier json en DF ( lecture tabulaire)
    df = pd.DataFrame(products)

    # Garder uniquement les colonnes utiles pour l'analyse sur dashboard interactif
    simple_cols = ["id","title","category","price","discountPercentage","rating","stock","brand","availabilityStatus","minimumOrderQuantity"]

    df_clean = df[simple_cols]

    # remplacement des valeurs manquantes par 'unknown'
    df_clean['brand'] = df_clean['brand'].fillna('unknown')

    # sauvegarde en CSV avec reset index
    df_clean.to_csv("data/processed/products_clean.csv", index=False)

    # verification
    print(df_clean.sample(10))


# ce bloc sert à dire :
# "si je lance ce fichier directement"
# alors execute la fonction run()
# sinon ne lance rien automatiquement
if __name__ == "__main__":
    run()