import sys
input = sys.stdin.readline

dp = [[0,0,0] for _ in range(41)]
dp[0][1] = 1
dp[2][0] = 1
dp[1][0] = 1
dp[1][2] = 1
dp[2][1] = 1
dp[2][2] = 1
dp[3][1] = 1
dp[3][2] = 2
dp[4][1] = 2
dp[4][2] = 3

for i in range(5,41):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i-1][1] + dp[i-2][1]
    dp[i][2] = dp[i-1][2] + dp[i-2][2]  

for _ in range(int(input())):
    x = int(input())
    print(f'{dp[x][1]} {dp[x][2]}')
    