def affichage():
    print("Hello World !!!")
    print("Programme contient deux fonction :")
    print("1 - Fonction d'affichage : pas de retour et pas d'arguments")
    print("2 - Fonction de la somme : Avec retour et d'arguments")

def somme(a, b):  #fonction avec retour et avec arguments
    s = a + b
    return s

affichage()

A = int(input("Veuillez entrer la valeur de A :"))
B = int(input("Veuillez entrer la valeur de B :"))

print("A + B =",somme(A, B))