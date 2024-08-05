import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

def dfs1(v):
    tf[v] = True
    for r,c in arr[v]:
        if tf[r]:
            continue
        dfs1(r)
        cnt[v] += cnt[r]
        dp[v] += c * cnt[r] + dp[r]

def dfs2(v):
    tf[v] = True
    for  r,c in arr[v]:
        if tf[r]:
            continue
        dp[r] = dp[v] - cnt[r] * c + (n- cnt[r]) * c
        dfs2(r)

while True:
    n = int(input())
    if n == 0:
        break
    else:
        arr = [[] for _ in range(n)]
        for _ in range(n-1):
            a,b,c = map(int,input().split())
            arr[a].append((b,c))
            arr[b].append((a,c))
        dp =[0] * (n)
        cnt = [1] * (n)
        tf = [False] * (n)
        dfs1(0)
        tf = [False] * (n)
        dfs2(0)
        print(min(dp))

    