def Signe(a, b):
    if a * b < 0 :
        print("A et B ont même signe")
    elif a * b > 0 :
        print("A et B ont deux signe différents")
    else:
        print("l'un des deux valeurs égale a zéro")


def Max(a, b):
    max = a
    if a < b   :
        max = b
    elif a > b :
        max = a
    return max


def Min(a, b):
    min = a
    if a > b   :
        min = b
    elif a < b :
        min = a
    else :
        print("les deux valeurs sont égaux")
    return min