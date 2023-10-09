print("________________________Ajout()___________________________")
liste1 = ['amine','amine', 'mohammed', 'ilias', 'mouad', 'ayman', 'redouane', 'anass']
liste2 = list(range(0, 10, 2))

liste1.append('younes')  #ajout d'un element a la fin de la liste
print(liste1)
liste1.insert(4,'ilyas') # insert un element a un index specifié dans une liste ( au debut )
print(liste1)
print(liste2)
liste1.extend(liste2) #cette methode permet d'ajouter les elements d'une sequence (liste,tuple,...)
print(liste1)
liste2.extend('AMINE')  # la méthode extend considère les String comme une liste
print(liste2)
print("________________________Suppression()___________________________")
liste1.remove('amine') #cette methode supprime la premiere occurence de l'element specifié si elle existe sinon erreur
print(liste1)
liste3 = ['LAAKROUTE', 'AMINE', '22', '22-05-2001','AMINE_LAAKROUTE']
print(liste3)
Nom_Prenom = liste3.pop()            #cette methode permet de supprimer un element situe a un index indiqué
print("Nom et Prenom :",Nom_Prenom)  #et de retour comme valeur de retour , si aucun index n'est spécifié la methode
                                     #supprime et renvoie le dernier element de la liste
print(liste3)
Nom = liste3.pop(0)
print("Nom :",Nom)

print(liste3)
Prenom = liste3.pop(0)
print("Prenom :",Prenom)

print(liste3)
Age = liste3.pop(0)
print("Age :",Age)

print(liste3)
Date_de_Naissance = liste3.pop(0)
print("Date de Naissance :",Date_de_Naissance)

print("Maintenant la liste est vide :",liste3)

liste4 = ['LAAKROUTE', 'AMINE', '22', '22-05-2001','AMINE_LAAKROUTE']
print(liste4)
liste4.clear()   # cette methode permet de supprimer tous le elements de la liste
print(liste4)

liste5 = ['LAAKROUTE', 'AMINE', '22', '22-05-2001','AMINE_LAAKROUTE']
del liste5 [3]                   #cette methode permet de supprimmer un element situé par un index
print(liste5)
liste6 = list(range(1,10))
print(liste6)
del liste6[1:6]               #cette methode permet de supprimmer une plage situé par un index
print(liste6)
print("________________________Opérations()___________________________")
Vr = list([2,1,1,1,1,1,1,2,3,4,5,6,7,8,9,0,9,8,7,6,5,4,3,2,3,4,5,6,5,4,3,2,1,2,3,4,5,6,7,6,5,4,3,2,3,4,5,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,4,8,7,8,8,9,0,9,8,9,8,7,6,5,4,4,6,7,8,9,0,8,0,7,6])
taile = len(Vr)              # cette fonction permet de renvoie le nombre d'elements de la liste
print("Vr =",Vr)
print("le nombre d'elements dans la liste Vr est :",taile)
somme = sum(Vr)              #cette fonction permet de renvoie la somme de tous les elements de la liste !!! val.num
print("la somme des elements de la liste Vr est :",somme)
print("la moyenne de la liste vr est :",somme/taile)

liste = [5.2, -2, -21, 6, 10, 15, 60, 1.2, 44, -9]


#Q1
Max = max(liste)
print("le maximum est :",Max)
#Q2
l1 = liste[:5]
print(l1)
print(max(l1))
#Q3
Min = min(liste)
print("le minimum est :",Min)
#Q4
l2 = liste[-5:]
print(l2)
print(min(l2))

#Ex
l3 = list(('PYTHON'))
print(l3)
print(max(l3))
print(min(l3))

N1=Vr.count(1) # cette methode permet déterminer combien de fois l'element specifié apparait dans la liste
print(N1)

print(liste)
liste.reverse()  # cette methode reverse l'ordre des elements dans la liste
print(liste)

import random
liste_nombre_aleatoire = [random.randint(1, 100) for _ in range(10)]  # sort methode de tri
print("liste aleatoire :", liste_nombre_aleatoire)
liste_nombre_aleatoire.sort()
print("liste aleatoire triée croissante  :",liste_nombre_aleatoire)
liste_nombre_aleatoire.sort(reverse=True)
print("liste aleatoire triée decroissante :",liste_nombre_aleatoire)

listo = ['amine','amine', 'mohammed', 'ilias', 'mouad', 'ayman', 'redouane', 'anass']
print(listo)
listo.sort(key=str.upper, reverse=True)
print(listo)
listo1 = sorted(listo,key=str.upper, reverse=False)
print(listo)
print(listo1)

amine = list(random.randint(-12, 12) for _ in range(25))
print(amine)
ilyass = sorted(amine, reverse=True)
print("Decroissante :",ilyass)
yassine = sorted(amine, reverse=False)
print("Croissante   :",yassine)