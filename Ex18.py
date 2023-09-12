A = int(input("Veuillez saisi un nombre entier positif superieur a 1 :"))

while A > 0 or A < 0:
    S = 0
    i = 0
    if A > 0 :
       while i <= A :
          S = S + i
          i = i + 1
       print("La somme des entier positif est : ",S)
       A = int(input("Veuillez saisi un nombre entier positif superieur a 1 :"))
    elif A < 0 :
      A = int(input("Veuillez saisi un nombre entier positif superieur a 1 A lbashar :"))
 