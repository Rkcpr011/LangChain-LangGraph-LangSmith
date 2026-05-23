
# Binary search tree
# Node creation 
# Insert function and the dry run to insert element [20,15,10,12,8,44,32]

# Define the node structure
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# show method is just for displaying the tree in sorted order
    def show(self):
        if self.left:
            self.left.show()
        if self.right:
            self.right.show()
        print(self.data)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# insert the element in tree
def insert(root, value):
    # If tree is empty, create a new node
    if root is None:
        return Node(value)
    # If smaller, go left
    if value < root.data:
        root.left = insert(root.left, value)
    # If greater, go right
    elif value > root.data:
        root.right = insert(root.right, value)
    # Return unchanged node pointer
    return root
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# get the height of the tree
def height(root):
    if root is None:
        return -1
    left_height = height(root.left)
    right_height = height(root.right)
    return 1 + max(left_height, right_height)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
root = None
for val in [20, 15, 10, 12, 8, 44, 32]:
    root = insert(root, val)
root.show()
print("Height of tree:", height(root))





