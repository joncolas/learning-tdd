from kata_2 import (
    isLapYear
)

""" TDD_Agile_technical_practices_distilled: kata 2 """
""" Write a function that returns true or false depending on whether its """
""" input integer is a leap year or not. A leap year is defined as one that """
""" is divisible by 4, but is not otherwise divisible by 100 unless it is """
""" also divisible by 400. For example, 2001 is a typical common year and """
""" 1996 is a typical leap year, whereas 1900 is an atypical common year """
""" and 2000 is an atypical leap year. """


""" EXPLANATION """
""" LAP YEARS ARE 1996 and 2000 """
""" Those are not divisible by 4 and not by 100 and 400 OR are divisible by """
""" 4 and 100 and 400 """

""" LAP YEARS ARE NOT 2001 and 1900 """
""" Those are not divisible by 4 and 100 and 400 OR are divisible by 4 """
""" and 100 but not divisible by 400 """

""" EXAMPLES """
""" 2001 """
""" 2001/4/100/400 = NOT DIVISIBLE """

""" 1996 """
""" 1996/4 = DIVISIBLE """
""" 1996/100/400 = NOT DIVISIBLE """

""" 1990 """
""" 1990/4/100 = DIVISIBLE """
""" 1990/400 = NOT DIVISIBLE """

""" 2000 """
""" 2000/4/100/400 = DIVISIBLE """



def test_is_lapyear_when_divisible_by_four_but_not_by_one_hundred_and_four_hundred():
    lapyear = isLapYear(1996)
    assert lapyear


def test_is_not_lapyear_when_not_divisible_by_four():
    lapyear = isLapYear(2001)
    assert not lapyear


def test_is_not_lapyear_when_divisible_by_four_and_by_one_hundred_but_not_by_four_hundred():
    lapyear = isLapYear(1900)
    assert not lapyear


def test_is_lapyear_when_divisible_by_four_and_by_one_hundred_and_by_four_hundred():
    lapyear = isLapYear(2000)
    assert lapyear
