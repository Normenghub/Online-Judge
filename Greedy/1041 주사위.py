import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
result = []
minSum =[]
minSum.append([arr[0],arr[4],arr[2]])
minSum.append([arr[0],arr[4],arr[3]])
minSum.append([arr[0],arr[1],arr[3]])
minSum.append([arr[0],arr[1],arr[2]])
minSum.append([arr[5],arr[4],arr[2]])
minSum.append([arr[5],arr[4],arr[3]])
minSum.append([arr[5],arr[1],arr[3]])
minSum.append([arr[5],arr[1],arr[2]])
for xx in range(len(minSum)):
    minSum[xx].sort()

if n ==1 :
    arr.sort()
    del arr[-1]
    print(sum(arr))
      
         
         
elif n ==2 :
    for ii in range(8):
            resultValue = 0
            resultValue += (minSum[ii][-1] * 4)
            del minSum[ii][-1]
            resultValue += (sum(minSum[ii]) * 8)
            result.append(resultValue)
    print(min(result))   
else:
     for iii in range(8):
          resultValue = 0
          resultValue += (sum(minSum[iii]) * 4)
          del minSum[iii][-1]
          resultValue += (sum(minSum[iii])*((8*n)-12)) 
          del minSum[iii][-1]
          resultValue += (sum(minSum[iii])* ((4*(n-1)*(n-2)) + ((n*n)-((4*n)-4))))  
          result.append(resultValue)
     print(min(result))
# if 3 -> 1 2 3 4 5 6
# - > 1 1  1 1  1 1  1 1 6 6 6 6 1 3 3 3 3 3 3 3 3 3 3 3 3

          