class node:
    def __init__(self):
        self.data = None
        self.right = None
        self.left = None


class tree:
    def __init__(self):
        self.root = None

    def CreateNode(self, data):
        if self.root == None:
            self.root = node()
            self.root.data = data
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
                return
            elif self.root.data > data:
                temp = self.root
                self.root = self.root.left
            elif self.root.data < data:
                temp = self.root
                self.root = self.root.right

    def PreOrderTraverse(self, root):
        print(root.data, end=" ")
        if root.left != None:
            self.PreOrderTraverse(root.left)
        if root.right != None:
            self.PreOrderTraverse(root.right)

    def InOrderTraverse(self, root):
        if root.left != None:
            self.InOrderTraverse(root.left)
        print(root.data, end=" ")
        if root.right != None:
            self.InOrderTraverse(root.right)

    def PostOrderTraverse(self, root):
        if root.left != None:
            self.PostOrderTraverse(root.left)
        if root.right != None:
            self.PostOrderTraverse(root.right)
        print(root.data, end=" ")

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
t.InOrderTraverse(t.root)
print("\n")
t.PreOrderTraverse(t.root)
print("\n")
t.PostOrderTraverse(t.root)
print("\n")
