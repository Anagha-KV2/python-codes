class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def invertTree(root):
    if root is None:
        return None

    # Swap left and right children
    root.left, root.right = root.right, root.left

    # Recursively invert subtrees
    invertTree(root.left)
    invertTree(root.right)

    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Example Tree
root = Node(4)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(9)

print("Inorder before inversion:")
inorder(root)

invertTree(root)

print("\nInorder after inversion:")
inorder(root)