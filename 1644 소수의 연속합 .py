#에라토스테네스의 체로 n 까지 소수 판별 후 arr에 저장
# 투 포인터로 연속 누적합 구하고 같은거 나올떄마다 카운터 정렬 상태니까 합이 더 크면 start point << +1 합이더 작으면 end point + 1
# 같으면 된거에서 start point +1 에서 다시 시작 
import sys
input = sys.stdin.readline
n = int(input())
if n == 1:
   print(0)
   exit()
trueOrFalse = [True] * (n+1)
arr = []
trueOrFalse[0], trueOrFalse[1] == False
for i in range(2, n+1):
    if trueOrFalse[i] == True:
        arr.append(i)
        j =2
        while i * j <= n:
            trueOrFalse[i*j] = False
            j+=1
count = 0
start = 0
end = 0
result = 0
if arr[-1] == n:
   count +=1

while start <= end and end < len(arr):
    if result <n:
      result += arr[end]
      end+=1
    elif result > n:
      result -=arr[start]
      start +=1
    else:
      count +=1
      result += arr[end]
      end +=1
print(count)

