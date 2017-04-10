class Node(object):
    def __init__(self, obj, next_node=None):
        self._obj = obj
        self._next = next_node

    @property
    def object(self):
        return self._obj

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, value):
        self._next = value

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.object)


class SinglyLinkedList(object):
    def __init__(self, nodes=None):
        super().__init__()
        self._first_node = None

        if nodes:
            prev_node = None
            for cur_node in nodes:
                if prev_node is not None:
                    prev_node.next = cur_node
                prev_node = cur_node

                if self._first_node is None:
                    self._first_node = cur_node

    @property
    def first_node(self):
        return self._first_node

    def insert_after(self, new_node, node=None):
        if node is None:
            new_node.next, self._first_node = self._first_node, new_node
        else:
            next_for_new_node = node.next
            node.next = new_node
            if new_node is not None:
                new_node.next = next_for_new_node

    def remove_after(self, node):
        if node is None:
            removing_node = self._first_node
            self._first_node = self._first_node.next
            return removing_node
        else:
            removing_node = node.next
            node.next = None if removing_node is None else removing_node.next
            return removing_node

    def __iter__(self):
        cur_node = self._first_node
        while cur_node is not None:
            yield cur_node
            cur_node = cur_node.next

    def clear(self):
        self._first_node = None

    @property
    def is_empty(self):
        return self._first_node is None

    def reverse(self):
        if self.is_empty:
            return

        cur_node = self._first_node
        next_node = cur_node.next
        while next_node is not None:
            next_next, next_node.next = next_node.next, cur_node
            cur_node, next_node = next_node, next_next

        self._first_node.next = None
        self._first_node = cur_node

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, list(self))
