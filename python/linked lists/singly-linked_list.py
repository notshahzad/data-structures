
first = None
last = None


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def createNode():
    global first, last
    if first == None:
        last = first = Node(input())
    else:
        new = Node(input())
        last.next = new
        last = new


def printlinkedList():
    i = first
    while True:
        print(i.data)
        if i == last:
            break
        i = i.next


while True:
    choice = int(input("1.insert \n2.dipslay\n"))
    if choice == 1:
        createNode()
    else:
        printlinkedList()
