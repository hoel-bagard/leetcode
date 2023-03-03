import random
from collections.abc import Callable, Iterable

import pytest
from hypothesis import given
from hypothesis import strategies as st

from .three_sum import Solution

solution = Solution()
min_value, max_value = -100_000, 100_000
min_size, max_size = 3, 3000


def to_set(list_output: Iterable[Iterable[int]]) -> set[tuple[int, int, int]]:
    return {tuple(triplet) for triplet in list_output}


@pytest.mark.parametrize("nums, expected_answer",
                         [([-1, 0, 1, 2, -1, -4], {(-1, -1, 2), (-1, 0, 1)}),
                          ([-1, 3, 1, 2, -1, -4], {(-1, -1, 2), (-4, 1, 3)}),
                          ([0, 1, 1], set()),
                          ([0, 0, 0], {(0, 0, 0)}),
                          ([0, 0, 0, 0], {(0, 0, 0)}),
                          ])
def test_base(nums: list[int], expected_answer: set[tuple[int, int, int]]) -> None:
    output = solution.three_sum(nums)
    assert expected_answer == to_set(output)


@given(st.lists(st.integers(min_value=1, max_value=max_value),
                min_size=min_size,
                max_size=max_size))
def test_all_positive(nums: list[int]) -> None:
    output = solution.three_sum(nums)
    assert set() == to_set(output)


@given(st.lists(st.integers(min_value=min_value, max_value=-1),
                min_size=min_size,
                max_size=max_size))
def test_all_negative(nums: list[int]) -> None:
    output = solution.three_sum(nums)
    assert set() == to_set(output)


@given(st.lists(st.integers(min_value=min_value, max_value=max_value),
                min_size=min_size,
                max_size=max_size))
def test_no_duplicates(nums: list[int]) -> None:
    output = solution.three_sum(nums)
    assert len(output) == len(to_set(output))


@given(triplets=st.sets(st.builds(lambda neg, pos: tuple(sorted([neg, -neg-pos, pos])),
                                  st.integers(min_value=min_value, max_value=0),
                                  st.integers(min_value=0, max_value=max_value)),
                        min_size=0, max_size=10))
def test_can_find_triplets_non_exclusive(triplets: set[tuple[int, int, int]]) -> None:
    nums = []
    for triplet in triplets:
        nums.extend(triplet)
    output = solution.three_sum(nums)
    assert triplets.issubset(to_set(output))


@st.composite
def generate_nums(draw: Callable) -> tuple[list[int], set[tuple[int, int, int]]]:  # pyright: ignore
    nb_triplets: int = draw(st.integers(min_value=0, max_value=10))
    expected: set[tuple[int, int, int]] = set()
    nums: list[int] = []
    for _ in range(nb_triplets):
        neg: int = draw(st.integers(min_value=min_value, max_value=0))
        pos: int = draw(st.integers(min_value=0, max_value=max_value))
        target = -(neg + pos)
        expected.add(tuple(sorted([neg, target, pos])))
        nums.extend([neg, pos, target])
    random.shuffle(nums)
    return nums, expected


@given(nums_expected=generate_nums())
def test_can_find_triplets_non_exclusive_composite(nums_expected: tuple[list[int], set[tuple[int, int, int]]]) -> None:
    nums, expected = nums_expected
    output = solution.three_sum(nums)
    assert expected.issubset(to_set(output))


# TODO: test against reference implementation.
