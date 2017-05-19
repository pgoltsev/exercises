def fib1(amount):
    """
    Fibonacci generator example. The second variable is used to store
    the result.
    :param amount: Amount of numbers to produce.
    :return: Generator.

    >>> list(fib1(0))
    []
    >>> list(fib1(1))
    [0]
    >>> list(fib1(3))
    [0, 1, 1]
    >>> list(fib1(9))
    [0, 1, 1, 2, 3, 5, 8, 13, 21]
    """
    first = 0
    second = 1
    while 0 < amount:
        yield first
        first, second = second, first
        second += first
        amount -= 1


def fib2(amount):
    """
    Fibonacci generator example. The first variable is used to store
    the result.
    :param amount: Amount of numbers to produce.
    :return: Generator.

    >>> list(fib2(0))
    []
    >>> list(fib2(1))
    [0]
    >>> list(fib2(3))
    [0, 1, 1]
    >>> list(fib2(9))
    [0, 1, 1, 2, 3, 5, 8, 13, 21]
    """
    first = 0
    second = 1
    while 0 < amount:
        first, second = second, first
        yield second
        first += second
        amount -= 1


if __name__ == '__main__':
    import doctest

    doctest.testmod()
