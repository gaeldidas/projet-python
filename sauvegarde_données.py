import json

def sauvergade_donnees_vente(LISTE_PARAMETRE):
    with open('rapport_vente.json','w+') as FICHIER:
            json.dump(LISTE_PARAMETRE,FICHIER)
   
def sauvergade_donnees_achat(LISTE_PARAMETRE):
    with open('Produit.json','w+') as FICHIER:
            json.dump(LISTE_PARAMETRE,FICHIER)
