import sys
input = sys.stdin.readline
arr = []
for i in range(int(input())): arr.append(list(map(int,input().split())))

for i in range(1,len(arr)):
   x = [arr[i-1][0],arr[i-1][1],arr[i-1][2]]
   xc = [arr[i-1][0],arr[i-1][1],arr[i-1][2]]
   xc.sort()
   index1 =x.index(xc[0])
   index2 =x.index(xc[1])
   for k in range(3):
      if k == index1:
         arr[i][k] += xc[1]
      else:
         arr[i][k] += xc[0]
print(min(arr[len(arr)-1]))