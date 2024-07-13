import json

def charger_donnees_produit():
    with open ('Produit.json','r') as FICHIER: 
         LISTE_PRODUITS = json.load(FICHIER)
         return LISTE_PRODUITS

def charger_donnees_vente():
    with open('rapport_vente.json','r') as FICHIER:
        LISTE_RAPPORT = json.load(FICHIER)
    return LISTE_RAPPORT

