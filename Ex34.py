L = [10, ['marth','chimie'], ['python','c++']]
print("____________append()_______________")
L.append('maroc')
print(L)   #[10, ['marth', 'chimie'], ['python', 'c++'], 'maroc']
L.append([2,4])
print(L)   #[10, ['marth', 'chimie'], ['python', 'c++'], 'maroc', [2, 4]]
L[1].append('svt')
print(L)  #[10,  ['marth', 'chimie', 'svt'], ['python', 'c++'], 'maroc', [2, 4]]
print("____________insert()_______________")
L.insert(0,11)
print(L) #[11, 10, ['marth', 'chimie', 'svt'], ['python', 'c++'], 'maroc', [2, 4]]
L.insert(2,[23,25])
print(L) #[11, 10, [23, 25], ['marth', 'chimie', 'svt'], ['python', 'c++'], 'maroc', [2, 4]]
L[3].insert(1,'physique')
print(L) #[11, 10, [23, 25], ['marth', 'physique', 'chimie', 'svt'], ['python', 'c++'], 'maroc', [2, 4]]
print("____________extend()_______________")
L.extend([1,2,3])
print(L) #[11, 10, [23, 25], ['marth', 'physique', 'chimie', 'svt'], ['python', 'c++'], 'maroc', [2, 4], 1, 2, 3]
L[4].extend(['HTML','CSS'])
print(L) #[11, 10, [23, 25], ['marth', 'physique', 'chimie', 'svt'], ['python', 'c++', 'HTML', 'CSS'], 'maroc', [2, 4], 1, 2, 3]







