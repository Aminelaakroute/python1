a = [[0,0,0,0,0],[1,1,1,1,1],[2,2,2,2,2],[3,3,3,3,3],[4,4,4,4,4]]



Matrice = []
for i in range(5):
    ligne = []
    for j in range(5):
        ligne.append(i)

    Matrice.append(ligne)

for j in Matrice :
    print(j)
print("____________________________________________")

for ligne in a:
    for l in ligne:
        print(l, end="\t")
    print()
print("____________________________________________")
for k in range(len(a)):
    for m in range(len(a[k])):
        print(a[k][m],end="\t")
    print()