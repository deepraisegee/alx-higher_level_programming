#!/usr/bin/python3

"""Magic methods"""


class MyInt(int):
    """Sub class from int"""

    def __eq__(self, other):
        return self.real != other

    def __ne__(self, other):
        return self.real == other
