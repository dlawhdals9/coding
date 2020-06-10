class Node:
    def __init__(self, data): # 생성자에서 root를 만든다.
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            #print("self.data :", self.data)
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

    # Inorder traversal
    # Left -> Root -> Right
    def inorder(self, root):
        res = []
        if root:
            res = self.inorder(root.left)
            res.append(root.data)
            #print(res)
            res = res + self.inorder(root.right)
        return res

    # Preorder traversal
    # Root -> Left ->Right
    def preorder(self, root):
        res = []
        if root:
            res.append(root.data)
            #print(res)
            res = res + self.preorder(root.left)
            res = res + self.preorder(root.right)
        return res   

    # Postorder traversal
    # Left ->Right -> Root
    def postorder(self, root):
        res = []
        if root:
            res = self.postorder(root.left)
            res = res + self.postorder(root.right)
            res.append(root.data)
            #print(res)
        return res

if __name__ == "__main__":
    root = Node(27)
    root.insert(14)
    root.insert(35)
    root.insert(10)
    root.insert(19)
    root.insert(31)
    root.insert(42)
    root.PrintTree()
    print("=========================================")
    print("InOrder   :", root.inorder(root))
    print("=========================================")
    print("PreOrder  :", root.preorder(root))
    print("=========================================")
    print("PostOrder :", root.postorder(root))
    print("=========================================")
