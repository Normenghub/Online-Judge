import sys 
input = sys.stdin.readline    
import heapq
result = 0
n = int(input())
lists = []
for i in range(n):
  a = int(input())
  lists.append(a)
lists.append(5)
lists.append(6)
heapq.heapify(lists)
print(lists)
for k in range(len(lists)):
  print(heapq.heappop(lists))

'''

        1
      2   3
   3    4    5    6
 10 19 29 

 if insert heqp 4

           1 
    2            3
  3     4      4    5
 6 10 19 29   


          1 
      2            3
   4      3     10    19
 5   6  5     
            

'''