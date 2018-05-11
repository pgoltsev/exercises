"""Implementations calculation of factorial."""


def factorial_recursion(number):
    """Calculates factorial using recursion.

    :param number: A number for which factorial should be calculated.
    :return: Factorial number.

    >>> factorial_recursion(-1)
    1
    >>> factorial_recursion(0)
    1
    >>> factorial_recursion(1)
    1
    >>> factorial_recursion(3)
    6
    >>> factorial_recursion(5)
    120
    """

    if number in (0, 1) or number < 0:
        return 1

    return number * factorial_recursion(number - 1)


def factorial_loop(number):
    """Calculates factorial using loop.

    :param number: A number for which factorial should be calculated.
    :return: Factorial number.

    >>> factorial_loop(-1)
    1
    >>> factorial_loop(0)
    1
    >>> factorial_loop(1)
    1
    >>> factorial_loop(3)
    6
    >>> factorial_loop(5)
    120
    """
    result = 1
    while number > 1:
        result *= number
        number -= 1

    return result


if __name__ == '__main__':
    import doctest

    doctest.testmod()
