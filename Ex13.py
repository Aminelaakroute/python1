print("Un programme qui affiche le Tableau de multiplication ")

# Afficher les en-têtes de colonnes
print(" x |", end="")
for i in range(1, 10 + 1):
    print("{:4d}".format(i), end="")
print("\n---+" + "----" * (10 - 1+ 1))
# Générer la table de multiplication
for i in range(1, 10 + 1):
    print("{:2d} |".format(i), end="")
    for j in range(1, 10 + 1):
        resultat = i * j
        print("{:4d}".format(resultat), end="")
    print()  # Passer à la ligne suivante


