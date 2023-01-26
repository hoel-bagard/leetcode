from typing_extensions import Self


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val: int | None = None, left: Self | None = None, right: Self | None = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:  # noqa: N802
        self.update_tree_recursively(root)
        return root

    def update_tree_recursively(self, node: TreeNode | None, bigger_sum: int = 0) -> int:
        if node is None or node.val is None:
            return bigger_sum

        node.val += self.update_tree_recursively(node.right, bigger_sum)
        return self.update_tree_recursively(node.left, node.val)
