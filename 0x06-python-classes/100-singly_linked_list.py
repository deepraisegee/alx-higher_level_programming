#!/use/bin/python3
"""
A file that defines a node of a singly linked list
"""


class Node:
    """A node class for single linked list"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None:
            if not isinstance(value, self.__class__):
                raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A class for SinglyLinkedList"""

    def __init__(self):
        self.__nodes = []
        self.__head = self.__nodes[0]

    def __repr__(self):
        return f"{[node of node in self.nodes]}"
