n = int(input())

km = list(map(int,input().split()))
literprice = list(map(int,input().split()))
currentprice = literprice[0]
sumprice = 0
for z in range(1,len(literprice)):
    if literprice[z] < currentprice:
        sumprice += (currentprice * km[z-1])
        currentprice = literprice[z]
    else:
        sumprice += (currentprice * km[z-1])
        
print(sumprice)



        
        
    
