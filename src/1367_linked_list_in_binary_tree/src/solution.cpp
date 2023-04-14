#include "solution.hpp"

#include <cstdlib>
#include <memory>

bool is_sub_path_rec(std::shared_ptr<ListNode> head, std::shared_ptr<TreeNode> root) {
  if (head == nullptr) return true;
  if (root == nullptr) return false;

  if (root->val == head->val)
    return is_sub_path_rec(head->next, root->left) || is_sub_path_rec(head->next, root->right);
  else
    return false;
}

bool Solution::isSubPath(std::shared_ptr<ListNode> head, std::shared_ptr<TreeNode> root) {
  if (root == NULL) return false;

  return is_sub_path_rec(head, root) || isSubPath(head, root->left) || isSubPath(head, root->right);
}
