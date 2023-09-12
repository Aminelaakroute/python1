A = int(input("Veuillez entrer un nombre :"))
Liste = list(())
i = 1
while i <= 5 :
    B = int(input("Veuillez entrer num {} :".format(i)))
    Liste.append(B)
    i += 1

print(Liste)
def maxi():
        max = Liste[0]
        for j in range(len(Liste)) :

            if Liste[0] < Liste[j]:
                 max =Liste[j]
        return max

def Min():
    min = Liste[0]
    for i in range(len(Liste)):
        if min > Liste[i]:
            min = Liste[i]
    return min


print("Le maximum est :",maxi())
print("le minimum est :",Min())
if A in Liste :
    print("Le nombre que vous avez saisi est existe ")
else :
    print("Le nombre que vous avez saisi est n'existe pas")