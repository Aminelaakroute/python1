from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from base64 import b64encode, b64decode
import os

def encrypt_aes(message, key):
    key = key.ljust(32)[:32]  # Assure une longueur de clé de 32 caractères (256 bits)
    backend = default_backend()
    iv = os.urandom(16)  # IV (vecteur d'initialisation) aléatoire de 16 octets
    cipher = Cipher(algorithms.AES(key.encode()), modes.CFB(iv), backend=backend)
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(message.encode()) + encryptor.finalize()
    return b64encode(iv + ciphertext).decode()

def decrypt_aes(ciphertext, key):
    key = key.ljust(32)[:32]
    backend = default_backend()
    data = b64decode(ciphertext)
    iv = data[:16]  # Récupère l'IV à partir des premiers 16 octets
    ciphertext = data[16:]  # Récupère le reste comme texte chiffré
    cipher = Cipher(algorithms.AES(key.encode()), modes.CFB(iv), backend=backend)
    decryptor = cipher.decryptor()
    decrypted_message = decryptor.update(ciphertext) + decryptor.finalize()
    return decrypted_message.decode()

# Exemple d'utilisation AES
message_original = "Hello, AES Encryption!"
cle_aes = "my_secret_key12345"  # Clé de longueur 16, 24 ou 32 caractères
ciphertext_aes = encrypt_aes(message_original, cle_aes)
message_decrypte_aes = decrypt_aes(ciphertext_aes, cle_aes)

print("Message original:", message_original)
print("Message chiffré (AES):", ciphertext_aes)
print("Message déchiffré (AES):", message_decrypte_aes)
