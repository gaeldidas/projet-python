
from Charger_donnees import *

def Afficher_Produit(LISTE_PARAMETRE):
    
    LISTE_PARAMETRE = charger_donnees_produit()  
    print("""\n  LE PRODUITS EN STOCK\n""")
    COMPTEUR = 0  
    for PRODUIT in LISTE_PARAMETRE: 
        COMPTEUR +=1
        print(f" ID : {PRODUIT['ID_PRODUIT']}| NOM PRODUIT : {PRODUIT['NOM_PRODUIT']}  | PRIX  : {PRODUIT['PRIX_PRODUIT']} | QUANTITE EN STOCK : {PRODUIT['QUANTITE']}")
        print("================================================================================")
    if COMPTEUR == 0: 
            print("\n Il y a aucun produit dans le stock \n")
            return 
    return LISTE_PARAMETRE


