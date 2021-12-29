class node:
    def __init__(self):
        self.data = None
        self.right = None
        self.left = None


class tree:
    def __init__(self):
        self.root = None
        self.height = None

    def CreateNode(self, data):
        if self.root == None:
            self.root = node()
            self.root.data = data
            self.height = 0
            return
        i = self.root
        while 1:
            if self.root == None:
                self.root = node()
                self.root.data = data
                if temp.data > data:
                    temp.left = self.root
                else:
                    temp.right = self.root
                self.root = i
                self.CalcHeight(self.root, 0)
                return
            elif self.root.data > data:
                temp = self.root
                self.root = self.root.left
            elif self.root.data < data:
                temp = self.root
                self.root = self.root.right

    def Traverse(self, root):
        if root.left != None:
            self.Traverse(root.left)
        print(root.data)
        if root.right != None:
            self.Traverse(root.right)

    def CalcHeight(self, root, depth):
        if root.left != None:
            self.CalcHeight(root.left, depth + 1)
        if depth > self.height:
            self.height = depth
        if root.right != None:
            self.CalcHeight(root.right, depth + 1)

    def FindElement(self, element):
        i = self.root
        while 1:
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


t = tree()
t.CreateNode(6)
t.CreateNode(5)
t.CreateNode(9)
t.CreateNode(2)
t.CreateNode(7)
t.CreateNode(10)
t.CreateNode(1)
t.CreateNode(4)
t.CreateNode(8)
t.CreateNode(3)
t.Traverse(t.root)
print(f"height of tree is : {t.height}")
