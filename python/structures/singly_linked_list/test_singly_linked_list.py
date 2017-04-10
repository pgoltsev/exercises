import unittest

from python.structures.singly_linked_list.singly_linked_list import Node, \
    SinglyLinkedList


class SinglyLinkedListTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.items = [
            'i%d' % item
            for item in range(5)
        ]

    def test_creation_from_list(self):
        linked_list = SinglyLinkedList(
            (Node(test_item) for test_item in self.items)
        )

        self.assertListEqual(
            self.items,
            [
                item.object
                for item in linked_list
            ]
        )

    def test_is_empty_and_clear(self):
        linked_list = SinglyLinkedList()
        self.assertTrue(linked_list.is_empty)

        new_node = Node(self.items[0])
        linked_list.insert_after(new_node, linked_list.first_node)
        self.assertFalse(linked_list.is_empty)

        linked_list.clear()
        self.assertTrue(linked_list.is_empty)

    def test_first_node(self):
        linked_list = SinglyLinkedList()
        new_node = Node(self.items[0])
        linked_list.insert_after(new_node, linked_list.first_node)

        self.assertEqual(new_node.object, linked_list.first_node.object)

    def test_insert_after(self):
        linked_list = SinglyLinkedList()
        prev_node = linked_list.first_node
        for item in self.items[:3]:
            new_node = Node(item)
            linked_list.insert_after(new_node, prev_node)
            prev_node = new_node

        self.assertListEqual(
            self.items[:3],
            [
                item.object
                for item in linked_list
            ]
        )

    def test_remove_after(self):
        linked_list = SinglyLinkedList(
            (Node(test_item) for test_item in self.items)
        )

        self.assertListEqual(
            self.items,
            [
                item.object
                for item in linked_list
            ]
        )

        node = linked_list.remove_after(linked_list.first_node)

        self.assertEqual(node.object, self.items[1])

        node = linked_list.remove_after(None)

        self.assertEqual(node.object, self.items[0])

    def test_reverse(self):
        linked_list = SinglyLinkedList(
            (Node(test_item) for test_item in self.items)
        )

        self.assertListEqual(
            self.items,
            [
                item.object
                for item in linked_list
            ]
        )

        linked_list.reverse()

        reversed_items = self.items[:]
        reversed_items.reverse()

        self.assertListEqual(
            reversed_items,
            [
                item.object
                for item in linked_list
            ]
        )

    def test_reverse_empty_list(self):
        linked_list = SinglyLinkedList()
        # check no errors
        linked_list.reverse()

    def test_repl_output(self):
        linked_list = SinglyLinkedList(
            (Node(test_item) for test_item in self.items)
        )

        self.assertEqual(
            str(linked_list),
            'SinglyLinkedList(['
            'Node(\'i0\'), '
            'Node(\'i1\'), '
            'Node(\'i2\'), '
            'Node(\'i3\'), '
            'Node(\'i4\')'
            '])'
        )
