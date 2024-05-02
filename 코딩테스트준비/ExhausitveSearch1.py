from itertools import combinations

strings = input()
num=int(input())
C = list(combinations(strings, num))

D = list("".join(i) for i in C)

D.sort()

print(D)

