import bisect
import collections
import itertools
import random
from collections.abc import Callable, Iterable

import pytest
from hypothesis import given, settings
from hypothesis import strategies as st

from .three_sum import Solution

solution = Solution()
min_value, max_value = -100_000, 100_000
min_size, max_size = 3, 3000


def to_sorted_set(list_output: Iterable[Iterable[int]]) -> set[tuple[int, int, int]]:
    return {tuple(sorted(triplet)) for triplet in list_output}


@pytest.mark.parametrize(("nums", "expected_answer"),
                         [([-1, 0, 1, 2, -1, -4], {(-1, -1, 2), (-1, 0, 1)}),
                          ([-1, 3, 1, 2, -1, -4], {(-1, -1, 2), (-4, 1, 3)}),
                          ([0, 1, 1], set()),
                          ([0, 0, 0], {(0, 0, 0)}),
                          ([0, 0, 0, 0], {(0, 0, 0)}),
                          ])
def test_base(nums: list[int], expected_answer: set[tuple[int, int, int]]) -> None:
    output = solution.three_sum(nums)
    assert expected_answer == to_sorted_set(output)


@given(st.lists(st.integers(min_value=1, max_value=max_value),
                min_size=min_size,
                max_size=max_size))
def test_all_positive(nums: list[int]) -> None:
    output = solution.three_sum(nums)
    assert set() == to_sorted_set(output)


@given(st.lists(st.integers(min_value=min_value, max_value=-1),
                min_size=min_size,
                max_size=max_size))
def test_all_negative(nums: list[int]) -> None:
    output = solution.three_sum(nums)
    assert set() == to_sorted_set(output)


@settings(max_examples=150)
@given(st.lists(st.integers(min_value=min_value, max_value=max_value),
                min_size=min_size,
                max_size=max_size))
def test_no_duplicates(nums: list[int]) -> None:
    output = solution.three_sum(nums)
    assert len(output) == len(to_sorted_set(output))


@given(triplets=st.sets(st.builds(lambda neg, pos: tuple(sorted([neg, -neg-pos, pos])),
                                  st.integers(min_value=min_value, max_value=0),
                                  st.integers(min_value=0, max_value=max_value)),
                        min_size=0, max_size=10))
def test_can_find_triplets_non_exclusive(triplets: set[tuple[int, int, int]]) -> None:
    nums = []
    for triplet in triplets:
        nums.extend(triplet)
    output = solution.three_sum(nums)
    assert triplets.issubset(to_sorted_set(output))


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
    assert expected.issubset(to_sorted_set(output))


def reference_implementation(nums: list[int]) -> set[tuple[int, int, int]]:
    nums.sort()
    nums_counts = collections.Counter(nums)
    result: set[tuple[int, int, int]] = set()

    zero_idx = bisect.bisect_left(nums, 0)
    for pos, neg in itertools.product(nums[:zero_idx], nums[zero_idx:]):
        if ((target := -(pos + neg)) in nums_counts
                and (target != pos or nums_counts[pos] > 1)
                and (target != neg or nums_counts[neg] > 1)):
            result.add(tuple(sorted([pos, neg, target])))
    if nums_counts[0] >= 3:
        result.add((0, 0, 0))

    return result


@settings(max_examples=150)
@given(nums=st.lists(st.integers(), min_size=0, max_size=100))
def test_against_reference_implementation(nums: list[int]) -> None:
    expected = reference_implementation(nums)
    output = solution.three_sum(nums)
    assert to_sorted_set(output) == expected
