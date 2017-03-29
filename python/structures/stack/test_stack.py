from unittest import TestCase

from python.structures.stack.stack import Stack, StackIsEmpty, StackOverflow


class StackTestCase(TestCase):
    def setUp(self):
        super().setUp()

        self.stack = Stack()
        self.test_items = [
            'testitem1',
            'testitem2',
        ]

    def test_push(self):
        test_item = 'testitem'

        self.assertEqual(self.stack.length, 0)

        self.stack.push(test_item)

        self.assertEqual(test_item, self.stack.peek())
        self.assertEqual(self.stack.length, 1)

    def test_pop(self):
        self.stack.push(self.test_items[0])
        self.stack.push(self.test_items[1])
        popped_item = self.stack.pop()

        self.assertEqual(self.test_items[1], popped_item)
        self.assertEqual(self.stack.length, 1)

        popped_item = self.stack.pop()

        self.assertEqual(self.test_items[0], popped_item)
        self.assertEqual(self.stack.length, 0)

        with self.assertRaises(StackIsEmpty):
            self.stack.pop()

    def test_peek(self):
        self.assertEqual(self.stack.length, 0)

        self.stack.push(self.test_items[0])
        self.stack.push(self.test_items[1])

        self.assertEqual(self.test_items[1], self.stack.peek())
        self.assertEqual(self.stack.length, 2)

        self.stack.pop()

        self.assertEqual(self.test_items[0], self.stack.peek())

        self.stack.pop()

        self.assertEqual(None, self.stack.peek())

    def test_length(self):
        self.assertEqual(self.stack.length, 0)

        self.stack.push(self.test_items[0])

        self.assertEqual(self.stack.length, 1)

        self.stack.push(self.test_items[1])

        self.assertEqual(self.stack.length, 2)

        self.stack.pop()

        self.assertEqual(self.stack.length, 1)

        self.stack.pop()

        self.assertEqual(self.stack.length, 0)

    def test_size(self):
        stack = Stack(3)

        self.assertEqual(stack.size, 3)

    def test_limited_stack(self):
        stack = Stack(1)

        stack.push(self.test_items[0])

        self.assertEqual(stack.length, 1)

        with self.assertRaises(StackOverflow):
            stack.push(self.test_items[1])

        self.assertEqual(stack.length, 1)

    def test_clear(self):
        self.stack.push(self.test_items[0])
        self.stack.push(self.test_items[1])

        self.assertEqual(self.stack.length, 2)

        self.stack.clear()

        self.assertEqual(self.stack.length, 0)

        with self.assertRaises(StackIsEmpty):
            self.stack.pop()
