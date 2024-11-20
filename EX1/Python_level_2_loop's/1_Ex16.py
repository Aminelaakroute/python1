A = int(input("Veuillez saisir un nombre :"))
while A < 0 or A >10 :
   A = int(input("Veuillez saisir un nombre compris entre 1 et 10 :"))
i = 0
while i <= 10 :
   M = A * i
   print(A, "X", i,"=",M)
   i += 1