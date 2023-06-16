# Tree implementation 

class Node:
    # Tree Node structure
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def depth(root):
    current_depth = 0

    if root.left:
        current_depth = max(current_depth, depth(root.left))

    if root.right:
        current_depth = max(current_depth, depth(root.right))

    return current_depth + 1


# Inorder Traversal : left --> root --> right
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data)
        inorder(node.right)

# Preorder Traversal : root --> left --> right
def preorder(node):
    if node:
        print(node.data)
        preorder(node.left)
        preorder(node.right)

# Postorder Traversal : left --> right --> root
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data)

# Checking if is Full Binary Tree
def isFullTree(root):

    # An empty tree is Full
    if root is None:
        return True
    
    if root.left is None and root.right is None:
        return True
    
    if root.left is not None and root.right is not None:
        return (isFullTree(root.left) and isFullTree(root.right))
    
    return False

# Checking if is Perfect Binary Tree
def isPerfectTree(root, depth, level=0):

    # An empty tree is Perfect
    if root is None:
        return True
    
    if root.left is None and root.right is None:
        return(depth == level + 1)
    
    if root.left is None or root.right is None:
        return False
    
    return (isPerfectTree(root.left, depth, level + 1) and 
                isPerfectTree(root.right, depth, level + 1))

root = Node(10)
root.left = Node(78)
root.right = Node(2)
root.left.left = Node(54)
root.left.right = Node(9)
root.right.left = Node(1)
root.right.right = Node(3)

if isFullTree(root):
    print('This is a Full Binary Tree')
else:
    print('This is not a Binary Full Tree')

if isPerfectTree(root, depth(root)):
    print('This is a Perfect Binary Tree')
else:
    print('This is not a Perfect Binary Tree')


# Tree Implementation with BigTree package
# Run 'pip install bigtree' to install the package

from bigtree import Node, preorder_iter, postorder_iter

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