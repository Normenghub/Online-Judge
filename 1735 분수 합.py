import math
a,b = map(int,input().split())
c,d = map(int,input().split())

bb = b*d
aa = (a*d) +(b*c)
asd = math.gcd(aa,bb)
aa = int(aa/asd)
bb = int(bb/asd)
print(f"{aa} {bb}")
