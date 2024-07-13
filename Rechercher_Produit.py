import json 

from Verification_saisies import *
from Charger_donnees import *
from suppression_prduit import * 
from modiffier import * 


def rechercher_produit():

    LISTE_PRODUIT = charger_donnees_produit()
    
    RESULTAT = []  
    COMPTEUR = 0
    VERIFICATEUR = 0


    Menu_choix = input("\n 1. Rechercher par nom\n 2. Rechercher par ID\n Votre choix :")
       
    if Menu_choix == "1":
        nom = input("\n Entrez le du client : ")
        for PRODUIT in LISTE_PRODUIT:  
            if PRODUIT['NOM_PRODUIT'].lower() == nom.lower():  
                COMPTEUR +=1
                RESULTAT.append(PRODUIT)
        if COMPTEUR == 0:
            print(f"\n Aucun produit porte le nom  {nom} 😯\n")
            return
        else:
            print (f"\n LE PRODUIT A ETE TROUVE\n")
            
            for PRODIT_DISP in RESULTAT:
                print(f"ID : {PRODIT_DISP['ID_PRODUIT']} | NOM PRODUIT : {PRODIT_DISP['NOM_PRODUIT']} | PRIX : {PRODIT_DISP['PRIX_PRODUIT']} | QUANTITE EN STOCK :  {PRODIT_DISP['QUANTITE']}")
                print("\t\t================================================================================")

    elif Menu_choix == "2": 
        id_pro = input("\n Entrez l'ID : ")
        for PRODUIT in LISTE_PRODUIT: 
            if str(PRODUIT['ID_PRODUIT']) == id_pro:   
                COMPTEUR +=1
                RESULTAT.append(PRODUIT)
        if COMPTEUR == 0:
            print(f"\n Aucun produit porte l'ID  {id_pro} 😯\n")
            return
        else:
            print (f"\n \t\t\t\tLE PRODUIT A ETE TROUVE\n")
            
            for PRODIT_DISP in RESULTAT:
                print(f"ID : {PRODIT_DISP['ID_PRODUIT']} | NOM PRODUIT : {PRODIT_DISP['NOM_PRODUIT']} | PRIX : {PRODIT_DISP['PRIX_PRODUIT']} | QUANTITE EN STOCK :  {PRODIT_DISP['QUANTITE']}")
                print("================================================================================")
    elif Menu_choix != "1" or Menu_choix != "2":
        print("\n Mauvais choix")
        return
    
    MENU = Fore.BLUE +"""\n
                        1.  supprimer le produit
                        2.  modifier
                        3.  Quitter
                        Votre choix : """

    MENU_CHOICES = ["1","2","3"]   

    while True:    
                        CHOIX_UTILISATEUR = "" 
                        while CHOIX_UTILISATEUR not in MENU_CHOICES:
                            CHOIX_UTILISATEUR = input(MENU)
                            if CHOIX_UTILISATEUR not in MENU_CHOICES:
                                print("Veuillez Choisir une option valide...")
                        if CHOIX_UTILISATEUR == "1":  
                            suppr_produit(PRODIT_DISP['ID_PRODUIT'])
                            return
                        elif CHOIX_UTILISATEUR =="2":
                            modification(PRODIT_DISP['ID_PRODUIT'],RESULTAT)
                            return
                        elif CHOIX_UTILISATEUR == "3":
                            return 