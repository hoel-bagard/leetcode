from itertools import zip_longest


class Solution:
    def __init__(self) -> None:
        self.roman_char_to_int: dict[str, int] = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    def romanToInt(self, roman_numeral: str) -> int:  # noqa: N802
        result = 0
        for char, next_char in zip_longest(roman_numeral, roman_numeral[1:], fillvalue="I"):
            result += val if (val := self.roman_char_to_int[char]) >= self.roman_char_to_int[next_char] else -val
        return result
