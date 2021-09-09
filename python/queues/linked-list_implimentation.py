first = None
last = None


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


def enqueue(element):
    global first, last
    if first == None:
        first = last = Node(element)
    else:
        new = Node(element)
        last.next = new
        last = new


def dequeue():
    global first, last
    if first == last:
        first = last = None
    else:
        first = first.next


def PrintQueue():
    global first
    if first == None:
        print('Queue is empty')
    else:
        i = first
        while 1:
            print(i.data)
            if i == last:
                break
            i = i.next


enqueue(727)
enqueue('wysi')
enqueue('yeheboai')
PrintQueue()
dequeue()
dequeue()
PrintQueue()
