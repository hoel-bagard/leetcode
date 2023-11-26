import pytest

from .sliding_window_maximum import Solution

solution = Solution()


@pytest.mark.parametrize(("nums", "window_size", "expected"),
                         [
                             ([1,3,-1,-3,5,3,6,7], 3, [3,3,5,5,6,7]),
                             ([1], 1, [1]),
                         ])
def test_base(nums: list[int], window_size: int, expected: list[int]) -> None:
    result = solution.maxSlidingWindow(nums, window_size)
    assert expected == result
