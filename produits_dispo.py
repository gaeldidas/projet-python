import json 
from Charger_donnees import * 

def Afficher_Produit_dispo(LISTE_PARAMETRE):
    
    LISTE_PARAMETRE = charger_donnees_produit() 

    print("\n \t\t\t\tLES PRODUITS DISPONIBLES \n")
    COMPTEUR = 0
    for PRODUIT in LISTE_PARAMETRE:
        if PRODUIT['QUANTITE'] > 0 : 
            COMPTEUR +=1
            print(f" ID : {PRODUIT['ID_PRODUIT']} | NOM PRODUIT : {PRODUIT['NOM_PRODUIT']}  | PRIX  : {PRODUIT['PRIX_PRODUIT']} | QUANTITE EN STOCK : {PRODUIT['QUANTITE']}")
            print("\t\t ================================================================================")
    if COMPTEUR == 0:
        print("\n LE STOCK EST VIDE\n")
    return COMPTEUR,LISTE_PARAMETRE