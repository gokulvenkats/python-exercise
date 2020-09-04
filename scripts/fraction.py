"""
In this exercise, you will create a class `Fraction` which can represent fractional values.

You will have to add the definition of the class, and the definitions of two sort functions,
where you will use lambda expressions for the key function.
"""

class Fraction:
    """
    class `Fraction`

    A fraction is initialized with two arguments - numerator and denominator - and these
    values are what should be held in the class.

    When an object of the class is passed to a `print`, it should print in the form
    `numerator/denominator`.
    For example,
    numerator=2, denominator=3, should be printed as
    2/3

    Add a helper function that gets the fractional value of this fraction, rounded upto 3 decimal places.
    For example,
    numerator=2, denominator=3
    Value should be 0.667
    """
    pass


def sort_fractions_by_denominator(fractions):
    """
    The function takes a list of `Fraction` objects as its argument.
    It returns a list of the fractions sorted by its denominator.
    Use a lambda expression for the key function.

    For example,
    INPUT: [1/2, 3/4, 2/3]
    OUTPUT: [3/4, 2/3, 1/2]
    """
    return


def sort_fractions_by_value(fractions):
    """
    The function takes a list of `Fraction` objects as its argument.
    It returns a list of the fractions sorted by its floating point value.
    Use a lambda expression for the key function.

    For example,
    INPUT: [1/2, 3/4, 1/3]
    OUTPUT: [3/4, 1/2, 1/3]
    """
    return


def main():
    print('FRACTIONS')
    print('=========')
    fractions = [
        Fraction(1, 2),
        Fraction(3, 4),
        Fraction(1, 3),
        Fraction(5, 1),
        Fraction(4, 5),
    ]
    print(fractions)
    print(sort_fractions_by_denominator(fractions))
    print(sort_fractions_by_value(fractions))


if __name__ == '__main__':
    main()
