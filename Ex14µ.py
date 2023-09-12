print("Un programme qui affiche un rectangle d'etoile")

L = int(input("Veuillez Entrer le nombre de lignes : "))
C = int(input("Veulliez entrer le nombre de collones : "))
for j in range(L):
   for i in range(C):
      print("*", end="  ")
   print("")


