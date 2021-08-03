first = None
last = None
class Node():
    def __init__(self,element):
        self.element = element
        self.pointer = None
def createNode(element):
    global first, last
    if first == None:
        last = first = Node(element)
    else:
        new = Node(element)
        last.pointer = new
        last = new
    
def PrintLinkedList():
    i = first
    while 1:
        print(i.element)
        if i == last:
            break
        i = i.pointer
while 1:
    print('press i to insert and p to print')
    choice = input().lower()
    if choice == 'i':
        createNode(input())
    elif choice == 'p':
        PrintLinkedList()