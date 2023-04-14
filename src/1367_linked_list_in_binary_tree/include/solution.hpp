#pragma once

#include <memory>

// Definition for singly-linked list.
struct ListNode {
  int val;
  std::shared_ptr<ListNode> next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, std::shared_ptr<ListNode> next) : val(x), next(next) {}
};

// Definition for a binary tree node.
struct TreeNode {
  int val;
  std::shared_ptr<TreeNode> left;
  std::shared_ptr<TreeNode> right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, std::shared_ptr<TreeNode> left, std::shared_ptr<TreeNode> right) : val(x), left(left), right(right) {}
};

class Solution {
 public:
  bool isSubPath(std::shared_ptr<ListNode> head, std::shared_ptr<TreeNode> root);
};
