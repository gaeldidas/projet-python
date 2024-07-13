from Charger_donnees import * 
from sauvegarde_données import *


def suppr_produit (POSITION):
    LISTE_PRODUITS = charger_donnees_produit()
    del LISTE_PRODUITS[POSITION-1]
    print("le produit est supprimer")
    sauvergade_donnees_achat (LISTE_PRODUITS)
    