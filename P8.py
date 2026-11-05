
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def construct(exp):
    stack = []

    for ch in reversed(exp):
        node = Node(ch)

        if ch in "+-*/":
            node.left = stack.pop()
            node.right = stack.pop()

        stack.append(node)

    return stack.pop()

def postorder(root):
    s1 = [root]
    s2 = []

    while s1:
        node = s1.pop()
        s2.append(node)

        if node.left:
            s1.append(node.left)
        if node.right:
            s1.append(node.right)

    while s2:
        print(s2.pop().data, end=" ")

def delete(root):
    if root is None:
        return

    root.left = None
    root.right = None
    root.data = None

exp = "+--a*bc/def"

root = construct(exp)

print("Postorder Traversal:")
postorder(root)

delete(root)
root = None

print("\nTree Deleted")
