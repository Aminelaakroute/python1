from faker import Faker
fake = Faker()
A = int(input("Veuillez entrer le nombre d'etudiants :"))
Nom = [fake.name() for _ in range(A)]
Liste = list(())
i=1
while i <= A :
    K = float(input("Entrer la note num {}:".format(i)))
    Liste.append(K)
    i +=1
print(Liste)
for name , note in zip(Nom ,Liste):
    print("la note de",name,"est :",note)