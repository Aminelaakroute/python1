print("Programme de calcule d'un enssemble d'entier")

Reponse = input("Demmarer le programme (Oui/Non) :").strip().lower()

A = Reponse == "oui"  # Convertit la réponse en booléen (True si la réponse est "oui", False sinon)
i = 0
S = 0
while A :
    B = int(input("Veuillez entrer le nombre N{}:".format(i+1)))
    i += 1
    if B < 0:
        continue
    else :
        S += B
        if i >= 8:
         print("La somme des nombres entier positif est :", S)
         break


