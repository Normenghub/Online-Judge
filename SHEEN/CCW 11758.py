import sys 
input = sys.stdin.readline

x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())
result = ((x2-x1) * (y3-y2)) - ((y2-y1) * (x3-x2)) # 시작 끝 벡터 두 개 생성후 외적 계산.
if result == 0 :
    print(0)
elif result > 0:
    print(1)
else:
    print(-1)        