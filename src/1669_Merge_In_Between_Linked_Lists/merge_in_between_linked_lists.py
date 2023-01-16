"""Merge In Between Linked Lists exercise from leetcode.com.

You are given two linked lists: list1 and list2 of sizes n and m respectively.
Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

Constraints:
- 3 <= list1.length <= 104
- 1 <= a <= b < list1.length - 1
- 1 <= list2.length <= 104
"""
from typing import Optional

from typing_extensions import Self


class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, val: float = 0, next: Optional[Self] = None):  # noqa: A002
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:  # noqa: N802
        # Go through the first linked list to find where to cut (node a-1) and where to stitch (node b+1).
        current_node, cut_node, idx = list1, None, 0
        while idx < b+1 and current_node is not None:
            if idx == a-1:
                cut_node = current_node
            current_node = current_node.next
            idx += 1
        stitch_node = current_node  # Renaming for clarity. The stitch node is node b+1.

        # Cut list1 and make it point to list2.
        assert cut_node is not None
        cut_node.next = list2

        # Go to the end of list2 and make its last node point to the stitch node.
        while list2.next is not None:
            list2 = list2.next
        list2.next = stitch_node

        return list1
