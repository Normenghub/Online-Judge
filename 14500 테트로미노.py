import sys
input = sys.stdin.readline

graph = []
n,m = map(int,input().split())
maxs = 0

for _ in range(n): graph.append(list(map(int,input().split())))

def block1():
    global maxs

    for i in range(n):
        for k in range(m-3):
          result = 0
          for z in range(4):
            result += graph[i][k+z]
          maxs = max(maxs,result)
    for i in range(m):
       for k in range(n-3):
          result2 = 0
          for z in range(4):
             result2 += graph[k+z][i]
          maxs = max(maxs,result2)

def block2():
   global maxs
   for i in range(n-1):
      for k in range(m-1):
         result = graph[i][k] + graph[i][k+1] + graph[i+1][k] + graph[i+1][k+1]
         maxs = max(maxs, result)

def block3():
   global maxs
   for i in range(n-2):
      for k in range(m-1):
       result = 0
       arr = []
       for z in range(3):
          result += graph[i+z][k] + graph[i+z][k+1]
          arr.append([i+z,k])
          arr.append([i+z,k+1])
       maxs = max(result - graph[arr[3][0]][arr[3][1]] - graph[arr[5][0]][arr[5][1]],
                  result - graph[arr[1][0]][arr[1][1]] - graph[arr[3][0]][arr[3][1]],
                  result - graph[arr[0][0]][arr[0][1]] - graph[arr[2][0]][arr[2][1]],
                  result - graph[arr[2][0]][arr[2][1]] - graph[arr[4][0]][arr[4][1]],
                  result - graph[arr[1][0]][arr[1][1]] - graph[arr[5][0]][arr[5][1]],
                  result - graph[arr[0][0]][arr[0][1]] - graph[arr[4][0]][arr[4][1]],
                  result - graph[arr[1][0]][arr[1][1]] - graph[arr[4][0]][arr[4][1]],
                  result - graph[arr[0][0]][arr[0][1]] - graph[arr[5][0]][arr[5][1]],
                  
                  maxs)
   for i in range(n-1): 
      for k in range(m-2):
         result = 0 
         arr = []
         for z in range(3):
          result += graph[i][k+z] + graph[i+1][k+z]
          arr.append([i,k+z])
          arr.append([i+1,k+z])
         maxs = max(result - graph[arr[0][0]][arr[0][1]] - graph[arr[2][0]][arr[2][1]],
                    result - graph[arr[3][0]][arr[3][1]] - graph[arr[5][0]][arr[5][1]],
                    result - graph[arr[0][0]][arr[0][1]] - graph[arr[5][0]][arr[5][1]],
                    result - graph[arr[0][0]][arr[0][1]] - graph[arr[4][0]][arr[4][1]],
                    result - graph[arr[1][0]][arr[1][1]] - graph[arr[5][0]][arr[5][1]],
                    result - graph[arr[1][0]][arr[1][1]] - graph[arr[4][0]][arr[4][1]],
                    result - graph[arr[2][0]][arr[2][1]] - graph[arr[4][0]][arr[4][1]],
                    result - graph[arr[1][0]][arr[1][1]] - graph[arr[3][0]][arr[3][1]],
                  maxs)   
      
block1()
block2()
block3()

print(maxs)






