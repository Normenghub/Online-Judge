# 짝수 -> 홀수자리의 숫자의 합과 짝수 자리 숫자의 합의 차가 항상 0
# 홀수 -> 11의 배수 
# 10000000이상인 수에선 팰린드롬수이며 소수인 수가 없음
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
def isPrime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
if M > 10000000: 
    M = 10000000
arr = [i for i in range(N,M+1) if str(i) == str(i)[::-1]]
for k in arr:
    if isPrime(k):
        print(k)
print(-1) 

