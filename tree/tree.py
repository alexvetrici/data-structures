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


#Tree implementation from scratch

class Node:
    # Tree Node structure
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Tree construction
root = Node(10)                         # 10
root.left = Node(78)                    # ├── 78
root.right = Node(2)                    # │   ├── 54
root.left.left = Node(54)               # │   └── 9
root.left.right = Node(9)               # └── 2
root.right.left = Node(1)               #     ├── 1
root.right.right = Node(3)              #     └── 3