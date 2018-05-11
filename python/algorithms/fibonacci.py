"""Implementations calculation of Fibonacci numbers."""


def fib1(amount):
    """
    Calculate Fibonacci numbers.

    The second variable is used to store the result.
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
    first, second = 0, 1
    for _ in range(amount):
        yield first
        first, second = second + first, first


def fib2(amount):
    """
    Calculate Fibonacci numbers.

    The first variable is used to store the result.
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
    first, second = 1, 0
    for _ in range(amount):
        first, second = second, first + second
        yield first


if __name__ == '__main__':
    import doctest

    doctest.testmod()
