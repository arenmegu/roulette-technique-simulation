"""
================================================================================
Projet : Simulation d'une stratégie de roulette
Auteur : arenmegu
Date : 09/09/2024
Version : 0.3
================================================================================

Description :
    Ce programme est une simulation d'une stratégie pour gagner à la roulette.
    Les utilisateurs peuvent simuler grâce à ce programme une roulette et observer des estimations concernant cette stratégie

Outils utilisés :
    - Python : Pour le développement du programme
    - MatPlotLib : Pour la gestion des graphes
    - Random : Pour générer un nombre aléatoire (via une façon déterministe)
    - System : Pour mettre fin au programme
    
Fonctionnalités :
    - Simuler la roulette
    - Affichage Textuel et Graphique d'une simulation
    
Notes :
    - Ce projet est encore en développement et non fini.
    - Le code est structuré selon les conventions de base de python
    - On utilise le CamelCase pour le nom des fonctions/méthodes et le snake_case pour le nom des variables
    - L'intégralité du projet sera rédigé en français
    
Licence :
    Ce projet est sous licence MIT. Vous êtes libre de l'utiliser, de le modifier et
    de le distribuer à condition de conserver les mentions de l'auteur original.

================================================================================
"""


from random import randint 
import sys
import matplotlib.pyplot as plt

# -------------------------------------------------------------------------
# Initialisation des variables : nombre de victoires/défaites, tableau pour
# stocker le nombre de fois qu'un numéro tombe ainsi que le nombre de fois 
# que la "ligne forte" est tirée
# -------------------------------------------------------------------------

nb_victoires = 0
nb_défaites = 0
ligne_forte = 0
tirage_nombre = [0] * 37

# -------------------------------------------------------------------------
# Fonctions
# -------------------------------------------------------------------------

def roulette():
    """
    Génère un nombre aléatoire dans l'intervalle [0;36]

    Retour
    -------
    int
        Un entier tiré aléatoirement
    """
    return randint(0, 36)

def tirage():
    """
    Fonction qui va simuler un tour de roulette en utilisant la stratégie
    """
    global ligne_forte, nb_défaites,nb_victoires
    nombre_tiré = roulette()
    tirage_nombre[nombre_tiré] += 1
    if nombre_tiré in [2,8,11,14,17,20,23,26,29]:
        ligne_forte +=1
    if nombre_tiré in [3,6,9,5,10,16,22,25,32,33,34,35,36]:
        nb_défaites += 1
    else :
        nb_victoires += 1

def simulationRoulette(nbOccurences):
    """
    Fonction qui va simuler un certain nombre de tours de roulette

    Paramètre
    -------
    int
        Nombre de tours à réaliser
    """

    for i in range(nbOccurences):
            tirage()

def informationNumero(i):
    """
    Afficher les informations relatives au numéro donné en paramètre à savoir le numéro, le nombre de fois qu'il a été tiré et la probabilité de tomber dessus

    Paramètre
    -------
    int
        Le numéro dont il faut afficher les informations
    """
    print("Numéro ",i," - Nombre de tirages : ", tirage_nombre[i], " - Pourcentage de chance : ", tirage_nombre[i]/(nb_victoires+nb_défaites) * 100, " %")

def affichageInformationNuméro():
    """
    Affiche les informations relatives à chaque numéro présent sur le plateau (donc les entiers naturels présent dans [0,36])
    """
    for i in range(37):
            informationNumero(i)

