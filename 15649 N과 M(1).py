import itertools
a,b = map(int,input().split())
arr = [x for x in range(1,a+1)]    

l  = list(itertools.permutations(arr, b))
for k in range(len(l)):
    for z in range(len(l[k])):
        print(l[k][z],end=" ")
    print()    