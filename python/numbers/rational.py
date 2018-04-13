class Rational:
    """Addition implementation of rational number.

    >>> Rational(1, 2) + Rational(1, 2) == Rational(2, 2)
    True

    >>> Rational(1, 2) + Rational(3, 4) == Rational(10, 8)
    True

    >>> Rational(1, 2) + Rational(3, 4) == Rational(5, 4)
    True

    >>> r = Rational(1, 2)
    >>> r += Rational(3, 4)
    >>> r == Rational(5, 4)
    True

    >>> from collections import namedtuple
    >>> RationalDuckType = namedtuple('Rational', ('numerator', 'denominator'))
    >>> r1 = RationalDuckType(numerator=3, denominator=5)
    >>> result = Rational(41, 35)
    >>> Rational(4, 7) + r1 == result and r1 + Rational(4, 7) == result
    True

    """

    def __init__(self, numerator, denominator):
        """
        Initialize an instance.

        :param numerator: Numerator.
        :param denominator: Denominator.
        """
        self._numerator = numerator
        self._denominator = denominator

    @property
    def denominator(self):
        """Get denominator."""
        return self._denominator

    @property
    def numerator(self):
        """Get numerator."""
        return self._numerator

    def __add__(self, other):
        """Perform addition of two rational numbers."""
        return Rational(*self._addition(self, other))

    def __iadd__(self, other):
        """Perform addition and assignment to the current number.

        :param other: Rational number to be addition to the current one.
        """
        self._numerator, self._denominator = self._addition(self, other)
        return self

    __radd__ = __add__

    @staticmethod
    def _addition(val1, val2):
        """Get result of addition of two rational numbers.

        :param val1: First number.
        :param val2: Second number.
        :return: A tuple containing a numerator and a denominator.
        """
        if val1.denominator != val2.denominator:
            denominator = val1.denominator * val2.denominator

            val2_num = val1.denominator * val2.numerator
            val1_num = val2.denominator * val1.numerator

            numerator = val1_num + val2_num
        else:
            numerator = val1.numerator + val2.numerator
            denominator = val1.denominator

        return numerator, denominator

    def __eq__(self, other):
        """Perform equality.

        :param other: Rational number to be checked for equality
        with the current one.
        :return: True if the current number is equal to the other one,
        False otherwise.
        """
        return self._numerator / other.numerator == \
            self._denominator / other.denominator

    def __repr__(self):
        """Get representation."""
        return '%s/%s' % (self._numerator, self._denominator)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
