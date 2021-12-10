root = None


class tree:
    def __init__(self):
        self.data = None
        self.right = None
        self.left = None

    def CreateNode(self, data):
        global root
        if root == None:
            root = tree()
            root.data = data
            return
        i = root
        while(1):
            if root == None:
                root = tree()
                root.data = data
                if temp.data > data:
                    temp.left = root
                else:
                    temp.right = root
                root = i
                return
            elif root.data > data:
                temp = root
                root = root.left
            elif root.data < data:
                temp = root
                root = root.right

    def PrintTree(self, root):
        if root.left != None:
            self.PrintTree(root.left)
        print(root.data)
        if root.right != None:
            self.PrintTree(root.right)


tree().CreateNode(1)
tree().CreateNode(5)
tree().CreateNode(2)
tree().CreateNode(3)
tree().CreateNode(6)
tree().CreateNode(4)
tree().PrintTree(root)
