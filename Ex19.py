print("Programme de calcule d'un enssemble d'entier")

Reponse = input("Demmarer le programme (Oui/Non) :").strip().lower()

A = Reponse == "oui"
i = 1
S = 0
while A :
    B = int(input("Veuillez entrer le nombre N{}:".format(i)))
    i += 1
    if B < 0 or i >8 :
      print("La somme des nombres entier positif est :", S)
      break
    S += B
