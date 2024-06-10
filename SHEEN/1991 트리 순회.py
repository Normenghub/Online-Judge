import sys
imput = sys.stdin.readline
n = int(input())
if n == 1:
    a,b,c = map(str,input().split())
    for _ in range(3):
        print(a)
else:
    # 트리 생성
    treeSize = 0
    for i in range(0,n):
      treeSize += 2 **(i)
    tree = [0] * treeSize
    tree[1]= 'A'
    for i in range(n):
        x = list(map(str,input().split()))
        indexs = tree.index(x[0])
        if x[1] != '.':
             tree[indexs * 2] = x[1]
        if x[2] != '.':
             tree[indexs * 2 +1] = x[2]
    # 각각 트리 순환
     # 재귀로 푸는게 제일 빠름 .
        result = ""
        def preorder(tree,result):
            pass
        def inorder(treem,result):
            pass
        def postorder(tree,result):
            pass
        print(preorder(tree,result))
        print(inorder(tree,result))
        print(postorder(tree,result))

  
