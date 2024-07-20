import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

n,m = map(int,input().split())
arr = []
for i in range(n+1):
      arr.append(i)

def findParents(arr,a):
        if arr[a] != a:
               arr[a] = findParents(arr,arr[a])
        return arr[a]

def union(arr,a,b):
      a = findParents(arr,a)
      b = findParents(arr,b)
      if a > b:
            arr[b] = a
      else:
            arr[a] = b

for i in range(m):  
  a,b,c = map(int,input().split())
  if a == 0:
        union(arr,b,c)

  elif a == 1:
        if b==c:
         print("YES")
        elif findParents(arr,b) == findParents(arr,c):
              print("YES")
        else:
              print("NO")
          

