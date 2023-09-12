analyse     = list((10, 12, 14.5, 6, 2.5))
algebre     = list((8, 6.5, 12, 14.5, 10.5))
probabilite = list((9.5, 14, 12, 15, 13.5))
statistique = list((19, 20, 10, 19, 18))
NombreEtudiant = len(analyse)

note = analyse + algebre + probabilite + statistique
nombreNote = len(note)
print(nombreNote)
print("la note maximale parmis tous les notes est :",max(note))
print("la note minimale parmis tous les notes est :",min(note))
print("la somme de tous les notes est :",sum(note))
print("la moyenne des notes est :",(sum(note)/nombreNote))

print("Le nombre des etudiant est :",NombreEtudiant)

print("la somme de toutes les notes des Etudiants dans analyse:",sum(analyse))
print("la moyenne des notes des Etudiants dans analyse:",sum(analyse)/NombreEtudiant)
print("la note maximale dans l'analyse est :",max(analyse))
print("la note minimale dans l'analyse est :",min(analyse))

print("la somme de toutes les notes des Etudiants dans algebre:",sum(algebre))
print("la somme des notes des Etudiants dans algebre:",sum(algebre)/NombreEtudiant)
print("la note maximale dans l'algebre est :",max(algebre))
print("la note minimale dans l'algebre est :",min(algebre))

print("la somme de toutes les notes des Etudiants dans probabilite:",sum(probabilite))
print("la somme des notes des Etudiants dans probabilite:",sum(probabilite)/NombreEtudiant)
print("la note maximale dans probabilite est :",max(probabilite))
print("la note minimale dans probabilite est :",min(probabilite))

print("la somme de toutes les notes des Etudiants dans statistique:",sum(statistique))
print("la somme des notes des Etudiants dans statistique:",sum(statistique)/NombreEtudiant)
print("la note maximale dans statistique est :",max(statistique))
print("la note minimale dans statistique est :",min(statistique))
print(note)

pays = ['MAROC', 'SPAIN', 'FRANCE', 'ALGERIE', 'MALI', 'EGYPT']
for nom in pays :
    print(nom)