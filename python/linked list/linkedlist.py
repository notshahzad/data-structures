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
    i = first
    while 1:
        print(i.element)
        if i==last:
            break
        i = i.pointer
while 1:
    choice = input('press i for insertion and p for print.\n')
    if choice.lower() == 'i':
        CreateLinkedList(input('enter element :'))
    elif choice.lower() == 'p':
        PrintLinkedList()