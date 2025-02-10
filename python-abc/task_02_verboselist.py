#!/usr/bin/env python3
"""Task 02: VerboseList"""


class VerboseList(list):
    """Extends list class"""
    def append(self, item):
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(len(iterable)))

    def remove(self, value):
        print("Removed [{}] from the list.".format(value))
        super().remove(value)

    def pop(self, index = -1):
        item = self[index] if index != -1 else self[-1]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
