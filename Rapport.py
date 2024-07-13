from datetime import datetime
from Charger_donnees import *
import json


def rapport ():

    LISTE_VENTE = charger_donnees_vente()

    COMPTEUR2 = 0
    COMPTEUR3 = 0
    date = datetime.today().strftime('%d/%m/%Y')

    print("\n RAPPORT JOURNALIER:")

    print("\n VENTES \n")
          
    for VENTE in LISTE_VENTE: 
            COMPTEUR2 +=1
            print(f"ID VENTE {VENTE['ID']} |NOM CLIENT {VENTE['Nom_client']} |NOM PRODUIT {VENTE['Nom_produit']} |QUANTITE {VENTE['Quantite']} |PRIX UNITAIRE {VENTE['Prix_unitaire']} |PRIX TOTAL A PAYER {VENTE['Prix_payer']} |DATE {VENTE['Date']} |HEURE {VENTE['Heure']}")
            print("===========================================================================================================================================================")
    if COMPTEUR2 == 0:
         print("\n AUCUNNE VENTE A ETE FAITE AUJOURD'HUI\n")