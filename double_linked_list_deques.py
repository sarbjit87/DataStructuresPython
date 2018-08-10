# Deque ADT :-
# D.add_first(e)   : Add an element e to the front of Deque
# D.add_last(e)    : Add an element e to the rear of Deque
# D.delete_first() : Remove and return the first element, error if empty
# D.delete_last()  : Remove and return the last element, error if empty
# D.first()        : Return the reference of the first element, error if empty
# D.last()         : Return the reference of the last element, error if empty
# D.isEmpty()      : Returns True if Deque is empty
# D.size()         : Returns the size of Deque

class EmptyDequeException(Exception):
    pass

class Node(object):
    __slot__ = "data", "next", "prev"
    def __init__(self,data,next,prev):
        self.data = data
        self.next = next
        self.prev = prev

class Deque(object):
    def __init__(self):
        self._size = 0
        self.head = Node(None,None,None)
        self.tail = Node(None,None,None)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def size(self):
        return self._size
    
    def isEmpty(self):
        return self._size == 0

    def first(self):
        if self.isEmpty():
            raise EmptyDequeException("Empty Deque")
        return self.head.next.data
    
    def last(self):
        if self.isEmpty():
            raise EmptyDequeException("Empty Deque")
        return self.tail.prev.data

    def add_first(self,e):
        node = Node(e,self.head.next,self.head)
        self.head.next.prev = node
        self.head.next = node
        self._size += 1
    
    def add_last(self,e):
        node = Node(e,self.tail,self.tail.prev)
        self.tail.prev.next = node
        self.tail.prev = node
        self._size += 1
    
    def delete_first(self):
        if self.isEmpty():
            raise EmptyDequeException("Empty Deque")
        node = self.head.next
        retData = node.data
        newNode = node.next
        self.head.next = newNode
        newNode.prev = self.head
        self._size -= 1
        return retData

    def delete_last(self):
        if self.isEmpty():
            raise EmptyDequeException("Empty Deque")
        node = self.tail.prev
        retData = node.data
        newNode = node.prev
        self.tail.prev = newNode
        newNode.next = self.tail
        self._size -= 1
        return retData