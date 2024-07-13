

def verification_ajout_produit(NOM_PRODUIT_PARAMETRE,PRIX_PRODUIT_PARAMETRE,QUANTITE_PRODUIT_PARAMETRE,LISTE_PRODUITS_PARAMETRE,VERIFICATEUR_PARAMETRE,ID_PARAMETRE):

    for PRODUIT in LISTE_PRODUITS_PARAMETRE: 
            
            if PRODUIT["NOM_PRODUIT"].lower() == NOM_PRODUIT_PARAMETRE.lower():   
                print(f"\n Attention 🚨🚨 le produit que vous voulez ajouter est déjà dans le stock😯\n")
                VERIFICATEUR_PARAMETRE = 1
                return VERIFICATEUR_PARAMETRE 
            
    try:
        NOM_PRODUIT_PARAMETRE = int(NOM_PRODUIT_PARAMETRE)  
    except :            
            try : 
                PRIX_PRODUIT_PARAMETRE= float(PRIX_PRODUIT_PARAMETRE) 
                QUANTITE_PRODUIT_PARAMETRE = int(QUANTITE_PRODUIT_PARAMETRE) 
            except : 
                    print(f"\n Attention 🚨🚨 il faut un entier pour  la quantité et le prix😯\n")
                    VERIFICATEUR_PARAMETRE = 1
                    return VERIFICATEUR_PARAMETRE
            else :
                    if NOM_PRODUIT_PARAMETRE == "" or PRIX_PRODUIT_PARAMETRE == "" or  QUANTITE_PRODUIT_PARAMETRE == "":
                            print(f"\n Attention 🚨🚨 touts les champs sont obligatoire😯\n RASSIREZ-VOUS D'AVOIR REMPLIR TOUTS LES CHAMPS\n")
                            VERIFICATEUR_PARAMETRE = 1
                            return VERIFICATEUR_PARAMETRE
                    
                    elif  len(NOM_PRODUIT_PARAMETRE) < 3 : 
                            print(f"\n MAUVAISE VALEUR POUR LE NOM DU PRODUIT🚨🚨 😯\n")
                            VERIFICATEUR_PARAMETRE = 1
                            return VERIFICATEUR_PARAMETRE
                    
                    elif float(PRIX_PRODUIT_PARAMETRE) <= 0 or  QUANTITE_PRODUIT_PARAMETRE <= 0:
                            print(f"\n Attention 🚨🚨 le nombre min pour le prix et la quantité c'est 1 😯\n")
                            VERIFICATEUR_PARAMETRE = 1
                            return VERIFICATEUR_PARAMETRE
                    else:
                            VERIFICATEUR_PARAMETRE = 2 
                            return VERIFICATEUR_PARAMETRE
    else:
        print(f"\n Attention 🚨🚨 vous venez de saisir un entier pour le nom du produit😯\n VEUILLEZ SAISIR UNE CHAINE DE CARACTERES\n")
  
               

def verification_enregistrer_vente(NOM_CLIENT_PARAMETRE,NOM_PRODUIT_PARAMETRE,QUANTITE_VENDU_PARAMETRE,VERIFICATEUR_PARAMETRE):

        try:
                    NOM_CLIENT_PARAMETRE = int(NOM_CLIENT_PARAMETRE)   
        except :   
                    try : 
                            QUANTITE_VENDU_PARAMETRE = int(QUANTITE_VENDU_PARAMETRE)  
                    except : 
                            print(f"\n Attention 🚨🚨 il faut un entier pour  la quantité  😯\n")
                    else :
                            if NOM_CLIENT_PARAMETRE == "" or NOM_PRODUIT_PARAMETRE == "" or  QUANTITE_VENDU_PARAMETRE == "":
                                print(f"\n Attention 🚨🚨 touts les champs sont obligatoire  😯\n RASSIREZ-VOUS D'AVOIR REMPLIR TOUTS LES CHAMPS \n")
                            elif  len(NOM_CLIENT_PARAMETRE) < 3 : 
                                print(f"\n Mauvaise valeur pour le nom du client 🚨🚨 😯\n LE NOM DU CLIENT DOIT CONTENIR 3 CARACTES MIN")
                            elif int(QUANTITE_VENDU_PARAMETRE) <= 0 :
                                    print(f"\n Attention 🚨🚨 le nombre min pour la quantité c'est 1 😯\n")
                            else:
                                    VERIFICATEUR_PARAMETRE = 1 
                                    return VERIFICATEUR_PARAMETRE
        else:
                print(f"\n Attention 🚨🚨 vous venez de saisir un entier pour nom DU CLIENT 😯\n VEUILLEZ SAISIR UNE CHAINE DE CARACTERES POUR CETTE CASE")
        return VERIFICATEUR_PARAMETRE

