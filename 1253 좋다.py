import sys
input = sys.stdin.readline

# 입력 처리
n = int(input().strip())
x = list(map(int, input().strip().split()))

# 배열 정렬
arr = sorted(x)

# 결과값을 저장할 변수
good_count = 0

# 각 요소를 차례대로 검사
for i in range(n):
    target = arr[i]
    start = 0
    end = n - 1
    
    while start < end:
        if start == i:
            start += 1
            continue
        if end == i:
            end -= 1
            continue
        
        sum_val = arr[start] + arr[end]
        
        if sum_val == target:
            good_count += 1
            break
        elif sum_val < target:
            start += 1
        else:
            end -= 1

# 결과 출력
print(good_count)