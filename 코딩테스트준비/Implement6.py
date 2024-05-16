N = int(input())
maps = []
for i in range(N):
    for k in range(N):
        maps.append([i,k])
direction = list(map(str,input().split()))

dd = [[-1,0],[1,0],[0,1],[0,-1]]

def outLines(r,c):
    return 0<= r <= N-1 and 0 <= c <=N-1
r = 0
c=  0
for go in direction:
   if go == 'U':
      if outLines(r+dd[0][0],c+ dd[0][1]):
        r +=dd[0][0]
        c += dd[0][1]
      else:
         pass
   elif go == 'D':     
      if outLines(r+dd[1][0],c+ dd[1][1]):
        r +=dd[1][0]
        c += dd[1][1]
      else:
         pass  
   elif go == 'R':     
      if outLines(r+dd[2][0],c+ dd[2][1]):
        r +=dd[2][0]
        c += dd[2][1]
      else:
         pass  
   else:     
      if outLines(r+dd[3][0],c+ dd[3][1]):
        r +=dd[3][0]
        c += dd[3][1]
      else:
         pass       

print(f'{r+1} {c+1}')      