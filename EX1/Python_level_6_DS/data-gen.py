import random
import string

# Nombre de lignes à générer
num_lines = 100857

# Générer des mots aléatoires
words = [''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 5))) for _ in range(num_lines)]

# Générer des lignes aléatoires en concaténant les mots
lines = [' '.join(random.choices(words, k=random.randint(1, 10))) for _ in range(num_lines)]

# Écrire les lignes dans un fichier
with open('input.txt', 'w') as f:
    f.write('\n'.join(lines))
