import sys
input = sys.stdin.readline
h = int(input())
w = int(input())
if h >= w:
    r =w/2 * 100
    print(int(r))
else:
    r = h/2 * 100
    print(int(r))