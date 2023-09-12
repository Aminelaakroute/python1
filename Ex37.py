N=list(())
for i in range(2):
    ligne = list(())
    for j in range(3):
        print("N[",i+1,"][",j+1,"]=", end=" ")
        ligne.append(float(input()))
    N.append(ligne)
print(N)


S = 0
for ligne in N: 
    S = S + sum(ligne)
M = S /(len(N)*len(N[0]))


print("la somme des notes est :",S)
print("la moyenne des notes est :",format(M,'.2f'))