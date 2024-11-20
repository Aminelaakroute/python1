def salutation():
    print("_______________________Fonction 1_________________________")
    return "Welcome to python"


def affichage():
    print("_______________________Fonction 2_________________________")
    print("Hello World !!!")
    print("Programme contient trois fonction :")
    print("1 - Fonction d'affichage : avec retour et pas d'arguments")
    print("2 - Fonction d'affichage : pas de retour et pas d'arguments")
    print("3 - Fonction de la somme : avec arguments et pas de retour")

def somme(a, b): #Fonction avec arguments et pas de retour
    print("_______________________Fonction 3_________________________")
    S = a + b
    print("A + B =",S)




message = salutation()
print(message)
affichage()
print("__________________________________________________________")
A = int(input("Veuillez entrer la valeur de A :"))
B = int(input("Veuillez entrer la valeur de B :"))
somme(A, B)