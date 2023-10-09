N=list(())
for i in range(2):
    ligne = list(())
    for j in range(3):
        print("N[",i+1,"][",j+1,"]=", end=" ")
        ligne.append(float(input()))
    N.append(ligne)
print(N)

n = int(input("Veuillez saisir la valeur de n :"))
Occ = 0
for ligne in N:
    Occ = Occ + ligne.count(n)



print("le nombre d'occurrence de",n,"dans N est :",Occ)