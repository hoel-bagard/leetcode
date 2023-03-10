import bisect
import collections
import itertools

from typing_extensions import Self


class Solution:
    def three_sum_slow(self: Self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        nb_elts = len(nums)
        result: list[list[int]] = []

        # If all the numbers share the same sign, just return
        if nums[-1] < 0 or nums[0] > 0:
            return result

        for start_idx in range(nb_elts-2):
            if start_idx > 0 and nums[start_idx] == nums[start_idx - 1]:
                continue

            # If all the remaining numbers are positive, skip.
            if nums[start_idx] > 0:
                break

            middle_idx, end_idx = start_idx+1, len(nums)-1

            while middle_idx < end_idx:  # and signs differents
                if (three_sum := nums[start_idx] + nums[middle_idx] + nums[end_idx]) == 0:
                    result.append([nums[start_idx], nums[middle_idx], nums[end_idx]])
                    while middle_idx < end_idx and nums[middle_idx] == nums[middle_idx+1]:
                        middle_idx += 1
                    while middle_idx < end_idx and nums[end_idx] == nums[end_idx-1]:
                        end_idx -= 1
                    middle_idx += 1
                    end_idx -= 1
                elif three_sum < 0:
                    middle_idx += 1
                elif nums[start_idx] + nums[middle_idx] + nums[end_idx] > 0:
                    end_idx -= 1
        return result

    def three_sum(self: Self, nums: list[int]) -> set[tuple[int, int, int]]:
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

    def three_sum_fast(self: Self, nums: list[int]) -> list[tuple[int, int, int]]:
        """Fastest version according to leetcode.com."""
        nums_counts = collections.Counter(nums)
        triplets: list[tuple[int, int, int]] = []

        if nums_counts[0] >= 3:
            triplets.append((0, 0, 0))

        for num, count in nums_counts.items():
            if count >= 2 and (target := -2 * num) in nums_counts and num != 0:
                triplets.append((target, num, num))

        # TODO: remove the num != 0, and remove (0, 0, 0) here if added by mistake (num_counts[0] == 2)

        sorted_nums = sorted(nums_counts.keys())
        for i, neg in enumerate(sorted_nums[:bisect.bisect_left(sorted_nums, 0)]):
            # TODO: Comment this part.
            left = bisect.bisect_left(sorted_nums, -(neg + sorted_nums[-1]), i + 1)
            right = bisect.bisect_left(sorted_nums, -(neg / 2), left)
            for b in sorted_nums[left:right]:
                c = -(neg + b)
                if c in nums_counts:
                    triplets.append((neg, b, c))

        return triplets
