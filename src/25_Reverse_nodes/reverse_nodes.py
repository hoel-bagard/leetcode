"""25. Reverse Nodes in k-Group.

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
k is a positive integer and is less than or equal to the length of the linked list.If the number of nodes is not
a multiple of k then left-out nodes, in the end, should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be changed.
"""

from typing_extensions import Self


class ListNode:
    """Definition for singly-linked list."""
    def __init__(self: Self, val: int = 0, next_node: Self | None = None) -> None:
        self.val = val
        self.next_node = next_node

    def __repr__(self: Self) -> str:
        return f"{type(self).__name__}({self.val}, {self.next_node})"


def reverse_k_group(head: ListNode, k: int) -> ListNode:
    new_head = ListNode()
    # Jump is used to connect the last node of the previous k-group to the first node of the following k-group.
    jump = new_head

    new_head.next_node = group_start = group_end = head

    while True:
        count = 0
        while group_end and count < k:   # use r to locate the range
            group_end = group_end.next_node
            count += 1
        if count == k:  # If there are enough element to reverse, reverse them
            previous, current = group_end, group_start
            for _ in range(k):
                # Standard reversing
                current.next_node, current, previous = previous, current.next_node, current  # pyright: ignore
            # Connect the two k-groups
            jump.next_node, jump, group_start = previous, group_start, group_end
        else:
            return new_head.next_node
