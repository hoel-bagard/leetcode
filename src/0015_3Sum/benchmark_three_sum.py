import random
from typing import Any

from .three_sum import Solution

solution = Solution()


def get_nums(nb_nums: int = 10_000) -> tuple[tuple[list[int]], dict[str, Any]]:
    nums = list(range(nb_nums))
    random.shuffle(nums)
    return ((nums, ), {})


def test_slow(benchmark):  # pyright: ignore[reportMissingParameterType]
    # benchmark.pedantic(solution.three_sum_slow, args=(nums, ), rounds=500, iterations=10)
    benchmark.pedantic(solution.three_sum_slow, setup=get_nums, rounds=500, iterations=1)


def test_slow_already_sorted(benchmark):  # pyright: ignore[reportMissingParameterType]
    nums = list(range(10_000))
    benchmark.pedantic(solution.three_sum_slow, args=(nums, ), rounds=500, iterations=10)


def test_fast(benchmark):  # pyright: ignore[reportMissingParameterType]
    benchmark.pedantic(solution.three_sum, setup=get_nums, rounds=500, iterations=1)


def test_fast_already_sorted(benchmark):  # pyright: ignore[reportMissingParameterType]
    nums = list(range(10_000))
    benchmark.pedantic(solution.three_sum, args=(nums, ), rounds=500, iterations=10)
