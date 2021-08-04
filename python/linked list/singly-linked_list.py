first = None
last = None
class Node():
    def __init__(self,element):
        self.element = element
        self.pointer = None
def CreateLinkedList(element):
    global first, last
    if first == None:
        first = last = Node(element)
    else:
        new = Node(element)
        last.pointer = new
        last = new
def PrintLinkedList():
    print('-'*69)
    node = first
    while 1:
        print(node.element)
        if node==last:
            break
        node = node.pointer
    print('-'*69)
def InsertElement(position,element):
    i=0
    node = first
    while i<position:
        if i==position-1:
            new = Node(element)
            new.pointer =node.pointer
            node.pointer = new
            node = new
        node = node.pointer
        i+=1
while 1:
    choice = input('press c to create, i to insert and p for print.\n')
    if choice.lower() == 'c':
        CreateLinkedList(input('enter element :'))
    elif choice.lower() == 'i':
        InsertElement(int(input('enter position:')),input('input element'))
    elif choice.lower() == 'p':
        PrintLinkedList()