# Fonction de décalage d'un caractère dans l'alphabet
def decalage(caract, dis):
    if 65 <= ord(caract) <= 90:
        return chr(((ord(caract)-65)+dis) % 26 + 65)
    if 97 <= ord(caract) <= 122:
        return chr(((ord(caract)-97)+dis) % 26 + 97)
    return chr(ord(caract)+dis)

# Fonction de cryptage César
def crypterConstant(texte, dec):
    renvoi = ""
    for i in texte:
        if i.isalpha():
            renvoi += decalage(i, dec)
        else:
            renvoi += i
    return renvoi

# Fonction de décryptage César
def decrypterConstant(texte, dec):
    return crypterConstant(texte, 26-dec)

# Fonction de cryptage Vigenère
def crypterCle(texte, cle):
    renvoi = ""
    c = 0
    for i in range(len(texte)):
        if texte[i].isalpha():
            temp = ord(cle[(i-c) % len(cle)])
            temp -= 65 if temp <= 90 else 97
            renvoi += decalage(texte[i], temp)
        else:
            renvoi += texte[i]
            c += 1
    return renvoi

# Fonction de décryptage Vigenère
def decrypterCle(texte, cle):
    renvoi = ""
    c = 0
    for i in range(len(texte)):
        if texte[i].isalpha():
            temp = ord(cle[(i-c) % len(cle)])
            temp -= 65 if temp <= 90 else 97
            renvoi += decalage(texte[i], 26-temp)
        else:
            renvoi += texte[i]
            c += 1
    return renvoi

# Exemples d'utilisation
texte = "Hello World!"
cle_vigenere = "KEY"
decalage_cesar = 3

# Chiffrement César
texte_crypte_cesar = crypterConstant(texte, decalage_cesar)
texte_decrypte_cesar = decrypterConstant(texte_crypte_cesar, decalage_cesar)

# Chiffrement Vigenère
texte_crypte_vigenere = crypterCle(texte, cle_vigenere)
texte_decrypte_vigenere = decrypterCle(texte_crypte_vigenere, cle_vigenere)

# Affichage des résultats
print("Texte original:", texte)
print("Chiffrement César:", texte_crypte_cesar)
print("Déchiffrement César:", texte_decrypte_cesar)
print("Chiffrement Vigenère:", texte_crypte_vigenere)
print("Déchiffrement Vigenère:", texte_decrypte_vigenere)
