"""
================================================================================
Projet : Simulation d'une stratégie de roulette
Auteur : arenmegu
Date : 09/09/2024
Version : 0.2
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

Comment utiliser le programme :
    1. Merci de consulter le README
    
Notes :
    - Ce projet est encore en développement et non fini.
    - Le code est structuré selon les conventions de base de python
    
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
    Fonction qui va simuler un tour de roulette
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

def simulation_roulette():
    """
    Fonction qui va simuler 10 000 000 tours de roulette
    """
    for i in range(10000000):
            tirage()

def information_numéro(i):
    """
    Afficher les informations relatives au numéro donné en paramètre à savoir le numéro, le nombre de fois qu'il a été tiré et la probabilité de tomber dessus

    Paramètre
    -------
    int
        Le numéro dont il faut afficher les informations
    """
    print("Numéro ",i," - Nombre de tirages : ", tirage_nombre[i], " - Pourcentage de chance : ", tirage_nombre[i]/(nb_victoires+nb_défaites) * 100, " %")

def affichage_information_numéro():
    """
    Affiche les informations relatives à chaque numéro présent sur le plateau (donc les entiers naturels présent dans [0,36])
    """
    for i in range(37):
            information_numéro(i)


# -------------------------------------------------------------------------
# Partie affichage
# -------------------------------------------------------------------------

if __name__ == '__main__':

    # Menu principal avec 4 entrées disponibles
    while(True):
        print("\033cMerci de sélectionner parmi les propositions :\n1 - Visualisation Textuelle\n2 - Visualisation Graphique\n3 - Visualisation Texuelle et Graphique\n4 - Quitter")
        entree = int(input())
        if entree == 4:
            print("Sortie en cours...")
            sys.exit(0)
        if not(entree == 1 or entree == 2 or entree == 3):
            print("Erreur, entrée non reconnue")
        else :
            break

    # Génération de toute la roulette
    print("\033cSimulation en cours...")
    simulation_roulette()
    print("\033c")

    # Affichage Textuel
    if (entree == 1 or entree == 3):
        print("Nombre de Victoires : ", nb_victoires)
        print("Nombre de Défaites : ", nb_défaites)

        print("Pourcentage de chance de gagner : ", (nb_victoires/(nb_victoires + nb_défaites)) * 100, " %")
        print("Pourcentage de chance de perdre : ", (nb_défaites/(nb_victoires + nb_défaites)) * 100, " %")

        print("Pourcentage de chance de tomber sur la ligne forte : ", (ligne_forte/(nb_victoires + nb_défaites)) * 100, " %")

        print("Voulez vous afficher le nombre de tirage et le pourcentage de chance de tomber sur un numéro pour chaque numéro ?")
        if (input() == "oui"):
            affichage_information_numéro()
            
    # Affichage Graphique
    if entree == 2 or entree == 3:
        # TODO
        pass