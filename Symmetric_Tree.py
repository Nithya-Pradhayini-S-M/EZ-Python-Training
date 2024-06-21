class Node:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None

    def isMirror(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        
        if root1 and root2 and root1.value == root2.value:
            return self.isMirror(root1.left, root2.right) and self.isMirror(root1.right, root2.left)
        
        return False

    def isSymmetric(self, root):
        return self.isMirror(root, root)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(4)
    root.right.right = Node(3)

    if root.isSymmetric(root):
        print("Symmetric")
    else:
        print("Not symmetric")
