import sys
input =sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
arr.sort()
# 두개 더하기 
# 두 개 더한 값이 두 원소보다 크거나 같으면 while문 체크 후 값이 같거나 작을때까지
# 두 개 더한 값이 두 원소보다 작으면(?) << 성립 가능?
# 움직임은 투 포인터 
start = 0
end = 1
if n <= 2:
    print(0)
else:
    result = arr[start]+ arr[end]
    count = 0
    flag = True
    while True:
        print(count, end=' ')
        print(start, end = ' ')
        print(end, end = ' ')
        print(result)
        if result > arr[end]:
            j = end + 1
            while j <= len(arr)-1:
                if arr[j] == result:
                    count +=1
                    break
                elif arr[j] > result:
                    break
                else:
                    j+=1
            if flag == True:
               result -= arr[end]
               end +=1
               try:
                  result += arr[end]
                  flag = False
               except:
                  break
            else:
               result -= arr[start]
               start +=1
               result += arr[start]
               flag = True
        elif result < arr[start]:
            if start != 0:
                j = start-1
                while j >= 0:
                    if arr[j] == result:
                     count +=1
                     break
                    elif arr[j] < result:
                     break
                    else:
                     j-=1
                if flag == True:
                  result -= arr[end]
                  end +=1
                  try:
                   result += arr[end]
                   flag = False
                  except:
                   break
                else:
                 result -= arr[start]
                 start +=1
                 result += arr[start]
                 flag = True
            else:
               if flag == True:
                 result -= arr[end]
                 end +=1
                 try:
                  result += arr[end]
                  flag = False
                 except:
                  break
               else:
                result -= arr[start]
                start +=1
                result += arr[start]
                flag =True
        else:                      
             if end - start == 1:
                if flag == True:
                 result -= arr[end]
                 end +=1
                 try:
                  result += arr[end]
                  flag = False
                 except:
                  break
                else:
                 result -= arr[start]
                 start +=1
                 result += arr[start]
                 flag =True
             else:
                j = start + 1
                while j < end:
                   if arr[j] == result:
                      count +=1
                      break
                   elif arr[j] > result:
                      break
                   else:
                      j+=1 
                if flag == True:
                 result -= arr[end]
                 end +=1
                 try:
                  result += arr[end]
                  flag = False
                 except:
                   break
                else:
                 result -= arr[start]
                 start +=1
                 result += arr[start]
                 flag =True
    print(count)