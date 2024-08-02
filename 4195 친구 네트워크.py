import sys
input = sys.stdin.readline
def whoParent(a):
    if friend[a] == a:
        return a 
    else:
        return whoParent(friend[a])
    
def union(a,b):
    parenta = whoParent(a)
    parentb = whoParent(b)
    if parentb == parenta:
        return parenta
    if parenta < parentb:
        
        friend[parentb] = parenta
        howMany[parenta] += howMany[parentb]
        del howMany[parentb]
        return parenta
    else:
        friend[parenta] = parentb
        howMany[parentb] += howMany[parenta]
        del howMany[parenta]
        return parentb

def friendCheck(a):
    if a not in friend:
        friend[a] = a
        howMany[a] = 1


for _ in range(int(input())):
    friend = dict()
    howMany = {}
    for _ in range(int(input())):
        person1,person2 = map(str,input().split())
        friendCheck(person1)
        friendCheck(person2)
        
        realParent = union(person1,person2)
        print(howMany[realParent])

        
        
        