def affichageMenuPrincipal():
    """
    Affiche le menu principal : logo + propositions
    1 - Visualisation Textuelle
    2 - Visualisation Graphique
    3 - Visualisation Textuelle et Graphique
    4 - Sortie du programme
    """
    print("""\033c
        >>=======================================================<<
        ||                                                       ||
        ||   ____             _      _   _                       ||
        ||  |  _ \ ___  _   _| | ___| |_| |_ ___                 ||
        ||  | |_) / _ \| | | | |/ _ | __| __/ _ \                ||
        ||  |  _ | (_) | |_| | |  __| |_| ||  __/                ||
        ||  |_| \_\___/ \__,_|_|\___|\__|\__\___|                ||
        ||   _____         _           _                         ||
        ||  |_   ____  ___| |__  _ __ (_) __ _ _   _  ___        ||
        ||    | |/ _ \/ __| '_ \| '_ \| |/ _` | | | |/ _ \       ||
        ||    | |  __| (__| | | | | | | | (_| | |_| |  __/       ||
        ||    |_|\___|\___|_| |_|_| |_|_|\__, |\__,_|\___|       ||
        ||                                  |_|                  ||
        ||   ____  _                 _       _   _               ||
        ||  / ___|(_)_ __ ___  _   _| | __ _| |_(_) ___  _ __    ||
        ||  \___ \| | '_ ` _ \| | | | |/ _` | __| |/ _ \| '_ \   ||
        ||   ___) | | | | | | | |_| | | (_| | |_| | (_) | | | |  ||
        ||  |____/|_|_| |_| |_|\__,_|_|\__,_|\__|_|\___/|_| |_|  ||
        ||                                                       ||
        >>=======================================================<<""")
    print("Merci de sélectionner parmi les propositions :\n1 - Visualisation Textuelle\n2 - Visualisation Graphique\n3 - Visualisation Texuelle et Graphique\n4 - Quitter")
def menuPrincipal():
    """
    Traitement (backend) du menu principal

    Retour
    ------
    tuple[bool,bool]
        Tuple défini en fonction du choix de l'utilisateur 
    """
    affichageMenuPrincipal()
    entree = int(input("\n>> "))
    while(True):
        match entree :
            case 1 :
                return (True,False)
            case 2 :
                return (False,True)
            case 3 :
                return (True,True)
            case 4 :
                print("Sortie en cours...")
                sys.exit(0)
            case _ :
                print("Erreur, entrée non reconnue")

def affichageResultatsTextuel():
    """
    Affichage des variables globales et affichage des statistiques, réalisé une fois un tirage réalisé
    """
    print("\033cNombre de Victoires : ", nb_victoires)
    print("Nombre de Défaites : ", nb_défaites)

    print("Pourcentage de chance de gagner : ", (nb_victoires/(nb_victoires + nb_défaites)) * 100, " %")
    print("Pourcentage de chance de perdre : ", (nb_défaites/(nb_victoires + nb_défaites)) * 100, " %")

    print("Pourcentage de chance de tomber sur la ligne forte : ", (ligne_forte/(nb_victoires + nb_défaites)) * 100, " %")

    print("Voulez vous afficher le nombre de tirage et le pourcentage de chance de tomber sur un numéro pour chaque numéro ?")
    print("\n1 - Oui\n2 - Non")
    while(True):
        entree = int(input("\n>> "))
        match entree :
            case 1 :
                affichageInformationNuméro()
                break
            case 2 :
                break
            case _ :
                print("Entrée non reconnue")

def affichageResultatsGraphique():
    """
    Toute la partie affichage du modélisation/graphique à réaliser donc TODO
    """
    pass

def lancementRouletteTextuelle():
    """
    Fonction appelée si on souhaite avoir une simulation textuelle
    """
    print("\033cSimulation en cours...")
    simulationRoulette(10000000)
    affichageResultatsTextuel()

def lancementRouletteGraphique():
    """
    Fonction appelée si on souhaite avoir une simulation graphique
    """
    print("\033cSimulation en cours...")
    simulationRoulette(10000)
    print("\033c")
    affichageResultatsGraphique()

def nettoyageValeurs():
    """
    Fonction pour nettoyer les valeurs déjà enregistrées
    """
    global nb_défaites, nb_victoires, ligne_forte, tirage_nombre
    nb_victoires = 0
    nb_défaites = 0
    ligne_forte = 0
    tirage_nombre = [0] * 37


# -------------------------------------------------------------------------
# Partie affichage
# -------------------------------------------------------------------------

if __name__ == '__main__':

    # Menu principal avec 4 entrées disponibles
    choix = menuPrincipal()

    # Affichage Textuel
    if (choix[0]):
        lancementRouletteTextuelle()

    # On efface tout le travail antérieur pour laisser place à la potentielle simulation graphique
    nettoyageValeurs()

    # On attend confirmation puis on lance la simulation graphique
    if (choix[0] and choix[1]):
        print("Voulez vous démarrer la simulation graphique ?")
        if((input()) == "oui" ):
            lancementRouletteGraphique()
            affichageResultatsGraphique()
            sys.exit(0)
        else :
            sys.exit(0)

    # Affichage Graphique
    if (choix[1]):
        lancementRouletteGraphique()
        pass