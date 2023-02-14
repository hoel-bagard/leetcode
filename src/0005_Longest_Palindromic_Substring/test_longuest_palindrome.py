import pytest
from hypothesis import given
from hypothesis.strategies import text

from .longuest_palindrome import Solution, SolutionBruteForce

solution = Solution()


@pytest.mark.parametrize("input_string, expected_answer",
                         [("babad", "bab"),
                          ("cbbd", "bb"),
                          ("bb", "bb"),
                          ])
def test_simple(input_string: str, expected_answer: str):
    output = solution.longestPalindrome(input_string)
    assert expected_answer == output


solution_bf = SolutionBruteForce


def test_is_palindrome_base():
    assert solution_bf.is_palindrome("a")
    assert solution_bf.is_palindrome("aa")
    assert solution_bf.is_palindrome("aba")
    assert solution_bf.is_palindrome("abba")
    assert solution_bf.is_palindrome("ababa")
    assert not solution_bf.is_palindrome("abaa")
    assert not solution_bf.is_palindrome("abaca")


@given(text())
def test_is_palindrome(string: str):
    assert solution_bf.is_palindrome("".join([string, string[::-1]]))
    assert solution_bf.is_palindrome("".join([string[:-1], string[::-1]]))
