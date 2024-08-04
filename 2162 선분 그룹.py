import sys
sys.setrecursionlimit(10*4)
input = sys.stdin.readline

n = int(input())
coordinate = [[]]
arr = [i for i in range(n+1)]
dic ={}
for i in range(1,n+1): dic[i] = 1
count  = 0
maxs = 0

def ccw(x1,y1,x2,y2,x3,y3):
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

def findParents(v):
    if arr[v] == v:
        return v
    else:
        arr[v] = findParents(arr[v])
        return findParents(arr[v])
    
def whosmin(x1,x2,x3,x4,x5,x6,x7,x8):
    player1 = 0
    player2 = 0
    if x5 < x1: player2+=1
    elif x5 > x1: player1+=1
    if x6 < x2: player2+=1
    elif x2 > x6: player1+=1
    if x7 < x3: player2+=1
    elif x3 > x7: player1+=1
    if x4 < x8: player2+=1
    elif x8 > x4: player1+=1
    if player1 == player2: return 0
    elif player1 > player2: return 1
    else: return 2

def union(a,b):
    parents1 = findParents(a)
    parents2 = findParents(b)
    if parents1 == parents2:
        return 
    else:
        arr[parents2] = parents1
        dic[parents1] += dic[parents2]
        del dic[parents2]
                

for _ in range(n):
    coordinate.append(list(map(int,input().split())))

def segments_intersect(i, k):
    x1, y1, x2, y2 = coordinate[i]
    x3, y3, x4, y4 = coordinate[k]

    ccw1 = ccw(x1, y1, x2, y2, x3, y3)
    ccw2 = ccw(x1, y1, x2, y2, x4, y4)
    ccw3 = ccw(x3, y3, x4, y4, x1, y1)
    ccw4 = ccw(x3, y3, x4, y4, x2, y2)

    if ccw1 * ccw2 <= 0 and ccw3 * ccw4 <= 0:
        if ccw1 == 0 and ccw2 == 0 and ccw3 == 0 and ccw4 == 0:
            if min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):
                return True
            else:
                return False
        return True
    return False

for i in range(1, n + 1):
    for k in range(i + 1, n + 1):  
        if segments_intersect(i, k):
            union(i, k)
for i in dic.keys():
    maxs = max(dic[i] , maxs)
print(len(dic.keys()))
print(maxs)
    

        
