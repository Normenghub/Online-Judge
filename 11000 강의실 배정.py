import sys 
import heapq   
n = int(sys.stdin.readline().rstrip())
arr = []
End = []
for _ in range(n):
    a = list(map(int,sys.stdin.readline().rstrip().split()))
    arr.append(a)
arr.sort(key=lambda x: (x[0],x[1]))
heapq.heappush(End, arr[0][1])
for i in range(1,n):
    if arr[i][0] < End[0]:
        heapq.heappush(End,arr[i][1])
    else:
        heapq.heappop(End)
        heapq.heappush(End,arr[i][1])


print(len(End))




         

                   
    

    