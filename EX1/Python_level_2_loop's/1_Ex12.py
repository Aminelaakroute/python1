print("Un programme qui permet de calculer la somme des 20 premiers entier positifs")
S = 0
N = int(input("Veuillez entrer un nombre entier positif : "))
for i in range(1,N+1):
    S = S + i
print("La somme de 1 jusqu'a ",N," est :",S)