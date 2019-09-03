from kata_1 import (
    check_divisible
)

""" TDD_Agile_technical_practices_distilled: kata 1 """
""" Write a function that takes numbers from 1 to 100 and outputs them as """
""" a string, but for multiples of three it returns Fizz instead of the """
""" number, and for multiples of five it returns Buzz. For numbers that are """
""" multiples of both three and five, it returns FizzBuzz."""


def test_check_divisible_returns_string():
    result = check_divisible(1)
    assert isinstance(result, str)


def test_check_divisible_returns_same_number_as_string():
    result = check_divisible(2)
    assert isinstance(result, str)
    assert result == "2"


def test_check_divisible_returns_fizz_when_divisible_by_three():
    result = check_divisible(3)
    assert isinstance(result, str)
    assert result == "fizz"


def test_check_divisible_returns_buzz_when_divisible_by_five():
    result = check_divisible(5)
    assert isinstance(result, str)
    assert result == "buzz"


def test_check_divisible_returns_fizzbuzz_when_divisible_by_three_and_five():
    result = check_divisible(15)
    assert isinstance(result, str)
    assert result == "fizzbuzz"


def test_check_divisible_returns_nothing_when_number_is_greater_than_the_valid_range():
    result = check_divisible(101)
    assert not result


def test_check_divisible_returns_nothing_when_number_is_lower_than_the_valid_range():
    result = check_divisible(-1)
    assert not result
