import sys
input = sys.stdin.readline

dp = [1000001] * 1000001
dp [1] = 0
for i in range(1,1000001):
    if i * 3 < 1000001:
        dp[i*3] = min(dp[i*3] ,dp[i] + 1)
    if i * 2 < 1000001:    
     dp[i * 2] = min(dp[i*2] ,dp[i] + 1)
    if i + 1 < 1000001:
     dp[i+1] = min(dp[i+1] ,dp[i] + 1)
 


print(dp[int(input())])

#BottomUP DP