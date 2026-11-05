
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.data:
            root.left = self.insert(root.left, key)
        elif key > root.data:
            root.right = self.insert(root.right, key)
        return root

    def search(self, root, key):
        if root is None or root.data == key:
            return root
        if key < root.data:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def delete(self, root, key):
        if root is None:
            return root

        if key < root.data:
            root.left = self.delete(root.left, key)
        elif key > root.data:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            temp = root.right
            while temp.left:
                temp = temp.left

            root.data = temp.data
            root.right = self.delete(root.right, temp.data)

        return root

    def display(self, root):
        if root:
            self.display(root.left)
            print(root.data, end=" ")
            self.display(root.right)


b = BST()
root = None

for x in [50, 30, 70, 20, 40, 60, 80]:
    root = b.insert(root, x)

print("BST Elements:")
b.display(root)

key = 40
if b.search(root, key):
    print("\nElement Found:", key)
else:
    print("\nElement Not Found")

root = b.delete(root, 30)

print("After Deletion:")
b.display(root)
