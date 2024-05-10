from collections import deque
n = int(input())

arr = deque(map(int,input().split()))
save = [1]
index =deque()
for i in range(2,n+1):
    index.append(i)
howMany = arr.popleft()
if howMany < 0:
    temp = -1
else:  
    temp=1
while len(arr) >0:
    if howMany >0:  
        if howMany != temp:
            arr.append(arr.popleft())
            index.append(index.popleft())
            temp+=1

        else:
            temp = arr.popleft()
            howMany = temp
            save.append(index.popleft())
            if temp <0:
                temp = -1
            else:
                temp =1    
    else:
       if howMany != temp:
           arr.appendleft(arr.pop())
           index.appendleft(index.pop())
           temp-=1
       else:
           temp = arr.pop()
           howMany = temp    
           save.append(index.pop())
           if temp <0:
                temp = -1
           else:
                temp =1             
for i in save:
    print(i,end = " ")
