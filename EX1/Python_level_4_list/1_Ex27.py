pays = ['MAROC', 'SPAIN', 'FRANCE', 'ALGERIE', 'MALI', 'EGYPT']

P1  = input("Veuillez saisi le nom de premier pays :").upper()
P2  = input("Veuillez saisi le nom de deuxieme pays :").upper()

if P1 and P2 in pays :
    print("Les deux pays existe")
    i = pays.index(P1)
    j = pays.index(P2)
    print("L'index de",P1,"est :",i)
    print("L'index de",P2,"est :",j)
    pays[i], pays[j] = pays[j], pays[i]
    print(pays)
else :
    print("l'un des deux pays n'est pas existe ")