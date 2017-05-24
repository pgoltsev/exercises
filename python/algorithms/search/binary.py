def search1(value, arr):
    """
    Common implementation of binary search.
    :param value: Value to search.
    :param arr: Array to search in.
    :return: Index of found element or -1 if no element found.

    >>> search2(1, [1, 2, 3, 5, 8, 10, 15, 33, 56, 68, 102])
    0
    >>> search2(102, [1, 2, 3, 5, 8, 10, 15, 33, 56, 68, 102])
    10
    >>> search2(69, [1, 2, 3, 5, 8, 10, 15, 33, 56, 68, 102])
    -1
    >>> search2(15, [1, 2, 3, 5, 8, 10, 15, 33, 56, 68, 102])
    6
    """
    arr_length = len(arr)
    first_ind = 0
    last_ind = arr_length - 1
    while last_ind - first_ind > 1:
        middle_ind = (last_ind - first_ind) // 2
        cur_value = arr[middle_ind]
        if value == cur_value:
            return middle_ind

        if cur_value < value:
            last_ind = middle_ind
        else: # value < cur_value
            first_ind = middle_ind

    return -1


def search2(value, arr):
    """
    Experimental implementation of binary search using recursion.
    Not very good solution because of recursion. It may lead to stack
    overflow on big arrays.
    :param value: Value to search.
    :param arr: Array to search in.
    :return: Index of found element or -1 if no element found.

    >>> search2(1, [1, 2, 3, 5, 8, 10, 15, 33, 56, 68, 102])
    0
    >>> search2(102, [1, 2, 3, 5, 8, 10, 15, 33, 56, 68, 102])
    10
    >>> search2(69, [1, 2, 3, 5, 8, 10, 15, 33, 56, 68, 102])
    -1
    >>> search2(15, [1, 2, 3, 5, 8, 10, 15, 33, 56, 68, 102])
    6
    """
    arr_length = len(arr)
    if arr_length == 0:
        return -1
    cur_ind = arr_length // 2
    if 0 > cur_ind >= arr_length:
        return -1
    cur_value = arr[cur_ind]
    if cur_value == value:
        result_index = cur_ind
    else:
        if value < cur_value:
            result_index = search2(value, arr[:cur_ind])
        else:  # arr[cur_ind] < value
            start_ind = cur_ind + 1
            result_index = search2(value, arr[start_ind:])
            if result_index != -1:
                result_index += start_ind
    return result_index


if __name__ == '__main__':
    import doctest

    doctest.testmod()
