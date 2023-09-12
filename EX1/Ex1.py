import math
print("Un programme avec les modules standards de python")
print("__________________________________________________")
A = int (input("Entrer un nombre positif :"))
Facto = math.factorial(A)
print("le factoriel de",A ,"est :",Facto)
print("__________________________________________________")
import random
print("un programme affiche aleatoirement un nombre impaire entre deux valeurs")
Nombre_aleatoire = random.randrange(1, 101, 2)

print("Le nombre aleatoire impaire est :",Nombre_aleatoire)

print("__________________________________________________")
import statistics
Md = statistics.mode([2,1,1,1,1,1,1,2,3,4,5,6,7,8,9,0,9,8,7,6,5,4,3,2,3,4,5,6,5,4,3,2,1,2,3,4,5,6,7,6,5,4,3,2,3,4,5,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,4,8,7,8,8,9,0,9,8,9,8,7,6,5,4,4,6,7,8,9,0,8,0,7,6])
Vr = statistics.variance([2,1,1,1,1,1,1,2,3,4,5,6,7,8,9,0,9,8,7,6,5,4,3,2,3,4,5,6,5,4,3,2,1,2,3,4,5,6,7,6,5,4,3,2,3,4,5,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,4,8,7,8,8,9,0,9,8,9,8,7,6,5,4,4,6,7,8,9,0,8,0,7,6])
Ert = statistics.stdev([2,1,1,1,1,1,1,2,3,4,5,6,7,8,9,0,9,8,7,6,5,4,3,2,3,4,5,6,5,4,3,2,1,2,3,4,5,6,7,6,5,4,3,2,3,4,5,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,4,8,7,8,8,9,0,9,8,9,8,7,6,5,4,4,6,7,8,9,0,8,0,7,6])
print(Md)
print(Vr)
print(Ert)
print("__________________________________________________")
from datetime import date
date_aujourduit = date.today()
print("la date d'aujourduit est :",date_aujourduit)
print("__________________________________________________")
import webbrowser
url = "https://www.facebook.com/"
print("kayna")
#webbrowser.open(url)
print("__________________________________________________")
from forex_python.bitcoin import BtcConverter

bitcoins = BtcConverter()
print(bitcoins.get_latest_price('EUR'))
print(bitcoins.get_latest_price('USD'))
print(bitcoins.get_latest_price('MAD'))