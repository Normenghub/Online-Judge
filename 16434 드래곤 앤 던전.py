n, attack = map(int,input().split())
maxhp = 0
hp = 0
for _ in range(n):
 a, b, c = map(int,input().split())
 if a == 1:
  if c %attack == 0: hp -= b*((c//attack)-1)
  else: hp-= b*(c//attack)
 else: 
   attack += b
   if maxhp > hp: maxhp = hp
   if hp + c > 0: hp = 0
   else:  hp += c
if maxhp > hp: maxhp = hp
print(abs(maxhp)+1)
  


