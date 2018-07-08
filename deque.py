# Deque :  Deque or Double-Ended Queue supports insertion or deletion at both front and rear 
# Deque ADT :-
# D.add_first(e)   : Add an element e to the front of Deque
# D.add_last(e)    : Add an element e to the rear of Deque
# D.delete_first() : Remove and return the first element, error if empty
# D.delete_last()  : Remove and return the last element, error if empty
# D.first()        : Return the reference of the first element, error if empty
# D.last()         : Return the reference of the last element, error if empty
# D.isEmpty()      : Returns True if Deque is empty
# D.size()         : Returns the size of Deque
 
# Implementation :
# Queue will be implemented using Lists (circular dynamic arrays) with default size of 10

class EmptyDequeException(Exception):
    pass

class Deque(object):
    def __init__(self,N=10):
        self._N = N
        self._A = [None]*self._N
        self._front = -1
        self._rear= -1

    def isEmpty(self):
        if (self._front == -1) and (self._rear == -1):
            return True
        return False

    def add_first(self,e):
        if self.size() == self._N:
            self._resize(self._N*2)
        if self.isEmpty():
            self._front = 0
            self._rear = 0
        else:
            self._front = (self._N + self._front - 1) % self._N
        self._A[self._front] = e

    def add_last(self,e):
        if self.size() == self._N:
            self._resize(self._N*2)
        if self.isEmpty():
            self._front = 0
            self._rear = 0
        else:
            self._rear = (self._N + self._rear + 1) % self._N
        self._A[self._rear] = e

    def delete_first(self):
        if self.isEmpty():
            raise EmptyDequeException("Empty Deque")
        elif self._rear == self._front:
            retElem = self._A[self._front]
            self._A[self._front] = None # Don't care about the data
            self._rear = -1
            self._front = -1
        else:
            retElem = self._A[self._front]
            self._A[self._front] = None # Don't care about the data 
            self._front = (self._front + 1) % self._N
        return retElem

    def delete_last(self):
        if self.isEmpty():
            raise EmptyDequeException("Empty Deque")
        elif self._rear == self._front:
            retElem = self._A[self._rear]
            self._A[self._rear] = None # Don't care about the data 
            self._rear = -1
            self._front = -1
        else:
            retElem = self._A[self._rear]
            self._A[self._rear] = None # Don't care about the data
            self._rear = (self._rear - 1) % self._N
        return retElem

    def first(self):
        if self.isEmpty():
            raise EmptyDequeException("Empty Deque")
        return self._A[self._front]

    def last(self):
        if self.isEmpty():
            raise EmptyDequeException("Empty Deque")
        return self._A[self._rear]

    def size(self):
        if self.isEmpty():
            return 0
        return ((self._N - self._front + self._rear) % self._N) + 1

    def _resize(self,newSize):
        A1 = self._A
        self._A = [None]*newSize
        k = self._front
        for i in range(self.size()):
            self._A[i] = A1[k]
            k = (k + 1)%self._N
        self._front = 0
        self._rear = k
        self._N = newSize



