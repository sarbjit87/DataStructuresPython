# Tree Abstract Data Type:
#
# A Tree is a non linear data structure that stores the elements (or nodes) hierarchically. 
# Each element (or node) in a Tree has a parent element (Except the root element) and zero or more children elements.
# Two nodes that are children of same parent are siblings.
# A node is an external node if it has no children. External nodes are also known as leafs.
# A node is an internal node if it has one or more children.
# An edge of tree T is a pair of nodes (u,v) such that u is parent of v or vice-versa.
# A path of tree T is a sequence of nodes such that any two consecutive nodes in the sequence forms an edge.
# An ordered tree contains nodes which can be ordered according to a specific criteria.
# If we can go from A to B, then
# - A is the ancestor of B
# - B is the descendent of A
#
# Properties of Trees:
# Trees are recursive data structures i.e. a root element can contain links to sub-trees
# Tree with N nodes will have N-1 edges/links
#
# DEPTH of Node (x): Number of edges in path from root to x. 
# Another definition : Depth of p is number of ancestors of p, excluding p itself.

# HEIGHT of Node (x): Number of edges in longest path from x to leaf.
# Height of Tree is same as Height of Root Node.

# BINARY TREES: 
# Binary Tree is an ordered tree that has the following properties :-
# - Each Node will have at-most two children only (it can have one child)
# - Each child node is labelled as either left-node or right-node
# - Left-Child precedes over Right-Child in order of children of node
# A Binary Tree is Proper/Strict if each node has zero or two children

# COMPLETE BINARY TREE:
# All levels are completely filled i.e. have two children EXCEPT the last level and all nodes are are as left as possible

# PERFECT BINARY TREE:
# All levels are completely filled

# Properties of Binary Trees:
# Maximum number of nodes at level i is 2's power i
# Maximum number of nodes in a tree with height h is "2 (power : h+1) - 1"

# ARRAY Based Implementation for Binary Trees
#An alternative representation of a binary tree T is based on a way of numbering the
#positions of T. For every position p of T, let f (p) be the integer defined as follows.
#• If p is the root of T, then f (p) = 0.
#• If p is the left child of position q, then f (p) = 2 f (q)+1.
#• If p is the right child of position q, then f (p) = 2 f (q)+2.
#The numbering function f is known as a level numbering of the positions in a
#binary tree T, for it numbers the positions on each level of T in increasing order
#from left to right

class Tree(object):
    """Abstract Base Class for Tree Data Structure"""

    class Position(object):
        """Nested Class used for storing the location of single element"""
        def element(self):
            """Return the element stored at a particular position"""
            raise NotImplementedError('Needs to be implemented by sub-class')

        def __eq__(self,other):
            """Return True if other Position represents the same location"""
            raise NotImplementedError('Needs to be implemented by sub-class')

        def __ne__(self,other):
            """Return True if other Position does NOT represents the same location"""
            return not(self==other)

    def root(self):
        """Returns the position of Root element of Tree or None if empty"""
        raise NotImplementedError('Needs to be implemented by sub-class')

    def parent(self,p):
        """Returns the position of Parent element of node or None if it is the root node"""
        raise NotImplementedError('Needs to be implemented by sub-class')

    def num_children(self,p):
        """Returns the Number of Children nodes for node represented by position p"""
        raise NotImplementedError('Needs to be implemented by sub-class')

    def children(self,p):
        """Returns the iterator of Positions for node P's children"""
        raise NotImplementedError('Needs to be implemented by sub-class')

    def __len__(self):
         """Returns the number of elements in Tree"""
         raise NotImplementedError('Needs to be implemented by sub-class')

    def is_root(self,p):
        """Returns True if position p is the root node's position"""
        return (self.root() == p)

    def is_leaf(self,p):
        """Returns True if position p of node is the leaf node"""
        return (self.num_children(p) == 0)

    def is_empty(self):
        """Returns True if Tree is empty"""
        return len(self) == 0

    def depth(self,p):
        """Returns the depth of node represented by position p"""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height(self,p):
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height(c) for c in self.children(p))

    def height(self,p=None):
        """Returns the height of node represented by position p or for tree if p is not provided"""
        if p is None:
            return self._height(self.root())
        else:
            return self._height(p)



