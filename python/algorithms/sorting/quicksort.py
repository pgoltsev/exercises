def quicksort1(arr, start_idx=None, end_idx=None):
    """
    Sort array using Quicksort algorithm.
    Classical algorithm was introduced by C. A. R. Hoare.
    :param arr: Array to sort.
    :param start_idx: Start index. By default is zero.
    :param end_idx: End index. By default is the last index of array.
    :return: Sorted array.
    """
    if start_idx is None:
        start_idx = 0
    if end_idx is None:
        end_idx = len(arr) - 1

    if start_idx < end_idx:
        part_index = partition1(arr, start_idx, end_idx)
        quicksort1(arr, start_idx, part_index)
        quicksort1(arr, part_index + 1, end_idx)


def partition1(arr, start_idx, end_idx):
    pivot = arr[start_idx]
    i = start_idx - 1
    j = end_idx + 1
    while True:
        while True:
            i = i + 1
            if arr[i] >= pivot:
                break

        while True:
            j = j - 1
            if arr[j] <= pivot:
                break

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]


def quicksort2(arr, start_idx=None, end_idx=None):
    """
    Sort array using Quicksort algorithm.
    Algorithm was introduced by Nico Lomuto.
    :param arr: Array to sort.
    :param start_idx: Start index. By default is zero.
    :param end_idx: End index. By default is the last index of array.
    :return: Sorted array.
    """
    if start_idx is None:
        start_idx = 0
    if end_idx is None:
        end_idx = len(arr) - 1

    if start_idx < end_idx:
        part_index = partition2(arr, start_idx, end_idx)
        quicksort2(arr, start_idx, part_index - 1)
        quicksort2(arr, part_index + 1, end_idx)


def partition2(arr, start_idx, end_idx):
    pivot = arr[end_idx]
    i = start_idx - 1
    j = start_idx
    while j <= end_idx - 1:
        if arr[j] <= pivot:
            i += 1
            if i != j:
                arr[i], arr[j] = arr[j], arr[i]
        j += 1
    arr[i + 1], arr[end_idx] = arr[end_idx], arr[i + 1]
    return i + 1


if __name__ == '__main__':
    import doctest

    doctest.testmod()
