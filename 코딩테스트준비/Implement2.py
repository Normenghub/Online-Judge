n, m = map(int,input().split())
subjectList= list(input().split())

for i in range(m):
   subject = input()
   if subject != '-':
    print(subjectList.count(subject))
   else:
     print(n) 