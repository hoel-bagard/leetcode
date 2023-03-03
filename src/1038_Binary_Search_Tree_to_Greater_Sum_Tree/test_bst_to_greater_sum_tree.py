import pytest

from .bst_to_greater_sum_tree import Solution, TreeNode

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


def list_to_tree(node_list: list[int | None]) -> TreeNode:
    assert node_list[0] is not None
    tree_root = TreeNode(val=node_list[0])
    queue: list[TreeNode] = [tree_root]
    while node_list:
        node = queue.pop(0)
        node.val = node_list.pop(0)
        if node.val is not None:
            node.left = TreeNode()
            node.right = TreeNode()
            queue.append(node.left)
            queue.append(node.right)

    return tree_root


@pytest.mark.parametrize(("bst_as_list", "answer_as_list"),
                         [([4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8],
                           [30, 36, 21, 36, 35, 26, 15, None, None, None, 33, None, None, None, 8]),
                          ([0, None, 1], [1, None, 1]),
                          ])
def test_simple(bst_as_list: list[int | None], answer_as_list: list[int | None]) -> None:
    bst = list_to_tree(bst_as_list)
    output = solution.bstToGst(bst)
    output_as_list = tree_to_list(output)

    assert output_as_list == answer_as_list
