class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # Insert
    def insert(self, root, key):
        if root is None:
            return Node(key)

        if key < root.data:
            root.left = self.insert(root.left, key)
        elif key > root.data:
            root.right = self.insert(root.right, key)

        return root

    # Search
    def search(self, root, key):
        if root is None:
            return False

        if root.data == key:
            return True

        if key < root.data:
            return self.search(root.left, key)

        return self.search(root.right, key)

    # Preorder Traversal
    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def Inorder(self, root):
         if root:
            self.Inorder(root.left)
            print(root.data, end=" ")

        
            self.Inorder(root.right)
    def postorder(self, root):
         if root:
            self.postorder(root.left)

            self.postorder(root.right)
            print(root.data, end=" ")

   def find_min(self, root):
        while root.left:
         root = root.left
         return root

   def find_max(self, root):
         while root.right:
         root = root.right
        return root




# Create BST
bst = BST()

values = [13,6,9,4,7,10,20,15]

for value in values:
    bst.root = bst.insert(bst.root, value)
print("Inorder Traversal:",end="")
bst.Inorder(bst.root)
print()


print("Preorder Traversal:",end="")
bst.preorder(bst.root)
print()

print("postorder Traversal:",end="")
bst.postorder(bst.root)
print()




