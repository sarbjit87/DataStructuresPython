# Queue : A queue is a collection of objects in which elements are added/deleted based on the principle of FIFO (First In 
# First Out)
# Queue ADT :-
# Q.enqueue(e) : Add an element to the end
# Q.dequeue()  : Remove and return the first element, an error will be reported if empty
# Q._front()   : Returns the first element without removing it, an error will be reported if empty
# Q.isEmpty()  : Returns True if the Queue is empty
# Q.isFull()   : Returns True if the Queue is full
# Q.size()     : Returns the length of Queue
#
# Implementation :
# Queue will be implemented using Lists (circular arrays), where we assume that the Queue is of fixed size N

class FullQueueException(Exception):
    pass

class EmptyQueueException(Exception):
    pass

class Queue(object):
    def __init__(self,N=10):
        self.N = N  # Default size of queue = 10
        self._A = [None] * self.N
        self._front = -1
        self._rear = -1

    def isEmpty(self):
        if (self._front == -1) and (self._rear == -1):
            return True
        else:
            return False

    def isFull(self):
        return ((self._rear + 1) % self.N) == self._front

    def enqueue(self,e):
        if self.isEmpty():
            self._front = 0
            self._rear = 0
        elif self.isFull():
            raise FullQueueException('Queue is full')
        else:
            self._rear = (self._rear+1) % self.N
        self._A[self._rear] = e

    def dequeue(self):
        if self.isEmpty():
            raise EmptyQueueException('Queue is empty')
        elif (self._front == self._rear):
            self._A[self._front] = None # Don't care about the data but this is for garbage collector 
            self._front = -1
            self._rear = -1
        else:
            self._A[self._front] = None # Don't care about the data but this is for garbage collector
            self._front = (self._front+1) % self.N
    
    def size(self):
        if self.isEmpty():
            return 0
        return ((self.N - self._front + self._rear) % self.N) + 1

    def front(self):
        if self.isEmpty():
            raise EmptyQueueException('Queue is empty')
        return self._A[self._front]
