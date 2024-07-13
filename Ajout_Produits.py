import json
from Verification_saisies import * 
from Charger_donnees import * 
from sauvegarde_données import *
from datetime import datetime
import time 

def ajouter_Produits(LISTE_PARAMETRE):
        DICTIONNAIRE_INTERMEDIAIRE = {"ID_PRODUIT":0,"NOM_PRODUIT":0,"PRIX_PRODUIT":0,"QUANTITE":0,"DATE":0,"HEURE":0} 
        if LISTE_PARAMETRE == []:
            id = len(LISTE_PARAMETRE)+1
        else:
              id = LISTE_PARAMETRE[-1]['ID_PRODUIT']
              id = id + 1
        VERIFICATEUR  = 0  
        print("""\n ENREGISTREMENT DU PRODUIT""")
        while VERIFICATEUR < 2:

            if VERIFICATEUR == 1 : 
                REP_UTILISATEUR = input("VOULEZ-VOUS QUITTER (QUITTER) OU BIEN MODIFIER (CONTINUE) ?: ")
                if REP_UTILISATEUR.lower() == "QUITTER".lower():  
                            print("VOUS VENEZ D'ANNULER L'OPERATION  ") 
                            return
                elif REP_UTILISATEUR.lower() == "CONTINUE".lower():  
                    LISTE_PRODUITS = charger_donnees_produit()  
                    NOM_PRODUIT  = input("Entrez le nom du produit : ")
                    PRIX_PRODUIT  = input("Entrez le prix du produit : ")
                    QUANTITE_PRODUIT = input("Entrez la quantité du produit : ")

                    VERIFICATEUR = verification_ajout_produit(NOM_PRODUIT,PRIX_PRODUIT,QUANTITE_PRODUIT,LISTE_PRODUITS,VERIFICATEUR,id)
                else:
                      VERIFICATEUR = 1
            else:
                LISTE_PRODUITS = charger_donnees_produit()  
                NOM_PRODUIT  = input("Entrez le nom du produit : ")
                PRIX_PRODUIT  = input("Entrez le prix du produit : ")
                QUANTITE_PRODUIT = input("Entrez la quantité du produit : ")

                VERIFICATEUR = verification_ajout_produit(NOM_PRODUIT,PRIX_PRODUIT,QUANTITE_PRODUIT,LISTE_PRODUITS,VERIFICATEUR,id)

        PRIX_PRODUIT = float(PRIX_PRODUIT)   
        DICTIONNAIRE_INTERMEDIAIRE['ID_PRODUIT']=id
        DICTIONNAIRE_INTERMEDIAIRE['NOM_PRODUIT'] = NOM_PRODUIT
        DICTIONNAIRE_INTERMEDIAIRE['PRIX_PRODUIT']= PRIX_PRODUIT
        DICTIONNAIRE_INTERMEDIAIRE['QUANTITE']= int(QUANTITE_PRODUIT)
        heure = time.strftime('%H:%M:%S')   
        date = datetime.today().strftime('%d/%m/%Y')
        DICTIONNAIRE_INTERMEDIAIRE['DATE']= date
        DICTIONNAIRE_INTERMEDIAIRE['HEURE'] = heure 

        LISTE_PARAMETRE.append(DICTIONNAIRE_INTERMEDIAIRE) 
        
        sauvergade_donnees_achat(LISTE_PARAMETRE)  

        print("\n Le produit à été bien ajouter en stock \n")
        return LISTE_PARAMETRE


