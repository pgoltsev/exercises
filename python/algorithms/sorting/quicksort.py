import copy


def quicksort1(arr):
    """
    Sort array using Quicksort algorithm.
    :param arr: Array to sort.
    :return: Sorted array.

    >>> quicksort1([10, 2, 4, 6, 7, 5, 3, 1, 9, 8])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> quicksort1([10, 2])
    [2, 10]
    >>> quicksort1([1, 2])
    [1, 2]
    >>> quicksort1([2])
    [2]
    >>> quicksort1([])
    []
    """

    if len(arr) < 2:
        return arr

    result = copy.copy(arr)
    pivot_index = len(result) - 1
    cur_ind = 0
    while cur_ind < pivot_index and pivot_index >= 0:
        pivot = result[pivot_index]
        cur_val = result[cur_ind]
        if cur_val > pivot:
            result.insert(pivot_index, result.pop(cur_ind))
            pivot_index -= 1
        else:
            cur_ind += 1

    result = quicksort1(result[:pivot_index]) + [pivot] + quicksort1(
        result[pivot_index + 1:])

    return result


def partition2(arr, start_ind, end_index):
    pivot = arr[start_ind]
    i = start_ind - 1
    j = end_index + 1
    while True:
        while True:
            i = i + 1
            if arr[i] < pivot:
                break

        while True:
            j = j - 1
            if pivot < arr[j]:
                break

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]


def quicksort2(arr, start_ind=None, end_index=None):
    """
    Sort array using Quicksort algorithm.
    Classical algorithm introduced by C. A. R. Hoare.
    :param arr: Array to sort.
    :param start_ind: Start index. By default is zero.
    :param end_ind: End index. By default is the last index of array.
    :return: Sorted array.

    >>> quicksort1([10, 2, 4, 6, 7, 5, 3, 1, 9, 8])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> quicksort1([10, 2])
    [2, 10]
    >>> quicksort1([1, 2])
    [1, 2]
    >>> quicksort1([2])
    [2]
    >>> quicksort1([])
    []
    """
    if start_ind is None:
        start_ind = 0
    if end_index is None:
        end_index = len(arr) - 1

    if start_ind < end_index:
        part_index = partition2(arr, start_ind, end_index)
        quicksort2(arr, start_ind, part_index)
        quicksort2(arr, part_index + 1, end_index)


def partition3(arr, start_ind, end_index):
    pivot = arr[end_index]
    i = start_ind - 1
    for j in range(end_index - 1):
        if arr[j] <= pivot:
            i += 1
            if i != j:
                arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[end_index] = arr[end_index], arr[i + 1]
    return i + 1


def quicksort3(arr, start_ind=None, end_index=None):
    """
    Sort array using Quicksort algorithm.
    Algorithm introduced by Nico Lomuto.
    :param arr: Array to sort.
    :param start_ind: Start index. By default is zero.
    :param end_ind: End index. By default is the last index of array.
    :return: Sorted array.

    >>> quicksort1([10, 2, 4, 6, 7, 5, 3, 1, 9, 8])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> quicksort1([10, 2])
    [2, 10]
    >>> quicksort1([1, 2])
    [1, 2]
    >>> quicksort1([2])
    [2]
    >>> quicksort1([])
    []
    """
    if start_ind is None:
        start_ind = 0
    if end_index is None:
        end_index = len(arr) - 1

    if start_ind < end_index:
        part_index = partition3(arr, start_ind, end_index)
        quicksort2(arr, start_ind, part_index - 1)
        quicksort2(arr, part_index + 1, end_index)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
