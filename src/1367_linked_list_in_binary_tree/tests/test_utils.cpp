#include <unistd.h>

#include <chrono>
#include <cstdlib>
#include <optional>
#include <queue>
#include <tuple>
#include <vector>

#include "solution.hpp"

ListNode* vector_to_linked_list(std::vector<int>& arr) {
  ListNode* head = NULL;
  ListNode* prev = NULL;
  for (int elt : arr) {
    ListNode* current = new ListNode(elt);
    if (head == NULL)
      head = current;
    else
      prev->next = current;
    prev = current;
  }
  return head;
}

TreeNode* vector_to_b_tree(const std::vector<std::optional<int>>& vect) {
  if (vect.empty() || !vect[0].has_value()) {
    return nullptr;
  }

  TreeNode* root = new TreeNode(vect[0].value());
  std::queue<TreeNode*> node_queue;
  node_queue.push(root);
  size_t i = 1;
  while (!node_queue.empty() && i < vect.size()) {
    TreeNode* node = node_queue.front();
    node_queue.pop();

    if (vect[i].has_value()) {
      node->left = new TreeNode(vect[i].value());
      node_queue.push(node->left);
    }
    i++;

    if (i < vect.size() && vect[i].has_value()) {
      node->right = new TreeNode(vect[i].value());
      node_queue.push(node->right);
    }
    i++;
  }
  return root;
}
