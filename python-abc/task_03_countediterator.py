#!/usr/bin/env python3
"""CountedIterator class."""


class CountedIterator:
    """CountedIterator class."""

    def __init__(self, data):
        """Initialize data and counter."""
        self.data = data
        self.counter = 0

    def __iter__(self):
        """Return self."""
        return self

    def __next__(self):
        """Return next item or raise StopIteration."""
        if self.counter < len(self.data):
            item = self.data[self.counter]
            self.counter += 1
            return item
        raise StopIteration

    def get_count(self):
        """Return number of items iterated."""
        return self.counter
