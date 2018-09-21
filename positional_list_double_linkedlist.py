# Positional ADT :
# Unlike Stacks and Queues, where the elements can be either inserted/deleted at front/end;
# Positional List ADT allows to identify a location of an element. 
# A position 'p' is unaffected by any other changes in the list except if the element itself is deleted.
# Example : cursor in the text editors
#
# Methods :
# p.element()       : Returns the element stored at position p
# L.first()         : Return the position of first element of L or None if L is empty
# L.last()          : Return the position of last element of L or None if L is empty
# L.before(p)       : Return the position of L immediately before position p, None if p is the first element
# L.after(p)        : Return the position of L immediately after position p, None if p is the first element
# L.isEmpty()       : Return True if L is empty
# L.size()          : Return the number of elements in L
# L.add_first(e)    : Insert a new element e at the front of L, return the position of new element
# L.last(e)         : Insert a new element e at the end of L, return the position of new element
# L.add_before(p,e) : Insert a new element just before position p in L, return the position of new element
# L.add_after(p,e)  : Insert a new element just after position p in L, return the position of new element
# L.replace(p,e)    : Replace the element at position p, return the older element
# L.delete(p)       : Delete the element at position p

class _DoublyLinkedBase:
    class _Node:
        __slots__ = '_element' , '_prev', '_next'
        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next
    
    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element 
        node._prev = node._next = node._element = None 
        return element

class PositionalList(_DoublyLinkedBase):
    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not (self == other)


 #------------------------------- utility method -------------------------------
    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError( 'p must be proper Position type' )
        if p._container is not self:
            raise ValueError( 'p does not belong to this container' )
        if p._node._next is None: # convention for deprecated nodes
            raise ValueError( 'p is no longer valid' )
        return p._node

    def _make_position(self, node):
        if node is self._header or node is self._trailer:
            return None # boundary violation
        else:
            return self.Position(self, node) # legitimate position

 #------------------------------- accessors -------------------------------
    def first(self):
        return self._make_position(self._header._next)

    def last(self):
        return self._make_position(self._trailer._prev)

    def before(self, p):
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        cursor = self.first( )
        while cursor is not None:
            yield cursor.element( )
            cursor = self.after(cursor)

 #------------------------------- mutators -------------------------------
 # override inherited version to return Position, rather than Node

    def _insert_between(self, e, predecessor, successor):
        node = self._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        original = self._validate(p)
        return self._delete_node(original) # inherited method returns element

    def replace(self, p, e):
        original = self._validate(p)
        old_value = original._element # temporarily store old element
        original._element = e # replace with new element
        return old_value # return the old element value

L = PositionalList()
print L.add_first('A')
print L