"""
================================================================================
Projet : Simulation d'une stratégie de roulette
Auteur : arenmegu
Date : 09/09/2024
Version : 1.0
================================================================================

Description :
    Ce programme est une simulation d'une stratégie pour gagner à la roulette.
    Les utilisateurs peuvent simuler grâce à ce programme une roulette et observer des estimations concernant cette stratégie

Outils utilisés :
    - Python : Pour le développement du programme
    - MatPlotLib : Pour la mise en place de la partie graphique
    - Random : Pour générer un nombre aléatoire (via une façon déterministe)
    - System : Pour mettre fin au programme
    
Fonctionnalités :
    - Simuler la roulette
    - Affichage Textuel et Graphique d'une simulation
    - Gestion des entrées
    
Notes :
    - Ce projet est dans sa première version, n'hésitez pas à l'améliorer
    - Le code est structuré selon les conventions de base de python
    - On utilise le CamelCase pour le nom des fonctions/méthodes et le snake_case pour le nom des variables
    - L'intégralité du projet sera rédigé en français
    
Licence :
    Ce projet est sous licence MIT. Vous êtes libre de l'utiliser, de le modifier et
    de le distribuer à condition de conserver les mentions de l'auteur original.

================================================================================
"""

#-------------------------------------------------------------------------
# Importations des modules
#-------------------------------------------------------------------------

from random import randint 
import sys
import matplotlib.pyplot as plt

# -------------------------------------------------------------------------
# Initialisation des variables 
# nb_victoires -> compteur pour le nombre de victoires
# nb_défaites -> compteur pour le nombre de défaites
# ligne_forte -> compteur pour le nombre de fois où le gagnant est un nombre situé au milieu
# tirage_nombre -> tableau de 36 cases qui compte le nombre de fois que chaque numéro tombe
# wallet -> jetons disponible à utiliser
# tab_x -> pour modélisation du graphique : tableau contenant le numéro d'essai
# tab_y -> pour modélisation du graphique : tableau contenant l'état du wallet pour chaque essai
# -------------------------------------------------------------------------

nb_victoires = 0
nb_défaites = 0
ligne_forte = 0
tirage_nombre = [0] * 37

wallet = 1000
tab_x = [0] * 10000
tab_y = [0] * 10000

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
    Fonction qui va simuler un tour de roulette en utilisant la stratégie initiale
    """
    global ligne_forte, nb_défaites,nb_victoires,wallet
    nombre_tiré = roulette()
    wallet -= 24
    tirage_nombre[nombre_tiré] += 1
    if nombre_tiré in [2,8,11,14,17,20,23,26,29]:
        ligne_forte +=1
    if nombre_tiré in [3,6,9,5,10,16,22,25,32,33,34,35,36]:
        nb_défaites += 1
    else :
        nb_victoires += 1
        wallet += 36

def simulationRouletteTexuelle():
    """
    Fonction qui va simuler 10 M d'essais
    """
    for i in range(10000000):
            tirage()

def simulationRouletteGraphique():
    """
    Fonction qui va simuler 10k essais
    """
    for i in range(10000):
            tirage()
            tab_x[i] = i+1
            tab_y[i] = wallet


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
    Toute la partie construction/affichage du graphique
    """
    plt.scatter(tab_x, tab_y, color="blue", label="Points")
    plt.plot(tab_x, tab_y, color="green", linestyle="-", label="Ligne")
    plt.title("Simulation sur 10 000 tirages")
    plt.xlabel("Numéro de l'essai")
    plt.ylabel("Argent possédé")
    plt.legend()
    plt.show()

def lancementRouletteTextuelle():
    """
    Fonction appelée si on souhaite avoir une simulation textuelle
    """
    print("\033cSimulation en cours...")
    simulationRouletteTexuelle()
    print("\033c")
    affichageResultatsTextuel()

def lancementRouletteGraphique():
    """
    Fonction appelée si on souhaite avoir une simulation graphique
    """
    print("\033cSimulation en cours...")
    simulationRouletteGraphique()
    print("\033c")
    affichageResultatsGraphique()

def réinitialisation():
    """
    Fonction de réinitialisation, on réassigne les valeurs d'origine du programmme après un potentiel travail réalisé dessus
    """
    global nb_défaites, nb_victoires, ligne_forte, tirage_nombre, tab_x, tab_y, wallet
    nb_victoires = 0
    nb_défaites = 0
    ligne_forte = 0
    tab_x = [0] * 10000
    tab_y = [0] * 10000
    tirage_nombre = [0] * 37
    wallet = 1000

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
    réinitialisation()

    # On attend confirmation puis on lance la simulation graphique
    if (choix[0] and choix[1]):
        #Créer un SAS
        print("Voulez vous démarrer la simulation graphique ?\n1 - Oui\n2 - Non")

        while (True):
            entree = int(input("\n>> "))
            match entree :
                case 1 :
                    lancementRouletteGraphique()
                    sys.exit(0)
                case 2 :
                    sys.exit(0)
                case _ :
                    print("Entrée non reconnue")

    # Affichage Graphique
    if (choix[1]):
        lancementRouletteGraphique()
    