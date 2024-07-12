import sys
input = sys.stdin.readline
n = int(input())
alphbet =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
dic = {}
for i in range(n):
    dic[alphbet[i]] = []
for _ in range(n):
    a,b,c = map(str,input().split())
    dic[a].append(b)
    dic[a].append(c)
def preorder(dic,v):
     print(v,end="")
     if dic[v][0] != '.':
          preorder(dic,dic[v][0])
     else:
          pass
     if dic[v][1] != '.':
          preorder(dic,dic[v][1])
     else:
          pass

preorder(dic,'A')
print()
def inorder(dic,v):
     if dic[v][0] != '.':
          inorder(dic,dic[v][0])
     print(v,end= "")
     if dic[v][1] != '.':
          inorder(dic,dic[v][1])


inorder(dic,'A')
print()

def postorder(dic,v):
     if dic[v][0] != '.':
          postorder(dic,dic[v][0])
     if dic[v][1] != '.':
          postorder(dic,dic[v][1])
     print(v,end= "")
postorder(dic,'A')