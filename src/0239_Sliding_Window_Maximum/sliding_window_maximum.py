from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        result: list[int] = []
        window: deque[int] = deque()
        for i in range(len(nums)):
            while window and nums[window[-1]] < nums[i]:
                window.pop()

            window.appendleft(i)

            result.append(nums[window[-1]])

        return result
