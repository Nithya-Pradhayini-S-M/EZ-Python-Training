class Node:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None

    def preorder(self, root):
        # Preorder traversal: Root -> Left -> Right
        if root is None:
            return
        print(root.value)
        self.preorder(root.left)
        self.preorder(root.right)

    def Inorder(self, root):
        # Inorder traversal: Left -> Root -> Right
        if root is None:
            return
        self.Inorder(root.left)
        print(root.value)
        self.Inorder(root.right)

    def Postorder(self, root):
        # Postorder traversal: Left -> Right -> Root
        if root is None:
            return
        self.Postorder(root.left)
        self.Postorder(root.right)
        print(root.value)

    def Height(self, root):
        # Calculate the height of the tree
        if root is None:
            return 0
        LH = self.Height(root.left)
        RH = self.Height(root.right)
        return max(LH, RH) + 1

    @staticmethod
    def levelorder(root):
        # Level-order (BFS) traversal
        Q = [root]
        Q.append(None)

        while len(Q) > 0:
            curr = Q.pop(0)

            if curr is None:
                if len(Q) == 0:
                    break
                else:
                    print()
                    Q.append(None)
            else:
                print(curr.value, end=" ")
                if curr.left:
                    Q.append(curr.left)
                if curr.right:
                    Q.append(curr.right)

    def count_of_Nodes(self, root):
        # Count the total number of nodes in the tree
        if root is None:
            return 0
        Lcount = self.count_of_Nodes(root.left)
        Rcount = self.count_of_Nodes(root.right)
        return Lcount + Rcount + 1

    def Sum_of_Nodes(self, root):
        # Calculate the sum of all node values
        if root is None:
            return 0
        Lsum = self.Sum_of_Nodes(root.left)
        Rsum = self.Sum_of_Nodes(root.right)
        return Lsum + Rsum + root.value


if __name__ == "__main__":
    # Create a sample binary tree
    root=Node(1)

    root.left=Node(2)
    root.right=Node(3)

    root.left.left=Node(4)
    root.left.right=Node(5)

    root.right.left=Node(6)
    root.right.right=Node(7)

    root.left.right.left=Node(9)
    root.left.right.right=Node(10)

    root.right.right.right=Node(11)
    root.left.right.left.left=Node(12)
    root.left.right.left.right=Node(13)
    
   

    # Menu-driven options for tree traversal and other operations
    while True:
        print("\nMenu:")
        print("1. PreOrder")
        print("2. InOrder")
        print("3. PostOrder")
        print("4. LevelOrder or BFS")
        print("5. Height of Tree")
        print("6. Count of Nodes")
        print("7. Sum of Nodes")
        print("8. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            root.preorder(root)
        elif choice == 2:
            root.Inorder(root)
        elif choice == 3:
            root.Postorder(root)
        elif choice == 4:
             root.levelorder(root)
        elif choice == 5:
            res = root.Height(root)
            print("Height of the tree:", res)
        elif choice == 6:
            res = root.count_of_Nodes(root)
            print("Total number of nodes:", res)
        elif choice == 7:
            res = root.Sum_of_Nodes(root)
            print("Sum of all nodes:", res)
        elif choice == 8:
            break
        else:
            print("Invalid choice. Please try again.")
