
print("Petit programme de liste")
Liste1 = [1, 2, 3, 4, 6, 7, 8, 9]
Liste2 = ['amine', 'mohammed', 'ilias', 'mouad', 'ayman', 'redouane', 'anass']
Liste3 = [1, 'mohammed', True, 4, False, 7.12, 99998, 'amine']
print(Liste1)
print(Liste2[-1])
print(Liste3)
print("___________________________________________________")
Liste4 = list((1, 2, 3, 4, 6, 7, 8, 9))
Liste5 = list(('amine', 'mohammed', 'ilias', 'mouad', 'ayman', 'redouane', 'anass'))
Liste6 = list((1, 'mohammed', True, 4, False, 7.12, 99998, 'amine'))
print(Liste4)
print(Liste5[-1])
print(Liste6)
print("___________________________________________________")
Liste7 = list(('AMINE LAAKROUTE'))
Liste8 = list(range(0,99))
Liste9 = list(range(0,99,3))
print(Liste7)
print(Liste7[1])
print(Liste7[2])
print(Liste7[-5])
print(Liste7[-1])
print(Liste8)
print(Liste9)
print("___________________________________________________")
import string

Lettre = list(string.ascii_uppercase)

print(Lettre)
print(Liste1[-1:-9:-1])
print("___________________________________________________")

H = [ 1,2,3,4,5,6,7,8,9]
print(H)
H *=2
print(H)
print(Liste1 == Liste4)
print("___________________________________________________")

M = list(('AMINE LAAKROUTE', 2001, 175))
print(M)
Nom,Bd,taile=M
print(Nom)
print(Bd)
print(taile)
print("___________________________________________________")
l1 = list(range(1, 10 , 4))
print(l1)
l2 = list(range(2, 16 , 5))
print(l2)
l3 = l1 + l2
print(l3)
l4 = l1 * 2
print(l4)
print(l3==l4)
l3[-3:-1] = [1,5,9]
print(l3)
kk = list(range(0,5,3)) + l2*3
print(kk)

