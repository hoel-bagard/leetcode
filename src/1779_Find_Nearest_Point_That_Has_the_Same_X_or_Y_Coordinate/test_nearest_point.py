import pytest

from .nearest_point import Solution

solution = Solution()


@pytest.mark.parametrize("x, y, points, expected",
                         [(3, 4, [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]], 2),
                          (3, 4, [[3, 4]], 0),
                          ])
def test_base(x: int, y: int, points: list[list[int]], expected: int):
    assert solution.nearestValidPoint(x, y, points) == expected


@pytest.mark.parametrize("x, y, points, expected",
                         [(3, 4, [[2, 3]], -1),
                          ])
def test_impossible(x: int, y: int, points: list[list[int]], expected: int):
    assert solution.nearestValidPoint(x, y, points) == expected
