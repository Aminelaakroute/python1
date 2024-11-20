# Définir la plage de nombres pour la table de multiplication
debut = 1
fin = 10

# En-tête de la table
print("Table de multiplication de {} à {} :\n".format(debut, fin))

# Afficher les en-têtes de colonnes
print(" x |", end="")
for i in range(debut, fin + 1):
    print("{:4d}".format(i), end="")
print("\n---+" + "----" * (fin - debut + 1))

# Générer la table de multiplication
for i in range(debut, fin + 1):
    print("{:2d} |".format(i), end="")
    for j in range(debut, fin + 1):
        resultat = i * j
        print("{:4d}".format(resultat), end="")
    print()  # Passer à la ligne suivante

