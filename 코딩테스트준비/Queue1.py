import queue

queue = queue.Queue()

infor = []
num = int(input())
count = 0
for i in range(num):
   smallList = list(input().split())
   if len(smallList)==2:
       queue.put(int(smallList[1]))
       count +=1
       infor.append([count,int(smallList[1])])
   else:
       queue.get()
       count -=1

infor = sorted(infor, key = lambda x: (-x[0], x[1]))

print(f"{infor[0][0]} {infor[0][1]}") 
         

# deque << 스택, 큐 한 번에 해결 가능          