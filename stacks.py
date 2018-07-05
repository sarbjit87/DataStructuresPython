# Stack ADT implementation using Lists
# S.push(e)    : Add element 'e' to the top of Stack S
# S.pop()      : Remove element from the top of Stack S and return the removed element, error if empty
# S.top()      : Return the reference of the top element of S without removing it, error if empty
# S.isEmpty() : Return True if stack is empty
# len(S)       : Return number of elements in Stack S
 
class EmptyStackException(Exception):
    pass

class StacksList(object):
    def __init__(self):
        self._data = []

    def push(self,e):
        self._data.append(e)

    def pop(self):
        if self.isEmpty():
            raise EmptyStackException("No Elements in Stack")
        return self._data.pop()

    def top(self):
        if self.isEmpty():
            raise EmptyStackException("No Elements in Stack")
        return self._data[-1]
    
    def isEmpty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)

