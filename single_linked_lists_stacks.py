# Stack ADT implementation using Lists
# S.push(e)    : Add element 'e' to the top of Stack S
# S.pop()      : Remove element from the top of Stack S and return the removed element, error if empty
# S.top()      : Return the reference of the top element of S without removing it, error if empty
# S.isEmpty() : Return True if stack is empty
# len(S)       : Return number of elements in Stack S

class EmptyStackException(Exception):
    pass

class Node(object):
    __slot__ = "data", "next"
    def __init__(self,data,next):
        self.data = data
        self.next = next

class Stack(object):
    def __init__(self):
        self.head = None
        self.size = 0
    
    def __len__(self):
        return self.size

    def isEmpty(self):
        return self.size == 0
    
    def push(self,elem):
        self.head = Node(elem,self.head)
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise EmptyStackException("No Elements in Stack")
        retNodeData= self.head.data
        self.head = self.head.next
        self.size -= 1
        return retNodeData

    def top(self):
        if self.isEmpty():
            raise EmptyStackException("No Elements in Stack")
        retNodeData= self.head.data
        return retNodeData
