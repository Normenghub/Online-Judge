# 씨발 느금마
import sys
input = sys.stdin.readline
n,s = map(int,input().split())
arr =list(map(int,input().split()))
start = 0
end = 0
result = arr[start]
mins = 999999999999999999999
while start <= end and end < n:
    if result < s:
        end +=1
        try:
             result += arr[end]
        except:
             break
    else:
            mins = min(mins, end-start+1)
            result -=arr[start]
            start +=1
if mins == 999999999999999999999:
     print(0)
else:
     print(mins)

    