def  verification_modification(NOM_PRODUIT_PARAMETRE,PRIX_PRODUIT_PARAMETRE,QUANTITE_PRODUIT_PARAMETRE,VERIFICATEUR_PARAMETRE):
            try:
                    NOM_PRODUIT_PARAMETRE = int(NOM_PRODUIT_PARAMETRE) 
            except :
                try :
                    PRIX_PRODUIT_PARAMETRE = float(PRIX_PRODUIT_PARAMETRE)
                    QUANTITE_PRODUIT_PARAMETRE = int(QUANTITE_PRODUIT_PARAMETRE)
                except:
                        print(f"\n  Attention 🚨🚨 vous venez de saisir une chaine de caractères pour (la quantité ou prix unitaire)   😯\n RASSIREZ-VOUS D'AVOIR SAISIE LES ENTIERS POUR LES DEUX CASES\n")
                else:
                    if NOM_PRODUIT_PARAMETRE == "" or NOM_PRODUIT_PARAMETRE == "" or  QUANTITE_PRODUIT_PARAMETRE == "":
                        print(f"\n Attention 🚨🚨 touts les champs sont obligatoire  😯\n RASSIREZ-VOUS D'AVOIR REMPLIR TOUTS LES CHAMPS\n")
                    elif  len(NOM_PRODUIT_PARAMETRE) < 3 : 
                        print(f"\n MAUVAISE VALEUR POUR LE NOM DU PRODUIT🚨🚨 😯\n")
                    elif PRIX_PRODUIT_PARAMETRE <= 0 or  QUANTITE_PRODUIT_PARAMETRE <= 0:
                        print(f"\n Attention 🚨🚨 le nombre min pour le prix et la quantité c'est 1 😯\n")
                    else:
                        VERIFICATEUR_PARAMETRE = 1 
                        return  VERIFICATEUR_PARAMETRE 
            else:
                 print(f"\n Attention 🚨🚨 Venez de saisir un entier pour le nom du produit 😯\n RASSIREZ-VOUS D'AVOIR ENTRER UNE CHAINE DE CARACTERES\n")
            return  VERIFICATEUR_PARAMETRE


def recherche_produit(CHOIX_UTILISATEUR_PARAMETRE,VERIFICATEUR_PARAMETRE):
        if CHOIX_UTILISATEUR_PARAMETRE == "":
            print(f"\n Attention  🚨🚨 le champs de nom du produit ne doit pas resté vide\n VEUILLEZ LE REMPLIR SVP  😯\n")
        else:
            VERIFICATEUR_PARAMETRE = 1
            return VERIFICATEUR_PARAMETRE
        return VERIFICATEUR_PARAMETRE


def verification_vente(REPONSE_UTILISATUER_PARAMETRE,VERIFICATEUR_PARAMETRE):
        if REPONSE_UTILISATUER_PARAMETRE =="":
            print(f"\n Attention  🚨🚨 le champs pour le nom client est obligatoire\n VEUILLEZ LE REMPLIR SVP  😯\n")
        elif  REPONSE_UTILISATUER_PARAMETRE.isnumeric():
              print(f"\n Attention 🚨🚨 rien que une chaîne de caracters qui est valide pour le nom d'un produit 😯\n")
        elif  len(REPONSE_UTILISATUER_PARAMETRE) < 3 : 
             print(f"\n MAUVAISE VALEUR 🚨🚨 😯\n")
        else : 
             VERIFICATEUR_PARAMETRE = 1 
             return VERIFICATEUR_PARAMETRE
        
        return VERIFICATEUR_PARAMETRE