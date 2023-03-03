import pytest

from .longest_common_prefix import Solution

solution = Solution()


@pytest.mark.parametrize("strs, expected",
                         [
                             (["flower", "flow", "flight"], "fl"),
                             (["dog", "racecar", "car"], ""),
                             (["a"], "a"),
                             (["japan", "japan", "japan", "japan"], "japan"),
                         ])
def test_base(strs: list[str], expected: str) -> None:
    result = solution.longestCommonPrefix(strs)
    assert expected == result


@pytest.mark.parametrize("strs, expected",
                         [
                             ([""], ""),
                             (["", ""], ""),
                         ])
def test_empty(strs: list[str], expected: str) -> None:
    result = solution.longestCommonPrefix(strs)
    assert expected == result
