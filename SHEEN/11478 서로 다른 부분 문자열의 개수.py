from itertools import combinations


A = input()
array = []
A = ''.join(sorted(A))
print(A)
A = list(combinations(A, 2))
for k in A:
    tup = ''.join(k)
    print(tup)