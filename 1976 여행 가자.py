import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
arr = [i for i in range(n+1)]
dic = {}
def findParents(v):
   if arr[v] == v:
      return arr[v]
   else:
      return findParents(arr[v])
def union(v,e):
   parentsA = findParents(v)
   parentsB = findParents(e)
   if parentsA < parentsB:
      arr[parentsA] = parentsB
   elif parentsB < parentsA:
      arr[parentsB] = parentsA
   
for i in range(n):
   x = list(map(int,input().split()))
   for k in range(n):
      if x[k] == 1:
         union(i+1,k+1)
        
      
plan = list(map(int,input().split()))

for i in range(m-1):
   if plan[i] not in dic:
      dic[plan[i]] = findParents(plan[i])
      one = dic[plan[i]]
   else:
      one = dic[plan[i]]
   if plan[i+1] not in dic:
      dic[plan[i+1]] = findParents(plan[i+1])
      two = dic[plan[i+1]]

   else:
      two = dic[plan[i+1]]
   if one == two:
      continue
   else:
      print("NO")
      exit()
print("YES")
    
      


