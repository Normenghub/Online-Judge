from itertools import permutations


A = input()
array = []
A = ''.join(sorted(A))
A = list(permutations(A, len(A)))

for k in A:
    tup = ''.join(k)
    print(tup)