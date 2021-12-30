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
                # self.CalcHeight(self.root, 0)
                return
            elif self.root.data > data:
                temp = self.root
                self.root = self.root.left
            elif self.root.data < data:
                temp = self.root
                self.root = self.root.right

    def AddNodeRecursive(self, el):
        self.CreateTreeNodeRecrsive(self.root, el)

    def CreateTreeNodeRecrsive(self, Node, el):
        if Node == None:
            Node = node()
            Node.data = el
            node.left = None
            node.right = None
            if self.root == None:
                self.root = Node
            return Node
        elif el < Node.data:
            n = self.CreateTreeNodeRecrsive(Node.left, el)
            if n != None:
                Node.left = n
        elif el > Node.data:
            n = self.CreateTreeNodeRecrsive(Node.right, el)
            if n != None:
                Node.right = n

    def Traverse(self, root):
        if root.left != None:
            self.Traverse(root.left)
        print(root.data)
        if root.right != None:
            self.Traverse(root.right)

    def CalcDepth(self, el):
        i = self.root
        depth = 0
        while 1:
            if i == None:
                print(f"{el} not present in tree")
                break
            if i.data == el:
                h = self.CalcHeight(i, 0)
                self.height = None
                print(f"depth : {depth}\nheight : {h}")
                return depth
            if i.data > el:
                depth += 1
                i = i.left
            else:
                depth += 1
                i = i.right

    def CalcHeight(self, el, depth):
        if el.left != None:
            self.CalcHeight(el.left, depth + 1)
        if depth > self.height:
            self.height = depth
        if el.right != None:
            self.CalcHeight(el.right, depth + 1)
        return self.height

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
t.AddNodeRecursive(69)
t.AddNodeRecursive(717)
t.AddNodeRecursive(13)
t.AddNodeRecursive(643)
t.AddNodeRecursive(625)
t.AddNodeRecursive(594)
t.AddNodeRecursive(245)
t.CreateNode(1)
t.Traverse(t.root)
