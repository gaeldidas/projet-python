
import sys
from Ajout_Produits import *
from Afficher_Produits import *
from Rechercher_Produit import *
from enregistrer_vente import *
from Affiche_Ventes import *
from vente_client import *
from Rapport import *
from Charger_donnees import * 
from modiffier import * 


LISTE_PRODUITS = [] 
LISTE_PRODUITS = charger_donnees_produit() 

MENU = """\n MENU PRINCIPAL\n""" """
                1.  Ajouter produit
                2.  Afficher produits
                3.  Rechercher produit
                4.  Enregistrer vente
                5.  Afficher ventes
                6.  Ventes par client
                7.  Générer rapport de ventes
                8.  Charger données
                9.  Quitter
                 Votre choix : """

MENU_CHOICES = ["1","2","3","4","5","6","7","8","9","10","11","12"]   

while True:    
        CHOIX_UTILISATEUR = "" 
        while CHOIX_UTILISATEUR not in MENU_CHOICES: 
            CHOIX_UTILISATEUR = input(MENU)
            if CHOIX_UTILISATEUR not in MENU_CHOICES:
                print("Veuillez Choisir une option valide...")
        if CHOIX_UTILISATEUR == "1":
            ajouter_Produits(LISTE_PRODUITS)
        elif CHOIX_UTILISATEUR =="2":
            Afficher_Produit(LISTE_PRODUITS)
        elif CHOIX_UTILISATEUR == "3":
            rechercher_produit()
        elif CHOIX_UTILISATEUR =="4":
            Enregistrer_vente(LISTE_PRODUITS)
        elif CHOIX_UTILISATEUR  == "5":
            afficher_vente()
        elif CHOIX_UTILISATEUR =="6":
            vente_client ()
        elif CHOIX_UTILISATEUR == "7":
            rapport()
        elif CHOIX_UTILISATEUR =="8":
            charger_donnees_produit()
            charger_donnees_vente()
            print("\n tchargement de données terminer\n")
        elif CHOIX_UTILISATEUR == "9":
            print("\n À BIENTÔT...")
            sys.exit() 