"""
@property tutorial
"""
from typing import Any, Callable, Union
from base import BaseLinkedList
from node import Node


class SinglyLinkedList(BaseLinkedList):
    """Implements a Singly Linked List"""

    def __init__(self, head=None, tail=None):
        self._head = head
        self._tail = tail
        self._size = 0

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, new_size):
        if not isinstance(new_size, int):
            raise ValueError('List size must be int')
        if new_size < 0:
            raise ValueError('List size cannot be negative')
        self._size = new_size

    @property
    def head(self):
        """returns the head of the linked list"""
        return self._head

    @head.setter
    def head(self, node: Union[Node, None]):
        """Sets the head of the linked list"""
        if node is not None and not isinstance(node, Node):
            raise TypeError("Node must be of type None or Node")
        else:
            self._head = node

    @property
    def tail(self):
        """returns the tail of the linked list"""
        return self._tail

    @tail.setter
    def tail(self, node: Union[Node, None]):
        """Sets the tail of the list"""
        if node is not None and not isinstance(node, Node):
            raise TypeError("Node must be of type None or Node")
        elif self.head is not None and node is None:
            raise ValueError("Tail cannot be none if head is not none")
        else:
            self._tail = node

    def append(self, val: Any) -> None:
        """Append a new node with given value to end of list"""
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next_node = Node(val)
            self.tail = self.tail.next_node
        self.size += 1

    def appendleft(self):
        raise NotImplementedError

    def __len__(self) -> int:
        return self._size

    def accepts(*types):
        def check_accepts(f):
            assert len(types) == f.__code__.co_argcount

            def new_f(*args, **kwds):
                for (a, t) in zip(args, types):
                    assert isinstance(a, t), \
                        "arg %r does not match %s" % (a, t)
                return f(*args, **kwds)
            new_f.__name__ = f.__name__
            return new_f
        return check_accepts

    def handle_index(func) -> Callable:
        """Makes sure the indexes are valid are of type int"""

        def new_func(self, *args):
            index = args[0]
            if not isinstance(index, (int, slice)):
                return TypeError(
                    f'list indices must be integers or slices and not {type(args)}'
                )
            if isinstance(index, slice):
                raise NotImplementedError('Slicing is not implemented yet!')
            if self.head is None:
                raise IndexError('Index out of range. List Empty')
            if index < -self.size or index >= self.size:
                raise IndexError('List assignmnent out of range')
            return func(self, *args)
        return new_func

    @handle_index
    def __setitem__(self, index: int, value: Any) -> None:
        if isinstance(index, slice):
            raise NotImplementedError('Slicing is not implemented yet!')
        else:
            if index < 0:
                index += self.size
            node = self.head
            for i in range(index):
                node = node.next_node
            node.val = value

    @handle_index
    def __getitem__(self, index: int) -> Any:
        if isinstance(index, slice):
            raise NotImplementedError
        else:
            if index < 0:
                index += self.size
            node = self.head
            for i in range(index):
                node = node.next_node
            return node.val

    def __iter__(self):
        raise NotImplementedError

    def pop(self, index=-1) -> Any:
        """Removes the node at the end of the list
        and returns it's value
        """

        if index < 0:
            index += self.size

        if index == 0:
            node = self.head
            self.head = self.head.next_node
            self.size -= 1
            return node.val

        reset_tail = index == self.size-1

        prev = Node(0, self.head)
        node = self.head.next_node

        for i in range(index):
            prev = prev.next_node
            node = node.next_node

        removed = prev.next_node
        prev.next_node = node

        if reset_tail:
            self.tail = prev
        
        prev = prev.next_node
        self.size -= 1
        return removed.val

    def remove(self, value) -> None:
        raise NotImplementedError

    def sort(self):
        """Sorts the linked list in ascending order"""
        raise NotImplementedError

    def __repr__(self) -> str:
        out = ""
        node = self.head
        while node:
            out += str(node.val) + '->'
            node = node.next_node
        return out + 'None'
