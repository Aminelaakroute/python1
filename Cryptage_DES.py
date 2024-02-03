from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from base64 import b64encode, b64decode
import os

def encrypt_des(message, key):
    key = key.ljust(24)[:24]  # Triple DES utilise des clés de 24 octets (192 bits)
    backend = default_backend()
    iv = os.urandom(8)  # IV (vecteur d'initialisation) aléatoire de 8 octets
    cipher = Cipher(algorithms.TripleDES(key.encode()), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()

    padder = padding.PKCS7(algorithms.TripleDES.block_size).padder()
    padded_data = padder.update(message.encode()) + padder.finalize()

    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return b64encode(iv + ciphertext).decode()

def decrypt_des(ciphertext, key):
    key = key.ljust(24)[:24]
    backend = default_backend()
    data = b64decode(ciphertext)
    iv = data[:8]  # Récupère l'IV à partir des premiers 8 octets
    ciphertext = data[8:]  # Récupère le reste comme texte chiffré

    cipher = Cipher(algorithms.TripleDES(key.encode()), modes.CBC(iv), backend=backend)
    decryptor = cipher.decryptor()

    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()

    unpadder = padding.PKCS7(algorithms.TripleDES.block_size).unpadder()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()

    return unpadded_data.decode()

# Test des fonctions
texte = "Hello World!"
cle_des = "my_key_64"

# Chiffrement DES
ciphertext_des = encrypt_des(texte, cle_des)
texte_decrypte_des = decrypt_des(ciphertext_des, cle_des)

# Affichage des résultats
print("Texte original:", texte)

print("\nChiffrement DES")
print("Texte chiffré DES:", ciphertext_des)
print("Texte déchiffré DES:", texte_decrypte_des)
