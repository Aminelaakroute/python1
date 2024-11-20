A = int(input("Veuillez entrer un nombre antier positif :"))
L1 = list(range(1,A+1))

while A < 0 :
    A = int(input("Veuillez entrer un nombre antier positif :"))

L1 = list(range(1,A+1))
print("liste des nombre de 1 jusqu'a",A,"est         : ",L1)
L1 = list(range(0,A+1,2))
print("liste des nombre paire de 1 jusqu'a",A,"est   : ",L1)
L1 = list(range(1,A+1,2))
print("liste des nombre impaire de 1 jusqu'a",A,"est : ",L1)