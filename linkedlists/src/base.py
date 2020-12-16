"""Base class for Node and LinkedLists"""

class BaseLinkedList:
    def __init__(self):
        pass

class BaseNode:
    def __init__(self, val=0, next=None):
        self._val = val
        self._next = next
    
    def __repr__(self):
        return f"Node({self.val, self._next})"