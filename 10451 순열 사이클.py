import sys
input = sys.stdin.readline
for i in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    arr2 = sorted(arr)
    dic = {}
    dic2 = {}
    count = 0
    queue = []
    for i in range(len(arr2)):
        dic[arr2[i]] = arr[i]
        dic2[arr2[i]] = False
        queue.append(arr2[i])
    while queue:
        x = queue.pop()
        if dic2[x] == True:
            continue
        else:
            if dic[x] == x:
                dic2[x] = True
                count+=1
                continue
            else:
                while dic2[x] == False:
                    dic2[x] = True
                    x = dic[x]
                count +=1
                continue
    print(count)


    
