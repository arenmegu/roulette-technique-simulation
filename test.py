import matplotlib.pyplot as plt
import random

# Abscisses (x) : 5 points fixés
x = [1, 2, 3, 4, 5]

# Ordonnées (y) : générées aléatoirement
y = [random.randint(-10, 10) for _ in range(5)]

# Créer le graphique
plt.scatter(x, y, color='blue', label='Points')  # Tracer les points
plt.plot(x, y, color='green', linestyle='-', label='Ligne')  # Tracer la courbe

# Ajouter des titres et des labels
plt.title('Graphique avec points tirés au hasard et courbe')
plt.xlabel('Abscisses')
plt.ylabel('Ordonnées')

# Ajouter une légende
plt.legend()

# Afficher le graphique
plt.show()


"""-----------------------------------------------------------------------"""
"""
def construction_et_affichage_graphique():
    
    #Utilisation de la technique si on suppose qu'on a un wallet infini et qu'on commence à 72 jetons soit 3 coups avant de perdre
    
    x = list(range(1,10001))
    y = 72

    plt.scatter(x, y, color='blue', label='Points')  # Tracer les points
    plt.plot(x, y, color='green', linestyle='-', label='Ligne')  # Tracer la courbe
    plt.title('Visualisation Gain et Perte')
    plt.legend()
    plt.xlabel('Tirage')
    plt.ylabel('Wallet')
    plt.show()
    pass
"""