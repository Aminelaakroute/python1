import random

# Listes de prénoms et de noms de famille
prenoms = ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Henry']
noms_de_famille = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson']

# Fonction pour générer un nom aléatoire
def generer_nom_aleatoire():
    prenom = random.choice(prenoms)
    nom_de_famille = random.choice(noms_de_famille)
    nom_complet = f"{prenom}{nom_de_famille}"
    return nom_complet

# Exemple d'utilisation
for _ in range(15):
    nom_aleatoire = generer_nom_aleatoire()
    print(nom_aleatoire)
