import sys
input = sys.stdin.readline
n = int(input())
'''
count = 0
zz = 0
zzz = 0
memoization = []
memoization2 = []
if n ==2:
    print(1)
    exit()
elif n ==3:
    print(1)
    exit()
elif n ==1:
    print(0)
    exit()
else:
        if n %3 == 0:
           memoization.append(n//3)
           zz +=1
           if n%2==0:
               memoization.append(n//2)
               zz+=1
               memoization.append(n-1)
               zz+=1
           else:
                memoization.append(n-1)
                zz+=1
        elif n%2==0:
               memoization.append(n//2)
               zz+=1
               memoization.append(n-1)
               zz+=1
        else:
             memoization.append(n-1)
             zz+=1     
while True:
  if 1 in memoization:
       count +=1
       break   
  for i in range(zzz,zz):
        if memoization[i] %3 == 0:
           memoization.append(memoization[i]//3)
           zz +=1
           if memoization[i]%2==0:
               memoization.append(memoization[i]//2)
               zz+=1
               memoization.append(memoization[i]-1)
               zz+=1
           else:
                memoization.append(memoization[i]-1)
                zz+=1
        elif memoization[i]%2==0:
               memoization.append(memoization[i]//2)
               zz+=1
               memoization.append(memoization[i]-1)
               zz+=1
        else:
             memoization.append(memoization[i]-1)
             zz+=1
  count +=1
  zzz = i+1
print(count) 
'''

dp = [0] * 1000001

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] +1 )
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] +1 )    

print(dp[n])