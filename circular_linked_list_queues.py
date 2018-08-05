# Queue : A queue is a collection of objects in which elements are added/deleted based on the principle of FIFO (First In 
# First Out)
# In Circular linked list, next pointer of tail of the linked list points back to head of the list. An example would be 
# round-robin scheduler where the first element is serviced and the elements are then rotated.
# Queue ADT :-
# Q.rotate() : Move the first element to the back
# Q.enqueue(e) : Add an element to the end
# Q.dequeue()  : Remove and return the first element, an error will be reported if empty
# Q.front()   : Returns the first element without removing it, an error will be reported if empty
# Q.isEmpty()  : Returns True if the Queue is empty
# Q.size()  : Returns the size of Queue

class EmptyQueueException(Exception):
    pass

class Node(object):
    __slot__ = "data", "next"
    def __init__(self,data,next):
        self.data = data
        self.next = next

class Queue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def size(self):
        return self._size

    def isEmpty(self):
        return self._size == 0
    
    def enqueue(self,e):
        if self._size == 0:
            node = Node(e,None)
            self.head = node
            self.tail = node
            self.tail.next = self.head
        else:
            node = Node(e,None)
            self.tail.next = node
            self.tail = node
            self.tail.next = self.head
        self._size += 1

    def dequeue(self):
        if self.isEmpty():
            raise EmptyQueueException("No Elements in Queue")

        if self._size == 1:
            retNodeData = self.head.data 
            self.head = None
            self.tail = None
        else:
            retNodeData = self.head.data
            self.head = self.head.next
            self.tail.next = self.head
        self._size -= 1
        return retNodeData

    def front(self):
        if self.isEmpty():
            raise EmptyQueueException("No Elements in Queue")
        retNodeData = self.head.data 
        return retNodeData

    def rotate(self):
        self.head = self.head.next
        self.tail = self.tail.next
    