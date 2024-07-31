import sys
input =sys.stdin.readline

n,k = map(int,input().split())

dp = [[0] * (n+1) for i in range(k+1)]

for i in range(1,k+1):
    dp[i][1] = i
    dp[i][0] = 1
for i in range(1,k+1):
    for z in range(2,n+1):
        dp[i][z] = dp[i][z-1] + dp[i-1][z]

print(dp[k][n]%1000000000)