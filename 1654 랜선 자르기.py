import sys
input = sys.stdin.readline

n , k = map(int,input().split())

arr = []
start = 0
end = 0
result = 0

for i in range(n):
 x = int(input())
 end = max(end,x)
 arr.append(x)


while start <= end:
  mid = (start + end) // 2
  total = 0
  for x in arr:
    try:
     total += x// mid
    except:
      print(1)
      exit()
  if total < k:
    end = mid-1
  elif total >= k:
    result = mid
    start = mid +1
  


print(result)
