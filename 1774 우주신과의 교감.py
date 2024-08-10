import heapq,sys,math
input = sys.stdin.readline
result = 0 
n,k = map(int,input().split())
visited =[False] * (n+1)
front = [[] for _ in range(n+1)]
def caculateDistance(x,y,dx,dy):
    ddx = (dx - x)**2
    ddy = abs(dy - y)**2
    return round(math.sqrt(ddx+ddy),2)
arr= []
for _ in range(n):
    a,b = map(int,input().split())
    arr.append((a,b))
for _ in range(k):
    a,b = map(int,input().split())
    front[a].append((0,b))
    front[b].append((0,a))
for i in range(n):
    for k in range(i+1,n):
        distance = caculateDistance(arr[i][0], arr[i][1], arr[k][0], arr[k][1])
        front[i+1].append((distance,k+1))
        front[k+1].append((distance,i+1))
        
def MST(start):
    global result
    q = []
    for i in front[start]:
        heapq.heappush(q,i)
    visited[start] = True
    while q:
        r,c = heapq.heappop(q)
        if visited[c]:
            continue
        visited[c] = True
        result += r
        for a ,b in front[c]:
            if visited[b]:
                continue
            heapq.heappush(q,(a,b))
MST(1)
print(f"{result:.2f}")

         
