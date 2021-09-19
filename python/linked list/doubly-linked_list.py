first = None
last = None


class Node():
    def __init__(self, element):
        self.element = element
        self.next = None
        self.previous = None


def CreateLinkedList(element):
    global first, last
    if first == None:
        first = last = Node(element)
    else:
        new = Node(element)
        last.next = new
        new.previous = last
        last = new


def PrintLinkedList():
    print('-'*69)
    node = first
    while 1:
        print(node.element)
        if node == last:
            break
        node = node.next
    print('-'*69)


def Delete(position):
    global first, last
    i = first
    count = 0
    while 1:
        if count == position:
            if i != None:
                if i.next == None:
                    prev = i.previous
                    prev.next = i.next
                    last = prev
                    i.previous = None
                elif i.previous == None:
                    first = i.next
                    i.next = None
                    first.previous = None
                else:
                    prev = i.previous
                    nxt = i.next
                    prev.next = nxt
                    nxt.previous = prev
                break
        i = i.next
        count += 1


def Insert(position, element):
    global first, last
    i = first
    count = 0
    while 1:
        if count == position:
            if i != None:
                if i.previous == None:
                    new = Node(element)
                    new.next = first
                    first.previous = new
                    first = new
                else:
                    new = Node(element)
                    prev = i.previous
                    prev.next = new
                    new.next = i
                    new.previous = prev
                    i.previous = new

            else:
                CreateLinkedList(element)
            break
        i = i.next
        count += 1


CreateLinkedList(1)
CreateLinkedList(2)
CreateLinkedList(3)
CreateLinkedList(4)
CreateLinkedList(5)
Delete(4)
PrintLinkedList()
Insert(1, 69)
Delete(0)
PrintLinkedList()
