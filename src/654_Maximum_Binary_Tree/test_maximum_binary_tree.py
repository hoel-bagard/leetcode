import pytest

from .maximum_binary_tree import Solution, TreeNode

solution = Solution()


def tree_to_list(tree_root: TreeNode | None) -> list[int | None]:
    """Converts a binary tree to a list.

    The list corresponds to the tree traversed in a breadth first fashion.
    (That's the answer format given by leetcode.com)
    """
    # Edge case in case the tree_root is None.
    if tree_root is None:
        return [None]

    # Traverse the tree breadth first using a queue, accumulate the values in a list while doing so.
    tree_as_list: list[int | None] = []
    queue: list[TreeNode | None] = [tree_root]
    while queue:
        node = queue.pop(0)
        if node is not None:
            tree_as_list.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            tree_as_list.append(None)

    # The leetcode solutions don't have Nones at the end, so trim them.
    while tree_as_list[-1] is None:
        tree_as_list.pop()

    return tree_as_list


@pytest.mark.parametrize("nums, solution_as_list",
                         [([3, 2, 1, 6, 0, 5], [6, 3, 5, None, 2, 0, None, None, 1]),
                          ([3, 2, 1, 5, 6, 0], [6, 5, 0, 3, None, None, None, None, 2, None, 1]),
                          ([1, 2, 3, 4], [4, 3, None, 2, None, 1]),
                          ([3, 2, 1], [3, None, 2, None, 1]),
                          ])
def test_base(nums: list[int], solution_as_list: list[int | None]) -> None:
    result = solution.constructMaximumBinaryTree(nums)
    result_as_list = tree_to_list(result)
    assert result_as_list == solution_as_list


def test_empty() -> None:
    result = solution.constructMaximumBinaryTree([])
    result_as_list = tree_to_list(result)
    assert result_as_list == [None]
