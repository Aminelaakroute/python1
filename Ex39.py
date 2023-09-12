#Un nombre heureux est un nombre entier qui, lorsqu’on ajoute les carrés de chacun de ses chiffres, puis les carrés des chiffres de ce résultat et ainsi de suite jusqu'à l’obtention d’un nombre à un seul chiffre égal à 1 (un).
#
#Exemple :
#
#N=7 est heureux, puisque :
#
# 72=49
# 42+92=97
# 92+72=130
# 12+32+02=10
# 12+02=1
#On est arrivé à un nombre d’un seul chiffre qui est égal à 1, donc N=7 est heureux
#
#Travail demandé :
#Ecrire une fonction heureux(nb) qui permet de déterminer si un nombre entier nb est heureux ou non.

def heureux(nb):
    etat = False     # si le nomnre egale 1 etat prend true
    nombre = str(nb) # changement de numéro en chaîne
    limite = False   # le role de limite est le stop de programme si le nombre inférieur a 10
    while limite == False:
        s = 0
        for i in nombre:
            s += int(i) ** 2
        nombre = str(s)
        if nombre == '1':
            etat = True
            break
        if int(nombre) < 10:  # si le nombre<10 donc limite=True
            limite = True
            print(nombre)
    return etat


print(heureux(7))

