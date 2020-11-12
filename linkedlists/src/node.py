from base import BaseNode

class Node(BaseNode):
    """Implements node of the liked list"""

    def __init__(self, val=0, next_node=None):
        self._val = val
        self._next_node = next_node

    @property
    def val(self):
        return self._val

    @property
    def next_node(self):
        return self._next_node

    @val.setter
    def val(self, val):
        self._val = val

    @next_node.setter
    def next_node(self, node):
        if node is not None and not isinstance(node, Node):
            raise TypeError(f'next_node must be of type Node or None')
        else:
            self._next_node = node

    def __repr__(self):
        return f"Node({self.val, self.next_node})"

if __name__ == '__main__':
    a = Node()