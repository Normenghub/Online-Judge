import sys
input= sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
arr2 = sorted(arr)
dic = {}
dic2 = {}
queue = []
for i in range(n):

    dic[arr2[i]] = arr[i] 
    dic2[arr2[i]] = False
    
for k in arr:
    if dic2[k]:
        continue
    else:
        if dic[k] == k:
            dic2[k] = True
            continue
        else:
            count = 0
            while True:
                if dic2[k] ==  True:
                    break
                dic2[k] = True
                x = dic[k]
                k = x
                count +=1
            queue.append(count)
                
result =0
for i in queue:
    result += i-1
print(result)