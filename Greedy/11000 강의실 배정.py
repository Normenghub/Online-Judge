import sys 
import heapq
n = int(sys.stdin.readline().rstrip())
arr=[]
saveEnd = []
srr3=[]
for _ in range(n):
    a = list(map(int,sys.stdin.readline().rstrip().split()))
    arr.append(a)

arr.sort(key=lambda x: (x[0],x[1]))
count =1
heapq.heappush(saveEnd, arr[0][1])


for a in range(1,n):
    x = heapq.heappop(saveEnd)
    if x == arr[a][0]:
        heapq.heappush(saveEnd, arr[a][1])
        continue
    else:
        heapq.heappush(saveEnd,x)
        lenghts = len(saveEnd)
        for z in range(lenghts):
            x =saveEnd[z]
            del saveEnd[z]
            if x == arr[a][0]:
                heapq.heappush(saveEnd, arr[a][1])
                break  
            else:
                saveEnd.append(x)
                continue
        saveEnd.append(arr[a][1])
        heapq.heapify(saveEnd)            
        count+=1     
   
print(count)              
                
'''
1 3
2 4
1 2
3 4
5 6
2 3
4 5



        
'''

       
       
     
    