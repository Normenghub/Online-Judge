import itertools 

n,m = map(int,input().split())

arr =[i for i in range(1,n+1)]
nCr = itertools.combinations(arr,m)
nCr = list(nCr)
for z in range(len(nCr)):
    for k in range(len(nCr[z])):
        print(f"{nCr[z][k]}",end = " ")
    print()    