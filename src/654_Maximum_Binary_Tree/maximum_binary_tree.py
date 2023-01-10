"""Maximum Binary Tree exercise from leetcode.com.

You are given an integer array nums with no duplicates.
A maximum binary tree can be built recursively from nums using the following algorithm:
- Create a root node whose value is the maximum value in nums.
- Recursively build the left subtree on the subarray prefix to the left of the maximum value.
- Recursively build the right subtree on the subarray suffix to the right of the maximum value.
- Return the maximum binary tree built from nums.
"""
from typing import Optional

from typing_extensions import Self


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val: int = 0, left: Optional[Self] = None, right: Optional[Self] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: list[int]) -> TreeNode | None:  # noqa: N802
        # Edge case where the list is empty.
        if not nums:
            return None

        # Get the index of the max value.
        index_max = nums.index(max(nums))
        # Create a node with the max as its value.
        node = TreeNode(nums[index_max])
        # Set its left and right node to the left and right parts of the list (converted to trees throught recursion).
        node.left = self.constructMaximumBinaryTree(nums[:index_max])
        node.right = self.constructMaximumBinaryTree(nums[index_max+1:])

        return node
