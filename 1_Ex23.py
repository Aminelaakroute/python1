def signe(a, b):  #fonction avec arguments et pas de retour
    if a * b < 0 :
        print("A et B ne sont pas de meme signe")
    elif a * b > 0 :
        print("A et B sont de meme signe")
    else :
        print("l'un des deux nombre est egale a zéro !!")


def Max(a, b):    #fonction avec arguments et retour
    max = a
    if b > max :
        max = b
    else :
        max = a
    #print("Le Maximum et :", max)
    return max

def Min(a, b):    #fonction avec arguments et retour
    min = a
    if b < min :
        min = b
    else :
        min = a
    #print("Le Minimum et :", min)
    return min


A = int(input("Veuillez entrer la valeur de A :"))
B = int(input("Veuillez entrer la valeur de B :"))

signe(A, B)
#Max(A, B)
Maximum = Max(A, B)
print("Le maximum est",Maximum)
#Min(A, B)
Minimum = Min(A, B)
print("Le minimum est",Minimum)
