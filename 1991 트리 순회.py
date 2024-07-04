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
def preorder(dic,s):
    print(s,end="")
    if dic[s][0] != '.':
        preorder(dic,dic[s][0])
    if dic[s][1] != '.':
        preorder(dic,dic[s][1])
preorder(dic,'A')
print()
def inorder(dic, s):
    if s == '.':
        return
    if dic[s][0] != '.':
        inorder(dic, dic[s][0])
    print(s, end = "")
    if dic[s][1] != '.':
        inorder(dic, dic[s][1])
def postorder(dic,s):
    if s == '.':
        return
    if dic[s][0] != '.':
        inorder(dic, dic[s][1])
    if dic[s][1] != '.':
        inorder(dic, dic[s][0])
    print(s, end = "")
    
inorder(dic,'A')
print()
postorder(dic,'A')
