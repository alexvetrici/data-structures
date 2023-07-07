# Tree properties implementation

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

def node_count(root):
    if root is None:
        return 0
    return 1 + node_count(root.left) + node_count(root.right)


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
    
    return (isPerfectTree(root.left, depth, level + 1) 
                and isPerfectTree(root.right, depth, level + 1))

# Check if is Complete Binary Tree
def isCompleteTree(root):
    if root is None:
        return True
    
    queue = [root]
    found_null = False

    while queue:
        node = queue.pop(0)
        
        # Check if a non-null node has been found after a null node
        if node is None:
            found_null = True
        else:
            # If a null node has been found previously, tree is not complete
            if found_null:
                return False
            
            queue.append(node.left)
            queue.append(node.right)
    
    return True



# Tree construction
root = Node(10)                         # 10
root.left = Node(78)                    # ├── 78
root.right = Node(2)                    # │   ├── 54
root.left.left = Node(54)               # │   └── 9
root.left.right = Node(9)               # └── 2
root.right.left = Node(1)               #     ├── 1
root.right.right = Node(3)              #     └── 3

rootIndex = 0

# Check Tree properties

if isFullTree(root):
    print('This is a Full Binary Tree')
else:
    print('This is not a Binary Full Tree')


if isPerfectTree(root, depth(root)):
    print('This is a Perfect Binary Tree')
else:
    print('This is not a Perfect Binary Tree')


if isCompleteTree(root):
    print("This is a Complete Binary Tree")
else:
    print("This is not a Complete Binary Tree")
