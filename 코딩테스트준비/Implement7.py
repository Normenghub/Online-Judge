N = int(input())
threeCount = 0
time = ""
for i in range(N+1):
    for k in range(60):
        for z in range(60):
            time += str(i) + str(k) + str(z)
            if '3' in time:
                threeCount +=1
            else:
                pass
            time=""    
print(threeCount)            