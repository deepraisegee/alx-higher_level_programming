#!/usr/bin/python3

"""MyList that inherits from list"""


class MyList(list):
    """MyList class, subclass of list"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        data = self.copy()
        data.sort()
        print(data)
