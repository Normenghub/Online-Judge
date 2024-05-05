numarr = []
for i in range(1,200):
    for z in range(i):
       numarr.append(i)
a,b = map(int,input().split())

sum = 0 
for s in range(a-1,b):
    sum += numarr[s]
print(sum)    