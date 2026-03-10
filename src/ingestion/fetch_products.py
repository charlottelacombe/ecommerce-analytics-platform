# import biblio 
import requests
import json 

# URL de l'AI 
# base + products . limits à 5 
URL = "https://dummyjson.com/products?limit=5"

# affichage message pour verifier si le script demarre bien 
print("Appel en cours... ")

# envoi requete GET à l'api 
response = requests.get(URL)

# verification si connexion bien etablie 
# on trabnsforme la reponse de l'api en JSON exploitable 
if response.status_code == 200:
    data = response.json()

    # verif combien de produit on etait recuperes 
    print('produits recuperes : ', len(data['products']))

    #ouverture du fichier en mode ecriture as f pour fichier 
    with open("data/raw/products_raw.json", "w") as f :
        # dump --> ecrit les donnees json dans le fichier 
        # indentation à 4 pour rendre plus lisible 
        json.dump(data,f,indent=4)


    # message de confirmation 
    print("Fichier JSON sauvegardé dans data/raw/products_raw.json")

else:
    # si pas de rponse 200 
    print('erreur api :', response.status_code)

    
