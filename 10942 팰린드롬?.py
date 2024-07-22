import sys
input = sys.stdin.readline

n = int(input())

arr= list(map(int,input().split()))

dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(n):
    dp[i][i] = 1
for i in range(n-1):
    if arr[i] == arr[i+1]:
        dp[i][i+1] = 1
for i in range(n-2):
    for k in range(n-2-i):
        j = i+k+2
        if arr[k] == arr[j] and  dp[k+1][j-1] ==  1:
            dp[k][j] = 1


for _ in range(int(input())):
    a,b = map(int,input().split())
    print(dp[a-1][b-1])