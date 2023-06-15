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


# Tree Implementation with BigTree package

# Run 'pip install bigtree' to install the package

from bigtree import Node, preorder_iter, postorder_iter, inorder_iter

root = Node(10)
b = Node(78, parent=root)
c = Node(2, parent=root)
d = Node(54, parent=b)
e = Node(9, parent=b)
f = Node(1, parent=c)
g = Node(3, parent=c)

root.show()
# 10
# ├── 78
# │   ├── 54
# │   └── 9
# └── 2
#     ├── 1
#     └── 3

preorder = [node.name for node in preorder_iter(root)]
postorder = [node.name for node in postorder_iter(root)]

print(preorder) # [10, 78, 54, 9, 2, 1, 3]
print(postorder) # [54, 9, 78, 1, 3, 2, 10]
