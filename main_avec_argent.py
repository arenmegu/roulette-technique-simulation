from random import randint 

# -------------------------------------------------------------------------
# Initialisation des variables : nombre de victoires/défaites, tableau pour
# stocker le nombre de fois qu'un numéro tombe ainsi que le nombre de fois
# que la "ligne forte" est tirée
# -------------------------------------------------------------------------

nb_victoires = 0
nb_défaites = 0
ligne_forte = 0
wallet = 72
tirage_nombre = [0] * 37

# -------------------------------------------------------------------------
# Générer un nombre aléatoire dans l'intervalle [0;36]
# -------------------------------------------------------------------------

def roulette():
    return randint(0, 36)

# -------------------------------------------------------------------------
# Afficher les informations relatives au numéro donné en paramètre à savoir
# le numéro, le nombre de fois qu'il a été tiré et la probabilité de tomber
# dessus
# -------------------------------------------------------------------------

def information_numéro(i):
    print("Numéro ",i," - Nombre de tirages : ", tirage_nombre[i], " - Pourcentage de chance : ", tirage_nombre[i]/(nb_victoires+nb_défaites) * 100, " %")


# -------------------------------------------------------------------------
# On réalise le tirage sur un nombre conséquent d'essais, on assigne à la valeur correspondante dans le tableau puis on assigne en fonction de la technique
# -------------------------------------------------------------------------

for i in range(10000000):
    nombre_tiré = roulette()
    tirage_nombre[nombre_tiré] += 1
    if nombre_tiré in [2,8,11,14,17,20,23,26,29]:
        ligne_forte +=1
    if nombre_tiré in [3, 6, 9, 5, 10, 16, 22, 25, 32, 33, 34, 35, 36]:
        nb_défaites += 1
        wallet-=24
    else :
        nb_victoires += 1
        wallet+=12
    if wallet <=23:
        print("Jeu terminé, wallet inférieur à 24 : ", wallet)
        break
    

# -------------------------------------------------------------------------
# Partie affichage
# -------------------------------------------------------------------------

print("Nombre de Victoires : ", nb_victoires)
print("Nombre de Défaites : ", nb_défaites)

print("Pourcentage de chance de gagner : ", (nb_victoires/(nb_victoires + nb_défaites)) * 100, " %")
print("Pourcentage de chance de perdre : ", (nb_défaites/(nb_victoires + nb_défaites)) * 100, " %")

print("Pourcentage de chance de tomber sur la ligne forte : ", (ligne_forte/(nb_victoires + nb_défaites)) * 100, " %")

print("Voulez vous afficher le nombre de tirage et le pourcentage de chance de tomber sur un numéro pour chaque numéro ?")
if (input() == "oui"):
    for i in range(37):
        information_numéro(i);