L = [10, ['marth', 'chimie'], ['python', 'c++', 'HTML', 'CSS'], 'maroc']
H = L.copy()
K = L.copy()
print("____________remove()_______________")
L.remove(['marth', 'chimie'])
print(L) #[10, ['python', 'c++', 'HTML', 'CSS'], 'maroc']
L[1].remove('python')
print(L)  #[10, ['c++', 'HTML', 'CSS'], 'maroc']
print("____________pop()_______________")
m = L.pop(1)
print(L) #[10, 'maroc']
print(m) #['c++', 'HTML', 'CSS']
m.pop(1)
print(m) #['c++', 'CSS']
print("____________clear()_______________")
print(H) #[10, ['marth', 'chimie'], ['c++', 'CSS'], 'maroc']
print(K) #[10, ['marth', 'chimie'], ['c++', 'CSS'], 'maroc']
H.clear()
print(H)  #[]
del(K[0])
print(K) #[['marth', 'chimie'], ['c++', 'CSS'], 'maroc']
del(K[0][1])
print(K) #[['marth'], ['c++', 'CSS'], 'maroc']