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

    def Traverse(self, root):
        if root.left != None:
            self.Traverse(root.left)
        print(root.data)
        if root.right != None:
            self.Traverse(root.right)

    def FindElement(self, element):
        i = root
        while(1):
            if i == None:
                print(f"{element} not present in tree")
                break
            if i.data == element:
                print(f"{element} present in the tree")
                break
            if i.data > element:
                i = i.left
            else:
                i = i.right


tree().CreateNode(1)
tree().CreateNode(5)
tree().CreateNode(2)
tree().CreateNode(3)
tree().CreateNode(6)
tree().CreateNode(4)
tree().Traverse(root)
tree().FindElement(6)
tree().FindElement(727)
