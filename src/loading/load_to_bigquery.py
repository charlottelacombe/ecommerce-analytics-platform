# import biblio 
# pandas pur lecture CSV 
# big query pur envoyer les donnes vers BigQuery 
import pandas as pd
from google.cloud import bigquery

# fonction principale 
# contient tout le travail du script 
def run () :
    print('Debut chanrgement en big querry')

    # chemin du fichier csv propre 
    file_path = "data/processed/products_clean.csv"

    # lecture fichier csv 
    # tranformation en dataFrame 
    df = pd.read_csv(file_path)

    # affichier le shape du df 
    print('shape df : ', df.shape)

    # creation du client dans bigquery
    client = bigquery.Client()

    # connection avec ma table dans bigQuery
    table_id = "burnished-ether-490123-c8.ecommerce_analytics.products"

    # envoi des donnes vers BigQuery
    # j'envoi mon df vers la table
    job = client.load_table_from_dataframe(df, table_id)

    # attendre que le chargement soit terminé
    job.result()


    print("Chargement terminé dans BigQuery")


# lancer le script seulement si exécuté directement
if __name__ == "__main__":
    run()



