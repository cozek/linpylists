from base import BaseNode

class Node(BaseNode):
    """Implements node of the liked list"""

    def __init__(self, val=0, next=None):
        self._val = val
        self._next = next

    @property
    def val(self):
        return self._val

    @property
    def next(self):
        return self._next

    @val.setter
    def val(self, val):
        self._val = val

    @next.setter
    def next(self, node):
        if node is not None and not isinstance(node, Node):
            raise TypeError(f'next must be of type Node or None')
        else:
            self._next = node

    def __repr__(self):
        return f"Node({self.val, self.next})"

if __name__ == '__main__':
    a = Node()