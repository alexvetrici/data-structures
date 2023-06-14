# Tree implementation 

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(node):
    if node:
        inorder(node.left)
        print(node.data)
        inorder(node.right)

def preorder(node):
    if node:
        print(node.data)
        preorder(node.left)
        preorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data)

root = Node(10)
root.left = Node(78)
root.right = Node(2)
root.left.left = Node(54)
root.left.right = Node(9)
root.right.left = Node(1)
root.right.right = Node(3)

postorder(root)