class BinaryTree(Tree):
    def right(self,p):
        """Returns the position p's right child"""
        raise NotImplementedError('Needs to be implemented by sub-class') 
    
    def left(self,p):
        """Returns the position p's left child"""
        raise NotImplementedError('Needs to be implemented by sub-class')

    def sibling(self,p):
        """Returns the position of sibling of node represented by position p, return None if no sibling"""
        parent = self.parent(p)
        if parent is None or self.is_root(p):
            return None
        if p == self.left(parent):
            return self.right(parent)
        elif p == self.right(parent):
            return self.left(parent)

    def children(self,p):
        """Returns the position iterator of the child's for node represented by position p"""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

class LinkedBinaryTree(BinaryTree):
    
    class _Node:
        def __init__(self,element,parent=None,left=None,right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right
        
    class Position(BinaryTree.Position):
        def __init__(self,container,node):
            self._node = node
            self._container = container
        
        def element(self):
            """Return the element stored at this Position"""
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same location"""
            return type(other) is type(self) and other._node is self._node

    def _validate(self, p):
        """Return associated node, if position is valid"""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node (or None if no node)"""
        return self.Position(self, node) if node is not None else None

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def root(self):
        """Return the root Position of the tree (or None if tree is empty)"""
        return self._make_position(self._root)

    def parent(self,p):
        """Return the Position of p's parent (or None if p is root)"""
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self,p):
        """Return the Position of p's left child (or None if p is root)"""
        node = self._validate(p)
        return self._make_position(node._left)
    
    def right(self,p):
        """Return the Position of p's right child (or None if p is root)"""
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    def _add_root(self,e):
        """Place element e at the root of an empty tree and return new Position"""
        if self._root is not None:
            raise ValueError('Root is not Empty')
        self._root = self._Node(e)
        self._size = 1
        return self._make_position(self._root)

    def _add_left(self,p,e):
        """Create a new left child for Position p, storing element e.
        Return the Position of new node.
        Raise ValueError if Position p is invalid or p already has a left child"""
        node = self._validate(p)
        if node._left is not None:
            raise ValueError('Left Child already exists')
        node._left = self._Node(e,parent=node)
        self._size += 1
        return self._make_position(node._left)


    def _add_right(self,p,e):
        """Create a new right child for Position p, storing element e.
        Return the Position of new node.
        Raise ValueError if Position p is invalid or p already has a right child"""
        node = self._validate(p)
        if node._right is not None:
            raise ValueError('Right Child already exists')
        node._right = self._Node(e,parent=node)
        self._size += 1
        return self._make_position(node._right)

    def _replace(self,p,e):
        """Replace the element at position p with e, and return old element"""
        node = self._validate(p)
        oldValue = node._element
        node._element = e
        return oldValue

    def _delete(self, p):
        """Delete the node at Position p, and replace it with its child, if any.
        Return the element that had been stored at Position p.
        Raise ValueError if Position p is invalid or p has two children."""
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError('Position p has two childs')

        if node._left is not None:
            child = node._left
        else:
            child = node._right
        
        if child is not None:
            child._parent = node._parent

        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node #Depreciated node
        return node._element

    def _attach(self, p, t1, t2):
        """Attach trees t1 and t2 as left and right subtrees of external p"""
        node = self._validate(p)
        if not self.is_leaf(p): raise ValueError('position must be leaf')
        if not type(self) is type(t1) is type(t2): # all 3 trees must be same type
            raise TypeError('Tree types must match')
        self._size += len(t1) + len(t2)
        if not t1.is_empty(): # attached t1 as left subtree of node
            t1._root._parent = node
            node._left = t1._root
            t1._size = 0
        if not t2.is_empty( ): # attached t2 as right subtree of node
            t2._root._parent = node
            node._right = t2._root
            t2._root = None # set t2 instance to empty
            t2._size = 0

x = LinkedBinaryTree()
y = x._add_root(5)

print x.root().element()
print y.element()
