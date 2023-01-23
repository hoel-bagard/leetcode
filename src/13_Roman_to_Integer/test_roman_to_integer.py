import pytest

from .roman_to_integer import Solution

solution = Solution()


@pytest.mark.parametrize("roman_numeral, integer",
                         [("III", 3),
                          ("LVIII", 58),
                          ("XXVII", 27),
                          ])
def test_simple(roman_numeral: str, integer: int):
    assert solution.romanToInt(roman_numeral) == integer


@pytest.mark.parametrize("roman_numeral, integer",
                         [("MCMXCIV", 1994),
                          ("IV", 4),
                          ])
def test_subtraction(roman_numeral: str, integer: int):
    assert solution.romanToInt(roman_numeral) == integer
