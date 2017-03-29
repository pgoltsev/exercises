import collections


class StackOverflow(Exception):
    pass


class StackIsEmpty(Exception):
    pass


class Stack(object):
    def __init__(self, size=-1):
        self._size = size
        self._store = collections.deque(
            maxlen=self._size if self._size > 0 else None
        )
        self._length = 0

    def peek(self):
        if self._length == 0:
            return None

        return self._store[self._length - 1]

    def pop(self):
        if self._length == 0:
            raise StackIsEmpty()

        self._length -= 1
        return self._store.pop()

    def push(self, item):
        if self._size > 0 and self._length == self._size:
            raise StackOverflow()

        self._store.append(item)
        self._length += 1

    @property
    def length(self):
        return self._length

    @property
    def size(self):
        return self._size

    def clear(self):
        self._store.clear()
        self._length = 0
