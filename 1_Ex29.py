from faker import Faker
fake = Faker()

Note = [10, 12, 14.5, 6, 2.5, 8, 6.5, 12, 14.5, 10.5, 9.5, 14, 12, 15, 13.5, 19, 20, 10, 19, 18]
liste_nom_aleatoire = [fake.name() for _ in range(20)]
#i = 1
#for Nt in Note :
#   print("la note de l'etudiant num",i,"est :",Nt)
#   i +=1

#for i in range(len(Note)):
#    print("la note de l'etudiant num",i+1,"est :",Note[i])


#for i , N in enumerate(Note , start= 1):
#    print("la note de l'etudiant num",i,"est :",N)
print(liste_nom_aleatoire)

for nom , note in zip(liste_nom_aleatoire , Note):
       print("la note de",nom,"est :",note)