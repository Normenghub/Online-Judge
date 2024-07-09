import sys
input = sys.stdin.readline

graph =[] 
tf = []
n,m = map(int,input().split())
x,y,direction = map(int,input().split())
for _ in range(n):
    qwe = list(map(int,input().split()))
    s = [False] * m
    graph.append(qwe)
    tf.append(s)
#초기설정

dd = [[1,0],[0,-1],[-1,0],[0,1]]


def turn():
    global direction
    direction -=1
    if direction<0:
     direction = 3

def canGo(r,c):
    return 0<= r < n and 0<= c < m

def canBack(r,c,graph):
    global direction
    r +=dd[direction][0]
    c +=dd[direction][1]
    return canGo(r,c) and graph[r][c] == 0
count = 0
while True:
    if graph[x][y] == 0 and not tf[x][y]:
        count +=1
        tf[x][y] = True
    
    countxxyy = 0
    for dr ,dc in dd:
        ddr = dr+ x
        ddc = dc + y
        if not canGo(ddr,ddc) or graph[ddr][ddc] != 0 or tf[ddr][ddc]:
            countxxyy+=1
    if countxxyy == 4:
        if not canBack(x,y,graph):
            break
        else:
            x += dd[direction][0]
            y += dd[direction][1]
            continue
    else:
        for _ in range(4):
           turn()
           if direction== 0 and graph[x-1][y] == 0 and not tf[x-1][y] and canGo(x-1,y):
            x-=1
            break
           elif direction== 1 and graph[x][y+1] == 0 and not tf[x][y+1] and canGo(x,y+1):
                y+=1
                break
           elif direction== 2 and graph[x+1][y] == 0 and not tf[x+1][y] and canGo(x+1,y):
                x+=1
                break
           elif direction== 3 and graph[x][y-1] == 0 and not tf[x][y-1] and canGo(x,y-1):
                    y-=1
                    break
print(count)

    
   

