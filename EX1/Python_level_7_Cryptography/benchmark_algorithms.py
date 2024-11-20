import matplotlib.pyplot as plt

# Données d'exemple pour chaque métrique (à ajuster selon les benchmarks réels)
algorithms = ['KATAN', 'PICCOLO', 'AES', 'SIMON', 'SPARX', 'SPECK']

# Temps de chiffrement en millisecondes (ms) - données d'exemple
encryption_times = [150, 120, 250, 100, 200, 180]  

# Consommation de mémoire en kilooctets (kB) - données d'exemple
memory_usage = [2.1, 1.8, 3.5, 1.5, 2.0, 1.7]  

# Tailles des clés en bits (à adapter si besoin) - données d'exemple
key_sizes = [80, 80, 128, 128, 128, 128]

# Fonction pour afficher un graphique en barres
def plot_bar_chart(values, title, ylabel, xlabel='Algorithmes', color_list=None):
    plt.figure(figsize=(8, 6))
    plt.bar(algorithms, values, color=color_list if color_list else ['blue', 'green', 'red', 'orange', 'purple', 'cyan'])
    plt.title(title, fontsize=14)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.show()

# Affichage des graphiques

# 1. Temps de chiffrement
plot_bar_chart(encryption_times, 'Temps de Chiffrement par Algorithme (en ms)', 'Temps (ms)')

# 2. Consommation de mémoire
plot_bar_chart(memory_usage, 'Consommation de Mémoire par Algorithme (en kB)', 'Mémoire (kB)')

# 3. Taille des clés
plot_bar_chart(key_sizes, 'Taille des Clés par Algorithme (en bits)', 'Taille de Clé (bits)')
