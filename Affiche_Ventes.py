import json

from Charger_donnees import *


def afficher_vente():
    
    LISTE_VENTE = charger_donnees_vente()
    print(f"\n VENTES")
    COMPTEUR = 0  

    for VENTE in LISTE_VENTE: 
        COMPTEUR +=1
        print(f"ID VENTE {VENTE['ID']} |NOM CLIENT  {VENTE['Nom_client']} |PRODUIT {VENTE['Nom_produit']} | QUANTITE {VENTE['Quantite']} |PRIX UNITAIRE {VENTE['Prix_unitaire']} |PRIX A PAYER {VENTE['Prix_payer']} |DATE {VENTE['Date']} |HEURE {VENTE['Heure']}")
        print("========================================================================================================================================")
    if COMPTEUR == 0: 
        print("\n Il y a aucunne vente effectuée\n")
    