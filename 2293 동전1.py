import sys

input = sys.stdin.readline

n,k = map(int,input().split())

dp = [0] * (k+1)
arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort()
dp [0] = 1


for x in arr:
    for s in range(x,k+1):
        dp[s] = dp[s] + dp[s-x]

print(dp[k])


