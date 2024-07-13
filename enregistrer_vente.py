
from produits_dispo import * 
from Verification_saisies import *
from sauvegarde_données import *
from Charger_donnees import *
from sauvegarde_données import * 
from datetime import datetime
import time 


def Enregistrer_vente(LISTE_PRODUITS_PARAMETRE):
    LISTE_PRODUITS_RAPPORT = charger_donnees_vente()  
    RESULTAT = {"ID":0,"Nom_client":0,"Nom_produit":0,"Quantite":0,"Prix_unitaire":0,"Prix_payer":0,"Date":0,"Heure":0}  
    COMPTEUR = 0  
    VERIFICATEUR = 0 
    ETAT_STOCK = 0   
    ETAT_STOCK,LISTE_PRODUITS_PARAMETRE = Afficher_Produit_dispo(LISTE_PRODUITS_PARAMETRE)  
    if ETAT_STOCK == 0:
        return 
    else: 
        while VERIFICATEUR == 0: 
            NOM_CLIENT  = input("Entrez le nom du client : ")
            NOM_PRODUIT = input("Entrez le nom du produit : ")
            QUANTITE_VENDU = input("Entrez la quantité : ")

            VERIFICATEUR =  verification_enregistrer_vente(NOM_CLIENT,NOM_PRODUIT,QUANTITE_VENDU,VERIFICATEUR) 
        for PRODUIT in LISTE_PRODUITS_PARAMETRE:
   
            if  PRODUIT['NOM_PRODUIT'].lower() == NOM_PRODUIT.lower() and int(QUANTITE_VENDU) > 0   and int(PRODUIT['QUANTITE']) >= int(QUANTITE_VENDU) :  
                COMPTEUR +=1
                id = len(LISTE_PRODUITS_RAPPORT)+1  
                heure = time.strftime('%H:%M:%S')  
                date = datetime.today().strftime('%d/%m/%Y')  
                
                PRIX_TOTAL_A_PAYER = float(int(QUANTITE_VENDU)* PRODUIT['PRIX_PRODUIT'])
                RESULTAT['ID']=(id)
                RESULTAT['Nom_client']=(NOM_CLIENT.capitalize())
                RESULTAT['Nom_produit']= NOM_PRODUIT
                RESULTAT['Quantite']=int(QUANTITE_VENDU)
                RESULTAT['Prix_unitaire']= (PRODUIT['PRIX_PRODUIT'])
                RESULTAT['Prix_payer'] =(PRIX_TOTAL_A_PAYER)
                RESULTAT['Date']=(date)
                RESULTAT['Heure']=(heure)
                PRODUIT['QUANTITE']=(PRODUIT['QUANTITE'] - int(QUANTITE_VENDU))

                LISTE_PRODUITS_RAPPORT.append(RESULTAT)
                sauvergade_donnees_vente(LISTE_PRODUITS_RAPPORT)  
                sauvergade_donnees_achat(LISTE_PRODUITS_PARAMETRE) 
                print("\n \tL'évément a été bien enregistré\n")
               
        if COMPTEUR == 0:
            print("\n echec de vente 🚨 soit :\n le produit ne pas disponible,\n la quantité vendu est supérieure à la Quantité en stock pour ce produit. ")
        


