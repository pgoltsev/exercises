from unittest import TestCase

from algorithms.sorting.quicksort import quicksort1, quicksort2


class QuickSort1TestCase(TestCase):
    def test_common_array(self):
        arr = [10, 2, 4, 6, 7, 5, 3, 1, 9, 8]

        quicksort1(arr)

        self.assertListEqual(arr, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_only_two_elements(self):
        arr = [10, 2]

        quicksort1(arr)

        self.assertListEqual(arr, [2, 10])

    def test_ordered(self):
        arr = [1, 2]

        quicksort1(arr)

        self.assertListEqual(arr, [1, 2])

    def test_one_element(self):
        arr = [2]

        quicksort1(arr)

        self.assertListEqual(arr, [2])

    def test_no_elements(self):
        arr = []

        quicksort1(arr)

        self.assertListEqual(arr, [])


class QuickSort2TestCase(TestCase):
    def test_common_array(self):
        arr = [10, 2, 4, 6, 7, 5, 3, 1, 9, 8]

        quicksort2(arr)

        self.assertListEqual(arr, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_only_two_elements(self):
        arr = [10, 2]

        quicksort2(arr)

        self.assertListEqual(arr, [2, 10])

    def test_ordered(self):
        arr = [1, 2]

        quicksort2(arr)

        self.assertListEqual(arr, [1, 2])

    def test_one_element(self):
        arr = [2]

        quicksort2(arr)

        self.assertListEqual(arr, [2])

    def test_no_elements(self):
        arr = []

        quicksort2(arr)

        self.assertListEqual(arr, [])
