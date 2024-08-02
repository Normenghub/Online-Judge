import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
result = 0
arr = [False] * (n+1)
le = [0]
adress = 0
for _ in range(k):
    le.append(int(input()))
for x in range(1,len(le)):
    same = False
    if le[x] == le[x-1]:
        same = True
    if not arr[le[x]]:
        arr[le[x]] = True
        result +=1
        adress= le[x]
    else:
        flag = False
        if not same:
         for z in range(le[x],0,-1):
            if not arr[z]:
                arr[z] = True
                result +=1
                flag = True
                adress= z
                break

         if not flag:
            break
        else:
           for z in range(adress-1,0,-1):
              if not arr[z]:
                 arr[z] = True
                 result +=1
                 flag = True
                 break
           if not flag:
              break
           
print(result)