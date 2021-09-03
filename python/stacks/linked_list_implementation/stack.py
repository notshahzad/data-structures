first = None
Last = None


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


def Push(data):
    global first, Last
    if first == None:
        first = Last = Node(data)
    else:
        new = Node(data)
        Last.next = new
        new.previous = Last
        Last = new


def PrintLinkedList():
    i = first
    while 1:
        print(i.data)
        if i == Last:
            break

        i = i.next


def Pop():
    global Last
    Last = Last.previous
    Last.next = None


while 1:
    choice = input('press i to push, r to pop, and p to print:')
    if choice == 'i':
        Push(input('enter the element to push:'))
    elif choice == 'r':
        Pop()
    elif choice == 'p':
        PrintLinkedList()
