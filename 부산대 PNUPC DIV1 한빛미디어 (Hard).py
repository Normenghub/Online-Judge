import sys

input =sys.stdin.readline

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:  
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def inorder_traversal(self):
        self.present = 0
        self.count = 0
        self._inorder_traversal(self.root)
        return self.count

    def _inorder_traversal(self, node):
        if node:
            self._inorder_traversal(node.left)
            if self.present == 0 or self.present * 2 <= node.val:
                self.present = node.val
                self.count += 1
            self._inorder_traversal(node.right)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if not node:
            return node
        
        if key < node.val:
            node.left = self._delete(node.left, key)
        elif key > node.val:
            node.right = self._delete(node.right, key)
        else:
        
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp

            temp = self.min_value_node(node.right)

            node.val = temp.val

            node.right = self._delete(node.right, temp.val)

        return node

    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

bst = BinarySearchTree()

for i in range(int(input())):
    way = list(map(int,input().split()))
    if way[0] == 1:
        bst.insert(way[1])
    elif way[0] == 2:
        bst.delete(way[1])
    else:
        present = 0
        count  = 0
        print(bst.inorder_traversal())



