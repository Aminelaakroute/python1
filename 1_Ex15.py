print("Un programme affiche un triangle")

H = int(input("Veuillez Entrer l'hauteur de triangle : "))
for i in range(H):
    for j in range(H):
        if j <= i:
            print("*  ",end="")
    print("")
