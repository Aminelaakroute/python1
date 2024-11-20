L = [10,[10, 12, 14.5, 6, 2.5, 8, 6.5, 12, 14.5, 10.5, 9.5, 14, 12, 15, 13.5, 19, 20, 10, 19, 18] , ['math', 'chimie'], ['python', 'c++', 'HTML', 'CSS'], 'maroc']
print("_____________Operation_______________")
print("_____________len()_______________")
print(len(L)) # 5
print(len(L[1])) #20
print("_____________sum()_______________")
print(sum(L[1])) #246.5
print("_____________ max() et min() _______________")
print("le maximum dans L[1] est :",max(L[1])) #le maximum dans L[1] est : 20
print("le minimum dans L[1] est :",min(L[1])) #le minimum dans L[1] est : 2.5
print("_____________count()_______________")
print(L[1].count(10)) #2
print("_____________reverse()_______________")
L.reverse()
print(L) #['maroc', ['python', 'c++', 'HTML', 'CSS'], ['marth', 'chimie'], [10, 12, 14.5, 6, 2.5, 8, 6.5, 12, 14.5, 10.5, 9.5, 14, 12, 15, 13.5, 19, 20, 10, 19, 18], 10]
L.reverse()
print(L) #[10, [10, 12, 14.5, 6, 2.5, 8, 6.5, 12, 14.5, 10.5, 9.5, 14, 12, 15, 13.5, 19, 20, 10, 19, 18], ['marth', 'chimie'], ['python', 'c++', 'HTML', 'CSS'], 'maroc']
print("_____________sort()_______________")
L[1].sort(reverse=False)
print(L) #[10, [2.5, 6, 6.5, 8, 9.5, 10, 10, 10.5, 12, 12, 12, 13.5, 14, 14.5, 14.5, 15, 18, 19, 19, 20], ['marth', 'chimie'], ['python', 'c++', 'HTML', 'CSS'], 'maroc']
L[1].sort(reverse=True)
print(L) #[10, [20, 19, 19, 18, 15, 14.5, 14.5, 14, 13.5, 12, 12, 12, 10.5, 10, 10, 9.5, 8, 6.5, 6, 2.5], ['marth', 'chimie'], ['python', 'c++', 'HTML', 'CSS'], 'maroc']
L[2].sort(key=len, reverse=True)
print(L) #[20, 19, 19, 18, 15, 14.5, 14.5, 14, 13.5, 12, 12, 12, 10.5, 10, 10, 9.5, 8, 6.5, 6, 2.5], ['chimie', 'math'], ['python', 'c++', 'HTML', 'CSS'], 'maroc']
L[3].sort(key=str.upper,reverse=True)
print(L) #[10, [20, 19, 19, 18, 15, 14.5, 14.5, 14, 13.5, 12, 12, 12, 10.5, 10, 10, 9.5, 8, 6.5, 6, 2.5], ['chimie', 'math'], ['python', 'HTML', 'CSS', 'c++'], 'maroc']
Lh = sorted(L[1])
print(Lh)
print("_____________index()_______________")
print(L[1].index(12))
print(L[1].index(10,13))
print(L[1].index(18,0,4))
