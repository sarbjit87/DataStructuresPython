# Queue : A queue is a collection of objects in which elements are added/deleted based on the principle of FIFO (First In 
# First Out)
# Queue ADT :-
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
        else:
            node = Node(e,None)
            self.tail.next = node
            self.tail = node
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
        self._size -= 1
        return retNodeData

    def front(self):
        if self.isEmpty():
            raise EmptyQueueException("No Elements in Queue")
        retNodeData = self.head.data 
        return retNodeData