class node:
    def __init__(self):
        self.data = None
        self.right = None
        self.left = None


class tree:
    def __init__(self):
        self.root = None
        self.queue = []

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

    def BreathFirstTraverse(self, root):
        self.AppendChildren(root)
        while len(self.queue) != 0:
            temp = self.queue.pop(0)
            print(temp.data)
            if temp.left != None:
                self.AppendChildren(temp.left)
            if temp.right != None:
                self.AppendChildren(temp.right)

    def AppendChildren(self, address):
        self.queue.append(address)

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
t.BreathFirstTraverse(t.root)
